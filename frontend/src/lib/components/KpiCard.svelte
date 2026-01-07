<script lang="ts">
  interface Props {
    title: string;
    value: string | number;
    suffix?: string;
    trend?: number;
    icon?: string;
  }
  
  let { title, value, suffix = '', trend = 0, icon = '📊' }: Props = $props();
  
  const trendClass = $derived(
    trend > 0 ? 'text-emerald-400' : trend < 0 ? 'text-red-400' : 'text-slate-400'
  );
  
  const trendIcon = $derived(
    trend > 0 ? '↑' : trend < 0 ? '↓' : '→'
  );
</script>

<div class="card group">
  <div class="flex items-start justify-between mb-4">
    <span class="text-2xl">{icon}</span>
    {#if trend !== 0}
      <span class="{trendClass} text-sm font-medium flex items-center gap-1">
        {trendIcon} {Math.abs(trend)}%
      </span>
    {/if}
  </div>
  
  <h3 class="text-slate-400 text-sm font-medium uppercase tracking-wider mb-2">
    {title}
  </h3>
  
  <p class="text-3xl font-bold text-white">
    {value}<span class="text-xl text-slate-400 ml-1">{suffix}</span>
  </p>
</div>
