"""
Pydantic models for API responses.
Defines the data structures for KPIs, time series, and transactions.
"""

from pydantic import BaseModel, Field
from typing import List
from datetime import datetime


class KPISummary(BaseModel):
    """Main dashboard KPI metrics."""
    mrr: float = Field(description="Monthly Recurring Revenue in USD")
    active_users: int = Field(description="Number of active users")
    churn_rate: float = Field(description="Monthly churn rate as percentage")
    new_customers: int = Field(description="New customers this month")
    mrr_growth: float = Field(description="MRR growth percentage vs last month")


class DataPoint(BaseModel):
    """Single point in a time series."""
    date: str
    value: float


class HistoryResponse(BaseModel):
    """Time series data for charts."""
    metric: str
    range_days: int
    data: List[DataPoint]


class Transaction(BaseModel):
    """Recent transaction record."""
    id: str
    customer_name: str
    email: str
    amount: float
    plan: str
    date: str
    status: str


class TransactionsResponse(BaseModel):
    """List of recent transactions."""
    transactions: List[Transaction]
    total: int


class HealthStatus(BaseModel):
    """API health check response."""
    status: str
    timestamp: str
    version: str
