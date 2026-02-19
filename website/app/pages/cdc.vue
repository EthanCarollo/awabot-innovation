<template>
  <div class="min-h-screen bg-slate-50">
    <!-- Top bar -->
    <nav class="sticky top-0 z-50 bg-white/80 backdrop-blur-md border-b border-slate-200">
      <div class="max-w-4xl mx-auto px-8 py-4 flex items-center justify-between">
        <NuxtLink to="/" class="text-lg font-extrabold tracking-tight text-slate-900">
          awa<span class="text-blue-500">bot</span>
        </NuxtLink>
        <span class="text-sm font-medium text-slate-400">Cahier des charges</span>
      </div>
    </nav>

    <!-- Document -->
    <main class="max-w-4xl mx-auto px-8 py-12">
      <article class="bg-white rounded-2xl shadow-sm border border-slate-200 p-12 md:p-16 prose prose-slate prose-lg max-w-none
        prose-headings:font-bold prose-headings:tracking-tight
        prose-h1:text-3xl prose-h1:text-slate-900 prose-h1:pb-4 prose-h1:border-b-2 prose-h1:border-blue-500
        prose-h2:text-xl prose-h2:text-slate-800 prose-h2:mt-12 prose-h2:pb-2 prose-h2:border-b prose-h2:border-slate-200
        prose-h3:text-lg prose-h3:text-slate-700
        prose-p:text-slate-600 prose-p:leading-relaxed
        prose-li:text-slate-600 prose-li:marker:text-blue-400
        prose-strong:text-slate-800
        prose-a:text-blue-500 prose-a:no-underline hover:prose-a:underline
        prose-code:text-blue-600 prose-code:bg-blue-50 prose-code:px-1.5 prose-code:py-0.5 prose-code:rounded prose-code:text-sm prose-code:before:content-none prose-code:after:content-none
        prose-blockquote:border-blue-400 prose-blockquote:bg-blue-50/50 prose-blockquote:rounded-r-xl prose-blockquote:text-blue-900
        prose-table:text-sm
        prose-th:bg-slate-50 prose-th:text-slate-700
        prose-td:border-slate-200
      ">
        <ContentRenderer v-if="page" :value="page" />
      </article>

      <!-- Footer -->
      <div class="text-center py-10 text-sm text-slate-400">
        Awabot — Cahier des Charges · {{ new Date().getFullYear() }}
      </div>
    </main>
  </div>
</template>

<script setup lang="ts">
useHead({ title: 'Cahier des Charges — Awabot' })

const { data: page } = await useAsyncData('cdc', () =>
  queryCollection('content').path('/cdc').first()
)
</script>

<style>
@media print {
  nav { display: none !important; }

  .min-h-screen { background: white !important; }

  article {
    box-shadow: none !important;
    border: none !important;
    border-radius: 0 !important;
    padding: 0 !important;
  }

  main {
    padding: 0 !important;
    max-width: 100% !important;
  }
}
</style>
