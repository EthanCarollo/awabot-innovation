<template>
  <div v-if="isMermaid" class="my-8">
    <div ref="mermaidEl" class="flex justify-center overflow-x-auto min-h-[100px]" />
  </div>
  <pre v-else :class="$props.class"><slot /></pre>
</template>

<script setup lang="ts">
import { ref, onMounted, computed, nextTick } from 'vue'

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
  if (!isMermaid.value) return
  
  // Wait for nextTick to satisfy hydration and ensure ref is bound
  await nextTick()
  
  console.log('ProsePre mounted:', { language: props.language, hasCode: !!props.code, codeLength: props.code?.length, hasEl: !!mermaidEl.value })
  
  if (!mermaidEl.value) {
    console.error('ProsePre: mermaidEl is still null after nextTick')
    return
  }

  const code = props.code?.trim()
  if (!code) return

  try {
    const mermaid = (await import('mermaid')).default
    mermaid.initialize({
      startOnLoad: false,
      theme: 'default',
      fontFamily: 'Inter, system-ui, sans-serif',
      securityLevel: 'loose',
    })

    const id = `mermaid-${Math.random().toString(36).slice(2, 9)}`
    const { svg } = await mermaid.render(id, code)
    if (mermaidEl.value) {
      mermaidEl.value.innerHTML = svg
    }
  } catch (e) {
    console.error('ProsePre: Mermaid render error:', e)
    if (mermaidEl.value) {
      mermaidEl.value.innerHTML = `<pre class="p-4 bg-red-50 text-red-600 text-sm rounded-lg">Mermaid Error: ${e instanceof Error ? e.message : String(e)}\n\n${code}</pre>`
    }
  }
})
</script>
