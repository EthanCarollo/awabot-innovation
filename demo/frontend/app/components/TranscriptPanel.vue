<template>
  <div class="card">
    <div class="card-header">
      <h2>Transcription</h2>
      <button class="btn-icon" @click="$emit('clear')" title="Effacer">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <polyline points="3 6 5 6 21 6"/>
          <path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"/>
        </svg>
      </button>
    </div>
    <div class="transcript-body" ref="bodyEl">
      <p v-if="!text && !active" class="placeholder">La transcription apparaitra ici…</p>
      <p v-else class="transcript-text">
        {{ text }}<span v-if="active" class="cursor" :style="{ color: cursorColor }">|</span>
      </p>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, watch, nextTick } from 'vue'

const props = defineProps<{
  text: string
  active: boolean
  cursorColor?: string
}>()

defineEmits<{
  clear: []
}>()

const bodyEl = ref<HTMLElement | null>(null)

watch(() => props.text, async () => {
  await nextTick()
  if (bodyEl.value) bodyEl.value.scrollTop = bodyEl.value.scrollHeight
})
</script>

<style scoped>
.card {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 24px;
  display: flex;
  flex-direction: column;
  box-shadow: 0 1px 3px rgba(0,0,0,0.04);
}
.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 12px;
}
.card-header h2 {
  font-size: 13px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 1px;
  color: var(--text-muted);
}
.btn-icon {
  background: none;
  border: 1px solid var(--border);
  color: var(--text-muted);
  padding: 8px;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.2s;
}
.btn-icon:hover {
  background: var(--bg);
  color: var(--text);
}
.transcript-body {
  min-height: 180px;
  max-height: 360px;
  overflow-y: auto;
  padding: 16px;
  background: var(--bg);
  border-radius: 12px;
  border: 1px solid var(--border);
}
.placeholder {
  color: var(--text-muted);
  font-style: italic;
  font-size: 14px;
}
.transcript-text {
  font-size: 16px;
  line-height: 1.7;
  white-space: pre-wrap;
  word-break: break-word;
  color: var(--text);
}
.cursor {
  animation: blink 1s infinite;
  font-weight: 700;
}
@keyframes blink { 0%,100%{opacity:1} 50%{opacity:0} }
</style>
