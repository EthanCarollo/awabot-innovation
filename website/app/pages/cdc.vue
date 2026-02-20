<template>
  <div class="min-h-screen bg-[#F5F6F7]">
    <!-- Top bar -->
    <header class="sticky top-0 z-50 bg-[#F5F6F7]/90 backdrop-blur-md border-b border-gray-200 h-20">
      <nav class="max-w-[1700px] mx-auto px-6 md:px-12 lg:px-20 h-full flex items-center justify-between relative">
        <!-- Logo -->
        <div class="flex items-center">
          <NuxtLink to="/" class="cursor-pointer">
            <img src="/logo_baseline.svg" alt="Awabot" class="h-8 md:h-10 lg:h-12 w-auto" />
          </NuxtLink>
        </div>
        
        <!-- Breadcrumb / Links -->
        <div class="flex items-center gap-3 sm:gap-4">
          <NuxtLink to="/" class="text-[11px] sm:text-[13px] font-bold uppercase tracking-wider text-[#111111]/40 hover:text-awabot-orange transition-colors">Accueil</NuxtLink>
          <div class="w-px h-4 bg-gray-300" />
          <span class="text-[11px] sm:text-[13px] font-bold uppercase tracking-wider text-awabot-orange">Cahier des charges</span>
        </div>
      </nav>
    </header>

    <div class="max-w-7xl mx-auto flex flex-col lg:flex-row gap-6 lg:gap-12 px-4 sm:px-6 py-6 sm:py-8 lg:py-12">
      <!-- Sidebar TOC -->
      <aside class="hidden lg:block w-56 shrink-0">
        <div class="sticky top-24">
          <div class="flex items-center gap-2 mb-6 ml-4">
            <div class="w-1 h-3 bg-awabot-orange rounded-full" />
            <h4 class="text-[10px] font-bold uppercase tracking-widest text-[#111111]/40">Sommaire</h4>
          </div>
          <nav v-if="page?.body?.toc?.links" class="space-y-0.5 max-h-[calc(100vh-10rem)] overflow-y-auto toc-scroll">
            <template v-for="link in page.body.toc.links" :key="link.id">
              <a
                :href="`#${link.id}`"
                class="group block text-[13px] py-1.5 px-4 rounded-r-lg transition-all duration-200 border-l-2"
                :class="activeId === link.id
                  ? 'text-awabot-orange font-bold border-awabot-orange bg-awabot-orange/5'
                  : 'text-[#111111]/50 border-transparent hover:text-awabot-orange hover:border-awabot-orange/20'"
                @click.prevent="scrollTo(link.id)"
              >
                {{ link.text }}
              </a>
              <template v-if="link.children">
                <a
                  v-for="child in link.children"
                  :key="child.id"
                  :href="`#${child.id}`"
                  class="block text-[12px] py-1 px-4 pl-8 rounded-r-lg transition-all duration-200 border-l-2"
                  :class="activeId === child.id
                    ? 'text-awabot-orange/80 font-bold border-awabot-orange/40 bg-awabot-orange/5'
                    : 'text-[#111111]/40 border-transparent hover:text-awabot-orange/70 hover:border-awabot-orange/10'"
                  @click.prevent="scrollTo(child.id)"
                >
                  {{ child.text }}
                </a>
              </template>
            </template>
          </nav>
        </div>
      </aside>

      <!-- Document -->
      <main class="flex-1 min-w-0">
        
        <!-- Mobile TOC -->
        <div class="block lg:hidden mb-6">
          <details class="bg-white rounded-2xl border border-gray-100 p-4 transition-all group">
            <summary class="font-bold text-[#111111] cursor-pointer flex justify-between items-center outline-none list-none [&::-webkit-details-marker]:hidden">
              <div class="flex items-center gap-2">
                <div class="w-1 h-3 bg-awabot-orange rounded-full" />
                <span class="text-[11px] uppercase tracking-widest text-[#111111]/60">Sommaire</span>
              </div>
              <svg class="w-5 h-5 text-gray-400 transform transition-transform group-open:rotate-180" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
              </svg>
            </summary>
            <nav v-if="page?.body?.toc?.links" class="mt-4 space-y-2 border-t border-gray-100 pt-4">
              <template v-for="link in page.body.toc.links" :key="link.id">
                <a
                  :href="`#${link.id}`"
                  class="block text-[14px] py-1 text-[#111111]/70 hover:text-awabot-orange transition-colors"
                  :class="{ 'text-awabot-orange font-bold': activeId === link.id }"
                  @click.prevent="scrollTo(link.id)"
                >
                  {{ link.text }}
                </a>
                <template v-if="link.children">
                  <a
                    v-for="child in link.children"
                    :key="child.id"
                    :href="`#${child.id}`"
                    class="block text-[13px] py-1 pl-4 text-[#111111]/50 hover:text-awabot-orange transition-colors line-clamp-1"
                    :class="{ 'text-awabot-orange font-semibold': activeId === child.id }"
                    @click.prevent="scrollTo(child.id)"
                  >
                    {{ child.text }}
                  </a>
                </template>
              </template>
            </nav>
          </details>
        </div>

        <article class="bg-white rounded-2xl sm:rounded-[32px] border border-gray-100 p-6 sm:p-10 md:p-16 lg:p-20 prose prose-slate prose-base sm:prose-lg max-w-none
          prose-headings:font-black prose-headings:tracking-tight prose-headings:text-[#111111]
          
          prose-h1:text-3xl sm:prose-h1:text-4xl prose-h1:mb-8 sm:prose-h1:mb-12 prose-h1:pb-4 sm:prose-h1:pb-6 prose-h1:border-b-4 prose-h1:border-awabot-orange
          
          prose-h2:text-xl sm:prose-h2:text-2xl prose-h2:mt-12 sm:prose-h2:mt-20 prose-h2:mb-6 sm:prose-h2:mb-8 prose-h2:flex prose-h2:items-center prose-h2:gap-2 sm:prose-h2:gap-3
          prose-h2:before:content-[''] prose-h2:before:w-1.5 sm:prose-h2:before:w-2 prose-h2:before:h-6 sm:prose-h2:before:h-8 prose-h2:before:bg-awabot-orange prose-h2:before:rounded-full
          prose-h2:border-none
          
          prose-h3:text-lg sm:prose-h3:text-xl prose-h3:mt-8 sm:prose-h3:mt-12 prose-h3:text-awabot-orange/90 prose-h3:font-extrabold
          
          prose-p:text-[#111111]/70 prose-p:leading-[1.7] sm:prose-p:leading-[1.8] prose-p:text-[15px] sm:prose-p:text-[17px]
          
          prose-li:text-[#111111]/70 prose-li:marker:text-awabot-orange prose-li:my-1 prose-li:text-[15px] sm:prose-li:text-[17px]
          
          prose-strong:text-[#111111] prose-strong:font-bold
          
          prose-a:text-awabot-orange prose-a:font-semibold prose-a:decoration-2 prose-a:underline-offset-4 hover:prose-a:text-awabot-yellow transition-colors break-words
          
          prose-code:text-awabot-orange prose-code:bg-awabot-orange/5 prose-code:px-1.5 sm:prose-code:px-2 prose-code:py-0.5 prose-code:rounded-md sm:prose-code:rounded-lg prose-code:font-bold prose-code:text-[0.85em] sm:prose-code:text-[0.9em] prose-code:before:content-none prose-code:after:content-none prose-code:break-words
          
          prose-blockquote:border-l-4 prose-blockquote:border-awabot-yellow prose-blockquote:bg-awabot-yellow/5 prose-blockquote:py-2 prose-blockquote:px-5 sm:prose-blockquote:px-8 prose-blockquote:rounded-r-xl sm:prose-blockquote:rounded-r-2xl prose-blockquote:italic prose-blockquote:text-[#111111]/80 prose-blockquote:before:content-none prose-blockquote:after:content-none prose-blockquote:text-[15px] sm:prose-blockquote:text-[17px]
          
          prose-table:text-[13px] sm:prose-table:text-[15px] prose-table:border-collapse prose-table:my-8 sm:prose-table:my-10 prose-table:block prose-table:overflow-x-auto prose-table:w-full
          prose-th:bg-[#F5F6F7] prose-th:text-[#111111] prose-th:p-3 sm:prose-th:p-4 prose-th:font-bold prose-th:border prose-th:border-gray-200 prose-th:whitespace-nowrap
          prose-td:p-3 sm:prose-td:p-4 prose-td:border prose-td:border-gray-100 prose-td:text-gray-600
          
          prose-img:my-8 sm:prose-img:my-12 prose-img:mx-auto prose-img:rounded-lg
          
          prose-hr:my-10 sm:prose-hr:my-16 prose-hr:border-gray-100
        ">
          <ContentRenderer v-if="page" :value="page" />
        </article>
      </main>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'

useHead({ 
  title: 'Cahier des Charges — Awabot',
  meta: [
    { name: 'description', content: 'Cahier des charges technique et fonctionnel pour le projet de modernisation Nuxt.js d\'Awabot.' }
  ]
})

const { data: page } = await useAsyncData('cdc', () =>
  queryCollection('content').path('/cdc').first()
)

const activeId = ref('')

function scrollTo(id: string) {
  const el = document.getElementById(id)
  if (el) {
    const yOffset = -100
    const y = el.getBoundingClientRect().top + window.pageYOffset + yOffset
    window.scrollTo({ top: y, behavior: 'smooth' })
    activeId.value = id
  }
}

let observer: IntersectionObserver | null = null

onMounted(() => {
  const headings = document.querySelectorAll('article h1[id], article h2[id], article h3[id]')

  observer = new IntersectionObserver(
    (entries) => {
      // Find the first entry that is intersecting
      const visible = entries.find(e => e.isIntersecting)
      if (visible) {
        activeId.value = visible.target.id
      }
    },
    { 
      rootMargin: '-10% 0px -80% 0px', // Trigger when heading is near top
      threshold: 0 
    }
  )

  headings.forEach((h) => observer!.observe(h))

  // Initial active state based on hash
  if (window.location.hash) {
    activeId.value = window.location.hash.slice(1)
  }
})

onUnmounted(() => {
  observer?.disconnect()
})
</script>

<style>
.toc-scroll::-webkit-scrollbar {
  width: 4px;
}
.toc-scroll::-webkit-scrollbar-track {
  background: transparent;
}
.toc-scroll::-webkit-scrollbar-thumb {
  background: #FF7E22;
  border-radius: 99px;
  opacity: 0.2;
}

@media print {
  nav, aside { display: none !important; }
  .min-h-screen { background: white !important; }

  article {
    box-shadow: none !important;
    border: none !important;
    border-radius: 0 !important;
    padding: 0 !important;
    font-size: 12pt;
  }

  main {
    padding: 0 !important;
    max-width: 100% !important;
  }

  h1, h2, h3 { page-break-after: avoid; }
  pre, blockquote, img { page-break-inside: avoid; }
}
</style>
