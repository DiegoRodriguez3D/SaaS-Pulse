"""
Pydantic models for API responses.
"""

from pydantic import BaseModel, Field
from typing import List


class KPISummary(BaseModel):
    mrr: float = Field(description="Monthly Recurring Revenue")
    active_users: int
    churn_rate: float
    new_customers: int
    mrr_growth: float


class DataPoint(BaseModel):
    date: str
    value: float


class HistoryResponse(BaseModel):
    metric: str
    range_days: int
    data: List[DataPoint]


class Transaction(BaseModel):
    id: str
    customer_name: str
    email: str
    amount: float
    plan: str
    date: str
    status: str


class TransactionsResponse(BaseModel):
    transactions: List[Transaction]
    total: int


class HealthStatus(BaseModel):
    status: str
    timestamp: str
    version: str
