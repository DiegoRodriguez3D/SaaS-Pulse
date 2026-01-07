<script lang="ts">
  import "../app.css";

  interface Props {
    children: import("svelte").Snippet;
  }

  let { children }: Props = $props();
</script>

<svelte:head>
  <link rel="icon" type="image/png" href="/logo.png" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link
    rel="preconnect"
    href="https://fonts.gstatic.com"
    crossorigin="anonymous"
  />
  <link
    href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap"
    rel="stylesheet"
  />
  <title>SaaS Pulse | Dashboard</title>
  <meta
    name="description"
    content="Panel de métricas de negocio SaaS en tiempo real - Demo FastAPI & SvelteKit"
  />
</svelte:head>

<div class="min-h-screen px-4 py-8 sm:px-6 lg:px-8">
  <div class="max-w-7xl mx-auto">
    {@render children()}
  </div>
</div>
