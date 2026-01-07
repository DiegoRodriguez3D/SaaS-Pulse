/**
 * API client for SaaS Pulse backend.
 */

const API_BASE = (import.meta.env.VITE_API_URL || 'http://localhost:8000') + '/api';

export interface KPISummary {
    mrr: number;
    active_users: number;
    churn_rate: number;
    new_customers: number;
    mrr_growth: number;
}

export interface DataPoint {
    date: string;
    value: number;
}

export interface HistoryResponse {
    metric: string;
    range_days: number;
    data: DataPoint[];
}

export interface Transaction {
    id: string;
    customer_name: string;
    email: string;
    amount: number;
    plan: string;
    date: string;
    status: string;
}

export interface TransactionsResponse {
    transactions: Transaction[];
    total: number;
}

export interface HealthStatus {
    status: string;
    timestamp: string;
    version: string;
}

async function fetchJson<T>(endpoint: string): Promise<T> {
    const response = await fetch(`${API_BASE}${endpoint}`);
    if (!response.ok) {
        throw new Error(`API error: ${response.status}`);
    }
    return response.json();
}

export const api = {
    getStatus: () => fetchJson<HealthStatus>('/status'),
    getKPISummary: () => fetchJson<KPISummary>('/kpi/summary'),
    getHistory: (range = '30d') => fetchJson<HistoryResponse>(`/kpi/history?range=${range}`),
    getTransactions: (limit = 5) => fetchJson<TransactionsResponse>(`/transactions?limit=${limit}`),
};
