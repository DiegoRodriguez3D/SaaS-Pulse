<script lang="ts">
  import { onMount, onDestroy } from "svelte";
  import {
    api,
    type KPISummary,
    type DataPoint,
    type Transaction,
  } from "$lib/api";
  import { i18n } from "$lib/i18n.svelte";
  import Header from "$lib/components/Header.svelte";
  import KpiCard from "$lib/components/KpiCard.svelte";
  import RevenueChart from "$lib/components/RevenueChart.svelte";
  import TransactionsTable from "$lib/components/TransactionsTable.svelte";

  let kpis: KPISummary | null = $state(null);
  let chartData: DataPoint[] = $state([]);
  let transactions: Transaction[] = $state([]);
  let loading = $state(true);
  let isLive = $state(false);
  let error = $state<string | null>(null);
  let pollingInterval: ReturnType<typeof setInterval> | null = null;

  let selectedRange = $state("30d");
  const ranges = [
    { value: "7d", label: "7 días" },
    { value: "30d", label: "30 días" },
    { value: "90d", label: "90 días" },
  ];

  const t = $derived(i18n.t);

  async function fetchData() {
    try {
      loading = true;
      error = null;

      const [kpiData, historyData, transactionData] = await Promise.all([
        api.getKPISummary(),
        api.getHistory(selectedRange),
        api.getTransactions(5),
      ]);

      kpis = kpiData;
      chartData = historyData.data;
      transactions = transactionData.transactions;
    } catch (e) {
      error = e instanceof Error ? e.message : "Failed to fetch data";
      console.error("API Error:", e);
    } finally {
      loading = false;
    }
  }

  function toggleLive() {
    isLive = !isLive;

    if (isLive) {
      pollingInterval = setInterval(fetchData, 3000);
    } else if (pollingInterval) {
      clearInterval(pollingInterval);
      pollingInterval = null;
    }
  }

  function changeRange(range: string) {
    selectedRange = range;
    fetchData();
  }

  onMount(() => {
    fetchData();
  });

  onDestroy(() => {
    if (pollingInterval) {
      clearInterval(pollingInterval);
    }
  });

  const formattedMRR = $derived.by(() => {
    if (!kpis) return "-";
    return (
      kpis.mrr.toLocaleString("es-ES", {
        minimumFractionDigits: 0,
        maximumFractionDigits: 0,
      }) +
      " " +
      t.currency
    );
  });
</script>

<Header {isLive} {loading} onRefresh={fetchData} onToggleLive={toggleLive} />

{#if error}
  <div
    class="bg-red-500/20 border border-red-500/50 rounded-lg p-4 mb-6 text-red-400"
  >
    <p class="font-medium">Error al conectar con la API</p>
    <p class="text-sm mt-1">{error}</p>
  </div>
{/if}

<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 mb-8">
  <KpiCard
    title={t.monthlyRevenue}
    value={formattedMRR}
    trend={kpis?.mrr_growth ?? 0}
    icon="💰"
  />
  <KpiCard
    title={t.activeUsers}
    value={kpis?.active_users ?? "-"}
    trend={8.2}
    icon="👥"
  />
  <KpiCard
    title={t.churnRate}
    value={kpis?.churn_rate ?? "-"}
    suffix="%"
    trend={kpis ? -kpis.churn_rate : 0}
    icon="📉"
  />
  <KpiCard
    title={t.newCustomers}
    value={kpis?.new_customers ?? "-"}
    trend={12.5}
    icon="🎯"
  />
</div>

<div class="mb-6">
  <div class="flex items-center justify-between mb-4">
    <h2 class="text-lg font-semibold text-white">{t.revenueTrend}</h2>
    <div class="flex gap-2">
      {#each ranges as range}
        <button
          onclick={() => changeRange(range.value)}
          class="px-3 py-1.5 text-sm rounded-lg transition-all {selectedRange ===
          range.value
            ? 'bg-indigo-600 text-white'
            : 'bg-slate-700/50 text-slate-400 hover:bg-slate-600/50'}"
        >
          {range.label}
        </button>
      {/each}
    </div>
  </div>
  <RevenueChart data={chartData} title="" currency={t.currency} />
</div>

<TransactionsTable {transactions} />

<footer class="mt-12 text-center text-slate-500 text-sm">
  <p>{t.footer}</p>
</footer>
