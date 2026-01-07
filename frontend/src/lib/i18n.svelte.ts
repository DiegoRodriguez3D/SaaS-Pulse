/**
 * Internationalization store.
 */

type Language = 'es' | 'en';

interface Translations {
    title: string;
    subtitle: string;
    live: string;
    paused: string;
    refresh: string;
    monthlyRevenue: string;
    activeUsers: string;
    churnRate: string;
    newCustomers: string;
    revenueTrend: string;
    recentTransactions: string;
    customer: string;
    plan: string;
    amount: string;
    status: string;
    date: string;
    completed: string;
    pending: string;
    footer: string;
    currency: string;
}

const translations: Record<Language, Translations> = {
    es: {
        title: 'SaaS Pulse',
        subtitle: 'Panel de métricas de negocio en tiempo real',
        live: 'En vivo',
        paused: 'Pausado',
        refresh: 'Actualizar',
        monthlyRevenue: 'Ingresos Mensuales',
        activeUsers: 'Usuarios Activos',
        churnRate: 'Tasa de Abandono',
        newCustomers: 'Nuevos Clientes',
        revenueTrend: 'Evolución de Ingresos',
        recentTransactions: 'Transacciones Recientes',
        customer: 'Cliente',
        plan: 'Plan',
        amount: 'Importe',
        status: 'Estado',
        date: 'Fecha',
        completed: 'completado',
        pending: 'pendiente',
        footer: 'Desarrollado con FastAPI + SvelteKit',
        currency: '€',
    },
    en: {
        title: 'SaaS Pulse',
        subtitle: 'Real-time business metrics dashboard',
        live: 'Live',
        paused: 'Paused',
        refresh: 'Refresh',
        monthlyRevenue: 'Monthly Revenue',
        activeUsers: 'Active Users',
        churnRate: 'Churn Rate',
        newCustomers: 'New Customers',
        revenueTrend: 'Revenue Trend',
        recentTransactions: 'Recent Transactions',
        customer: 'Customer',
        plan: 'Plan',
        amount: 'Amount',
        status: 'Status',
        date: 'Date',
        completed: 'completed',
        pending: 'pending',
        footer: 'Built with FastAPI + SvelteKit',
        currency: '€',
    }
};

class I18nStore {
    language = $state<Language>('es');

    get t(): Translations {
        return translations[this.language];
    }

    toggle() {
        this.language = this.language === 'es' ? 'en' : 'es';
    }

    setLanguage(lang: Language) {
        this.language = lang;
    }
}

export const i18n = new I18nStore();
