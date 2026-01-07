"""
Mock data configuration.
"""

from dataclasses import dataclass
import unicodedata

PLANS = [
    {"name": "Básico", "price": 29, "weight": 50},
    {"name": "Profesional", "price": 99, "weight": 35},
    {"name": "Empresa", "price": 299, "weight": 15},
]

SAMPLE_CUSTOMERS = [
    {"first": "María", "last": "García López"},
    {"first": "Carlos", "last": "Rodríguez Martínez"},
    {"first": "Ana", "last": "Fernández Sánchez"},
    {"first": "Javier", "last": "López Hernández"},
    {"first": "Laura", "last": "Martínez Ruiz"},
    {"first": "Pedro", "last": "Sánchez García"},
    {"first": "Elena", "last": "González Díaz"},
    {"first": "Miguel", "last": "Pérez Torres"},
    {"first": "Lucía", "last": "Romero Navarro"},
    {"first": "David", "last": "Jiménez Moreno"},
    {"first": "Carmen", "last": "Ruiz Molina"},
    {"first": "Antonio", "last": "Díaz Serrano"},
    {"first": "Isabel", "last": "Moreno Castro"},
    {"first": "Francisco", "last": "Álvarez Ortega"},
    {"first": "Paula", "last": "Muñoz Delgado"},
]

EMAIL_DOMAINS = [
    "techsolutions.es",
    "innovatech.com",
    "dataservices.es", 
    "cloudpyme.es",
    "digitalpro.com",
    "softwareib.es",
    "consultoriatech.com",
    "empresadigital.es",
]


@dataclass
class KPIRanges:
    mrr_min: float = 15000.0
    mrr_max: float = 45000.0
    active_users_min: int = 200
    active_users_max: int = 800
    churn_rate_min: float = 2.0
    churn_rate_max: float = 5.0
    new_customers_min: int = 15
    new_customers_max: int = 60
    mrr_growth_min: float = 3.0
    mrr_growth_max: float = 18.0


@dataclass  
class RevenueConfig:
    base_daily_revenue: float = 900.0
    growth_factor: float = 1.5
    volatility: float = 50.0
    weekend_dip: float = 0.7


KPI_CONFIG = KPIRanges()
REVENUE_CONFIG = RevenueConfig()


def generate_email(first_name: str, last_name: str, domain: str) -> str:
    def normalize(s: str) -> str:
        nfkd = unicodedata.normalize('NFKD', s)
        return ''.join(c for c in nfkd if not unicodedata.combining(c)).lower()
    
    first = normalize(first_name)
    last = normalize(last_name.split()[0])
    
    return f"{first}.{last}@{domain}"
