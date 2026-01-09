<script lang="ts">
  import { onMount, onDestroy } from "svelte";
  import {
    Chart,
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    LineController,
    Title,
    Tooltip,
    Legend,
    Filler,
  } from "chart.js";
  import type { DataPoint } from "$lib/api";

  interface Props {
    data: DataPoint[];
    label?: string;
    title?: string;
    currency?: string;
  }

  let {
    data,
    label = "Ingresos",
    title = "Evolución de Ingresos",
    currency = "€",
  }: Props = $props();

  let canvas: HTMLCanvasElement;
  
  let chart: Chart | null = null;
  let mounted = $state(false);

  Chart.register(
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    LineController,
    Title,
    Tooltip,
    Legend,
    Filler,
  );

  function createChart() {
    if (!canvas || !mounted) return;

    if (chart) {
      chart.destroy();
      chart = null;
    }

    if (data.length === 0) return;

    const ctx = canvas.getContext("2d");
    if (!ctx) return;

    const gradient = ctx.createLinearGradient(0, 0, 0, 300);
    gradient.addColorStop(0, "rgba(99, 102, 241, 0.3)");
    gradient.addColorStop(1, "rgba(99, 102, 241, 0)");

    chart = new Chart(ctx, {
      type: "line",
      data: {
        labels: data.map((d) => {
          const [, month, day] = d.date.split("-");
          return `${day}/${month}`;
        }),
        datasets: [
          {
            label,
            data: data.map((d) => d.value),
            borderColor: "#6366f1",
            backgroundColor: gradient,
            fill: true,
            tension: 0.4,
            pointRadius: 0,
            pointHoverRadius: 6,
            pointHoverBackgroundColor: "#6366f1",
            pointHoverBorderColor: "#fff",
            pointHoverBorderWidth: 2,
          },
        ],
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        animation: { duration: 750 },
        plugins: {
          legend: { display: false },
          tooltip: {
            backgroundColor: "#1e293b",
            titleColor: "#f8fafc",
            bodyColor: "#94a3b8",
            borderColor: "#334155",
            borderWidth: 1,
            padding: 12,
            displayColors: false,
            callbacks: {
              label: (context) => {
                const value = context.parsed?.y ?? 0;
                return `${value.toLocaleString("es-ES")} ${currency}`;
              },
            },
          },
        },
        scales: {
          x: {
            grid: { color: "rgba(51, 65, 85, 0.5)" },
            ticks: { color: "#94a3b8", font: { size: 11 } },
          },
          y: {
            grid: { color: "rgba(51, 65, 85, 0.5)" },
            ticks: {
              color: "#94a3b8",
              font: { size: 11 },
              callback: (value) =>
                (value as number).toLocaleString("es-ES") + " " + currency,
            },
          },
        },
        interaction: {
          intersect: false,
          mode: "index",
        },
      },
    });
  }

  onMount(() => {
    mounted = true;
  });

  onDestroy(() => {
    if (chart) {
      chart.destroy();
      chart = null;
    }
  });

  $effect(() => {
    const hasData = data.length > 0;
    if (mounted && hasData && canvas) {
      createChart();
    }
  });
</script>

<div class="card">
  {#if title}
    <h3
      class="text-slate-400 text-sm font-medium uppercase tracking-wider mb-4"
    >
      {title}
    </h3>
  {/if}
  <div class="h-72">
    {#if data.length === 0}
      <div class="h-full flex items-center justify-center text-slate-500">
        <div class="text-center">
          <div class="animate-pulse text-4xl mb-2">📊</div>
          <p>Cargando datos...</p>
        </div>
      </div>
    {:else}
      <canvas bind:this={canvas}></canvas>
    {/if}
  </div>
</div>
