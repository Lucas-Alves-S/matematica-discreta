<script setup>
import EuclidesEstendido from '../components/calculadoras/EuclidesEstendido.vue'
</script>

<template>
  <div class="view-content">
    <div class="page-header">
      <h1>Algoritmo de Euclides</h1>
      <p class="subtitle">Calcula mdc(a, b) e os coeficientes de Bézout.</p>
    </div>
    <EuclidesEstendido />
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
