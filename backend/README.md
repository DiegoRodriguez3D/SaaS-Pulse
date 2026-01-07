# SaaS Pulse - Backend

FastAPI backend for the SaaS Pulse dashboard.

## Quick Start

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

## API Documentation

Once running, visit http://localhost:8000/docs for interactive Swagger UI.

## Endpoints

- `GET /api/status` - Health check
- `GET /api/kpi/summary` - Current KPI metrics
- `GET /api/kpi/history?range=30d` - Time series data
- `GET /api/transactions?limit=5` - Recent transactions
