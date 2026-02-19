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
  padding: 32px;
  display: flex;
  flex-direction: column;
  margin-bottom: 24px;
}
.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}
.card-header h2 {
  font-size: 11px;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 1px;
  color: var(--text-muted);
}
.btn-icon {
  background: white;
  border: 1px solid var(--border);
  color: var(--text-muted);
  padding: 8px;
  border-radius: 10px;
  cursor: pointer;
  transition: all 0.2s;
  display: flex;
}
.btn-icon:hover {
  background: var(--bg);
  color: var(--carbon);
  border-color: var(--carbon);
}
.transcript-body {
  min-height: 240px;
  max-height: 500px;
  overflow-y: auto;
  padding: 32px;
  background: var(--bg);
  border-radius: 14px;
  border: 1px solid var(--border);
}
.placeholder {
  color: var(--text-muted);
  font-style: italic;
  font-size: 15px;
  text-align: center;
  margin-top: 60px;
  opacity: 0.6;
}
.transcript-text {
  font-size: 18px;
  line-height: 1.8;
  white-space: pre-wrap;
  word-break: break-word;
  color: var(--carbon);
}
.cursor {
  display: inline-block;
  width: 8px;
  height: 20px;
  margin-left: 4px;
  vertical-align: middle;
  animation: blink 1s infinite;
}
@keyframes blink { 0%,100%{opacity:1} 50%{opacity:0} }
</style>
