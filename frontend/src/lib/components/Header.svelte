<script lang="ts">
  import { i18n } from "$lib/i18n.svelte";

  interface Props {
    isLive: boolean;
    onRefresh: () => void;
    onToggleLive: () => void;
    loading?: boolean;
  }

  let { isLive, onRefresh, onToggleLive, loading = false }: Props = $props();

  const t = $derived(i18n.t);
</script>

<header class="mb-8">
  <div
    class="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4"
  >
    <div class="flex items-center gap-4">
      <img
        src="/logo.png"
        alt="SaaS Pulse Logo"
        class="w-12 h-12 rounded-xl shadow-lg"
      />
      <div>
        <h1 class="text-3xl font-bold gradient-text">{t.title}</h1>
        <p class="text-slate-400 text-sm">{t.subtitle}</p>
      </div>
    </div>

    <div class="flex items-center gap-3">
      <a
        href="https://diego-rodriguez.es"
        class="flex items-center gap-2 px-3 py-2 rounded-lg bg-slate-700/50 text-slate-300
               border border-slate-600 hover:bg-slate-600/50 transition-all text-sm font-medium"
      >
        <svg
          class="w-4 h-4"
          fill="none"
          stroke="currentColor"
          viewBox="0 0 24 24"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M10 19l-7-7m0 0l7-7m-7 7h18"
          />
        </svg>
        {t.backToPortfolio}
      </a>

      <button
        onclick={() => i18n.toggle()}
        class="flex items-center gap-2 px-3 py-2 rounded-lg bg-slate-700/50 text-slate-300
               border border-slate-600 hover:bg-slate-600/50 transition-all text-sm font-medium"
      >
        {i18n.language === "es" ? "🇪🇸 ES" : "🇬🇧 EN"}
      </button>

      <button
        onclick={onToggleLive}
        class="flex items-center gap-2 px-4 py-2 rounded-lg transition-all {isLive
          ? 'bg-emerald-500/20 text-emerald-400 border border-emerald-500/50'
          : 'bg-slate-700/50 text-slate-400 border border-slate-600'}"
      >
        <span class="relative flex h-2 w-2">
          {#if isLive}
            <span
              class="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"
            ></span>
          {/if}
          <span
            class="relative inline-flex rounded-full h-2 w-2 {isLive
              ? 'bg-emerald-400'
              : 'bg-slate-500'}"
          ></span>
        </span>
        {isLive ? t.live : t.paused}
      </button>

      <button
        onclick={onRefresh}
        disabled={loading}
        class="flex items-center gap-2 px-4 py-2 bg-indigo-600 hover:bg-indigo-500 disabled:opacity-50
               text-white rounded-lg transition-all font-medium"
      >
        <svg
          class="w-4 h-4 {loading ? 'animate-spin' : ''}"
          fill="none"
          stroke="currentColor"
          viewBox="0 0 24 24"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"
          />
        </svg>
        {t.refresh}
      </button>
    </div>
  </div>
</header>
