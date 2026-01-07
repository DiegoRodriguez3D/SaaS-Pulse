"""
Data generation services using Pandas.
Uses mock_data.py for consistent, realistic sample data.
"""

import random
from datetime import datetime, timedelta
from typing import List

import pandas as pd

from app.models import (
    KPISummary,
    DataPoint,
    HistoryResponse,
    Transaction,
    TransactionsResponse,
)
from app.mock_data import (
    PLANS,
    SAMPLE_CUSTOMERS,
    EMAIL_DOMAINS,
    KPI_CONFIG,
    REVENUE_CONFIG,
    generate_email,
)


def generate_kpi_summary() -> KPISummary:
    """Generate realistic SaaS KPI metrics using configured ranges."""
    cfg = KPI_CONFIG
    
    return KPISummary(
        mrr=round(random.uniform(cfg.mrr_min, cfg.mrr_max), 2),
        active_users=random.randint(cfg.active_users_min, cfg.active_users_max),
        churn_rate=round(random.uniform(cfg.churn_rate_min, cfg.churn_rate_max), 2),
        new_customers=random.randint(cfg.new_customers_min, cfg.new_customers_max),
        mrr_growth=round(random.uniform(cfg.mrr_growth_min, cfg.mrr_growth_max), 2),
    )


def generate_history_data(range_days: int = 30, metric: str = "revenue") -> HistoryResponse:
    """
    Generate time series data using Pandas DataFrame.
    Creates realistic revenue patterns with trends and variance.
    """
    cfg = REVENUE_CONFIG
    end_date = datetime.now()
    start_date = end_date - timedelta(days=range_days)
    
    # Create date range using Pandas
    dates = pd.date_range(start=start_date, end=end_date, freq="D")
    
    df = pd.DataFrame({"date": dates})
    
    # Add day of week for weekend detection (0=Monday, 6=Sunday)
    df["day_of_week"] = df["date"].dt.dayofweek
    
    # Base value with cumulative growth trend
    df["base"] = cfg.base_daily_revenue + (df.index * cfg.growth_factor)
    
    # Add controlled random noise
    random.seed(42)  # Reproducible for demo consistency
    df["noise"] = [random.uniform(-cfg.volatility, cfg.volatility) for _ in range(len(df))]
    
    # Apply weekend dip
    df["weekend_factor"] = df["day_of_week"].apply(
        lambda x: cfg.weekend_dip if x >= 5 else 1.0
    )
    
    # Calculate final value
    df["value"] = (df["base"] + df["noise"]) * df["weekend_factor"]
    df["value"] = df["value"].clip(lower=0).round(2)
    
    # Reset random seed for other calls
    random.seed()
    
    # Convert to API response format
    data_points: List[DataPoint] = [
        DataPoint(
            date=row["date"].strftime("%Y-%m-%d"),
            value=row["value"]
        )
        for _, row in df.iterrows()
    ]
    
    return HistoryResponse(
        metric=metric,
        range_days=range_days,
        data=data_points
    )


def generate_transactions(count: int = 5) -> TransactionsResponse:
    """Generate realistic transactions with consistent customer data."""
    transactions: List[Transaction] = []
    
    # Select random customers without repetition
    selected_customers = random.sample(
        SAMPLE_CUSTOMERS, 
        min(count, len(SAMPLE_CUSTOMERS))
    )
    
    for customer in selected_customers:
        # Select plan based on weight distribution
        plan_weights = [p["weight"] for p in PLANS]
        plan = random.choices(PLANS, weights=plan_weights, k=1)[0]
        
        # Generate transaction date (last 7 days)
        days_ago = random.randint(0, 7)
        hours_ago = random.randint(0, 23)
        transaction_date = datetime.now() - timedelta(days=days_ago, hours=hours_ago)
        
        # Generate consistent email from name
        domain = random.choice(EMAIL_DOMAINS)
        full_name = f"{customer['first']} {customer['last']}"
        email = generate_email(customer['first'], customer['last'], domain)
        
        transactions.append(
            Transaction(
                id=f"TX{random.randint(10000, 99999)}",
                customer_name=full_name,
                email=email,
                amount=float(plan["price"]),
                plan=plan["name"],
                date=transaction_date.strftime("%Y-%m-%d %H:%M"),
                status=random.choices(
                    ["completado", "pendiente"], 
                    weights=[85, 15], 
                    k=1
                )[0],
            )
        )
    
    # Sort by date descending
    transactions.sort(key=lambda x: x.date, reverse=True)
    
    return TransactionsResponse(
        transactions=transactions,
        total=len(transactions)
    )
