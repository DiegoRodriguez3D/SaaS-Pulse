<script lang="ts">
  import type { Transaction } from "$lib/api";
  import { i18n } from "$lib/i18n.svelte";

  interface Props {
    transactions: Transaction[];
  }

  let { transactions }: Props = $props();

  const t = $derived(i18n.t);

  const statusClass = (status: string) => {
    return status === "completado" || status === "completed"
      ? "bg-emerald-500/20 text-emerald-400"
      : "bg-amber-500/20 text-amber-400";
  };

  const statusText = (status: string) => {
    if (status === "completado" || status === "completed") {
      return t.completed;
    }
    return t.pending;
  };

  const planClass = (plan: string) => {
    switch (plan) {
      case "Enterprise":
      case "Empresa":
        return "bg-purple-500/20 text-purple-400";
      case "Professional":
      case "Profesional":
        return "bg-blue-500/20 text-blue-400";
      default:
        return "bg-slate-500/20 text-slate-400";
    }
  };
</script>

<div class="card">
  <h3 class="text-slate-400 text-sm font-medium uppercase tracking-wider mb-4">
    {t.recentTransactions}
  </h3>

  <div class="overflow-x-auto">
    <table class="w-full">
      <thead>
        <tr class="text-left text-slate-400 text-sm border-b border-slate-700">
          <th class="pb-3 font-medium">{t.customer}</th>
          <th class="pb-3 font-medium">{t.plan}</th>
          <th class="pb-3 font-medium">{t.amount}</th>
          <th class="pb-3 font-medium">{t.status}</th>
          <th class="pb-3 font-medium">{t.date}</th>
        </tr>
      </thead>
      <tbody>
        {#each transactions as tx (tx.id)}
          <tr
            class="border-b border-slate-700/50 hover:bg-slate-700/30 transition-colors cursor-pointer"
          >
            <td class="py-4">
              <div>
                <p class="text-white font-medium">{tx.customer_name}</p>
                <p class="text-slate-500 text-sm">{tx.email}</p>
              </div>
            </td>
            <td class="py-4">
              <span
                class="px-2 py-1 rounded-full text-xs font-medium {planClass(
                  tx.plan,
                )}"
              >
                {tx.plan}
              </span>
            </td>
            <td class="py-4 text-white font-medium">
              {tx.amount.toLocaleString("es-ES")}
              {t.currency}
            </td>
            <td class="py-4">
              <span
                class="px-2 py-1 rounded-full text-xs font-medium capitalize {statusClass(
                  tx.status,
                )}"
              >
                {statusText(tx.status)}
              </span>
            </td>
            <td class="py-4 text-slate-400 text-sm">
              {tx.date}
            </td>
          </tr>
        {/each}
      </tbody>
    </table>
  </div>
</div>
