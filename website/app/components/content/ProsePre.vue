<template>
  <div v-if="isMermaid" class="my-8">
    <ClientOnly>
      <div ref="mermaidEl" class="flex justify-center overflow-x-auto" />
    </ClientOnly>
  </div>
  <pre v-else :class="$props.class"><slot /></pre>
</template>

<script setup lang="ts">
import { ref, onMounted, computed } from 'vue'

const props = defineProps({
  code: { type: String, default: '' },
  language: { type: String, default: null },
  filename: { type: String, default: null },
  highlights: { type: Array, default: () => [] },
  meta: { type: String, default: null },
  class: { type: String, default: null },
})

const isMermaid = computed(() => props.language === 'mermaid')
const mermaidEl = ref<HTMLElement | null>(null)

onMounted(async () => {
  if (!isMermaid.value || !mermaidEl.value) return

  const code = props.code?.trim()
  if (!code) return

  const mermaid = (await import('mermaid')).default
  mermaid.initialize({
    startOnLoad: false,
    theme: 'default',
    fontFamily: 'Inter, system-ui, sans-serif',
    securityLevel: 'loose',
  })

  const id = `mermaid-${Math.random().toString(36).slice(2, 9)}`

  try {
    const { svg } = await mermaid.render(id, code)
    mermaidEl.value.innerHTML = svg
  } catch (e) {
    console.error('Mermaid render error:', e)
    mermaidEl.value.innerHTML = `<pre class="p-4 bg-red-50 text-red-600 text-sm rounded-lg">${code}</pre>`
  }
})
</script>
