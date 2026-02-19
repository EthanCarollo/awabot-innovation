<template>
  <div class="status-badge" :class="badgeClass">
    <span class="dot" />{{ label }}
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'

const props = defineProps<{
  status: 'idle' | 'connecting' | 'connected' | 'ready' | 'generating' | 'error'
}>()

const badgeClass = computed(() => ({
  'st-idle': props.status === 'idle',
  'st-connecting': props.status === 'connecting',
  'st-ok': props.status === 'connected' || props.status === 'ready',
  'st-generating': props.status === 'generating',
  'st-error': props.status === 'error',
}))

const label = computed(() =>
  ({
    idle: 'Deconnecte',
    connecting: 'Connexion…',
    connected: 'Connecte',
    ready: 'En ecoute',
    generating: 'Generation…',
    error: 'Erreur',
  })[props.status]
)
</script>

<style scoped>
.status-badge {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 12px;
  font-weight: 600;
  padding: 6px 14px;
  border-radius: 100px;
  border: 1px solid var(--border);
}
.dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
}
.st-idle .dot { background: var(--text-muted); }
.st-connecting .dot { background: var(--yellow); animation: pulse 1s infinite; }
.st-ok .dot { background: #22c55e; }
.st-generating .dot { background: var(--yellow); animation: pulse 0.6s infinite; }
.st-error .dot { background: #ef4444; }
@keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.3} }
</style>
