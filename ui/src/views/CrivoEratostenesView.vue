<script setup>
import CrivoEratostenes from '../components/calculadoras/CrivoEratostenes.vue'
</script>

<template>
  <div class="view-content">
    <div class="page-header">
      <h1>Crivo de Eratóstenes</h1>
      <p class="subtitle">Encontra todos os primos menores que n.</p>
    </div>
    <CrivoEratostenes />
  </div>
</template>

<style scoped>
.view-content { padding: 2rem; }
.page-header { margin-bottom: 1.75rem; }
.page-header h1 {
  font-size: var(--text-xl);
  font-weight: var(--weight-bold);
  color: var(--color-text);
}
.subtitle {
  margin-top: 0.4rem;
  color: var(--color-subtext);
  font-size: var(--text-sm);
}
</style>
