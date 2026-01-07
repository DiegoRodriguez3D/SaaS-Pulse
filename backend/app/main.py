"""
SaaS Pulse API
"""

from datetime import datetime

from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

from app.models import KPISummary, HistoryResponse, TransactionsResponse, HealthStatus
from app.services import generate_kpi_summary, generate_history_data, generate_transactions

app = FastAPI(
    title="SaaS Pulse API",
    description="Backend API for SaaS metrics visualization dashboard",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/status", response_model=HealthStatus, tags=["Health"])
async def health_check() -> HealthStatus:
    return HealthStatus(
        status="healthy",
        timestamp=datetime.now().isoformat(),
        version="1.0.0"
    )


@app.get("/api/kpi/summary", response_model=KPISummary, tags=["KPIs"])
async def get_kpi_summary() -> KPISummary:
    return generate_kpi_summary()


@app.get("/api/kpi/history", response_model=HistoryResponse, tags=["KPIs"])
async def get_kpi_history(
    range: str = Query(default="30d", regex="^\\d+d$", description="Time range (e.g., 7d, 30d, 90d)"),
    metric: str = Query(default="revenue", description="Metric to retrieve")
) -> HistoryResponse:
    range_days = int(range.replace("d", ""))
    return generate_history_data(range_days=range_days, metric=metric)


@app.get("/api/transactions", response_model=TransactionsResponse, tags=["Transactions"])
async def get_transactions(
    limit: int = Query(default=5, ge=1, le=20, description="Number of transactions to return")
) -> TransactionsResponse:
    return generate_transactions(count=limit)
