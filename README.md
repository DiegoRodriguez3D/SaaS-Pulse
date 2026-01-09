# SaaS Pulse 📊

**Panel de métricas SaaS en tiempo real** | **Real-time SaaS metrics dashboard**

---

## 🇪🇸 Español

### Descripción

SaaS Pulse es una aplicación de demostración que visualiza métricas de negocio simuladas en tiempo real. Desarrollada para demostrar competencias Full Stack con FastAPI y SvelteKit.

### Características

- **4 Tarjetas KPI**: Ingresos mensuales, usuarios activos, tasa de abandono, nuevos clientes
- **Gráfico de ingresos**: Chart.js con gradiente y animaciones suaves
- **Selector de rango temporal**: 7 días / 30 días / 90 días
- **Tabla de transacciones**: Datos de clientes de ejemplo
- **Modo en vivo**: Auto-actualización cada 3 segundos
- **Cambio de idioma**: Toggle español/inglés
- **Datos**: Nombres, emails y moneda en euros (€)

### Stack Tecnológico

#### Backend
| Tecnología | Uso |
|------------|-----|
| **Python 3.12** | Lenguaje principal |
| **FastAPI** | Framework API REST asíncrono |
| **Pydantic** | Validación y serialización |
| **Pandas** | Generación de series temporales |

#### Frontend
| Tecnología | Uso |
|------------|-----|
| **SvelteKit** | Framework full-stack |
| **TypeScript** | Tipado estático |
| **Tailwind CSS v4** | Estilos utilitarios |
| **Chart.js** | Gráficos interactivos |

### Despliegue
El backend está desplegado en una instancia gratuita de **Render**. Si la aplicación lleva tiempo inactiva, **la primera carga de datos puede tardar hasta 50 segundos** mientras el servidor "despierta" (Cold Start). Las siguientes peticiones serán instantáneas.

- **Dashboard**: https://saas-pulse-one.vercel.app
- **API Docs**: https://saas-pulse-api.onrender.com/docs

### Estructura del Proyecto

```
saas-pulse/
├── backend/
│   ├── app/
│   │   ├── main.py         # Endpoints FastAPI
│   │   ├── models.py       # Esquemas Pydantic
│   │   ├── services.py     # Lógica de generación
│   │   └── mock_data.py    # Datos de prueba centralizados
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── lib/
│   │   │   ├── api.ts              # Cliente API tipado
│   │   │   ├── i18n.svelte.ts      # Traducciones ES/EN
│   │   │   └── components/         # Componentes Svelte
│   │   └── routes/
│   │       └── +page.svelte        # Dashboard principal
│   ├── .env.example                # Variables de entorno
│   └── package.json
├── screenshot.png
└── README.md
```

---

### 📄 Licencia

MIT License

---

Desarrollado con ❤️ usando FastAPI + SvelteKit  

## 🇬🇧 English

### Description

SaaS Pulse is a demo application that visualizes simulated business metrics in real-time. Built to demonstrate Full Stack capabilities with FastAPI and SvelteKit.

### Features

- **4 KPI Cards**: Monthly revenue, active users, churn rate, new customers
- **Revenue chart**: Chart.js with gradient fill and smooth animations
- **Time range selector**: 7 days / 30 days / 90 days
- **Transactions table**: Example customer data
- **Live mode**: Auto-refresh every 3 seconds
- **Language toggle**: Spanish/English switch
- **Data**: Names, emails, and Euro currency (€)

### Tech Stack

#### Backend
| Technology | Purpose |
|------------|---------|
| **Python 3.12** | Core language |
| **FastAPI** | Async REST API framework |
| **Pydantic** | Validation & serialization |
| **Pandas** | Time series data generation |

#### Frontend
| Technology | Purpose |
|------------|---------|
| **SvelteKit** | Full-stack framework |
| **TypeScript** | Type-safe development |
| **Tailwind CSS v4** | Utility-first styling |
| **Chart.js** | Interactive charts |

### Deployment
The backend is deployed on a free Render instance. If the application has been inactive, the initial data load may take up to 50 seconds while the server 'wakes up' (Cold Start). Subsequent requests will be instantaneous.

- **Dashboard**: https://saas-pulse-one.vercel.app
- **API Docs**: https://saas-pulse-api.onrender.com/docs

### API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/status` | Health check |
| GET | `/api/kpi/summary` | Current KPIs |
| GET | `/api/kpi/history?range=30d` | Time series data |
| GET | `/api/transactions?limit=5` | Recent transactions |

---

### 📄 License

MIT License

---

Built with ❤️ using FastAPI + SvelteKit
