<script setup>
import CalculadoraBases from '../components/calculadoras/CalculadoraBases.vue'
</script>

<template>
  <div class="view-content">
    <div class="page-header">
      <h1>Calculadora de Bases</h1>
      <p class="subtitle">Conversão e operações entre bases 2, 10 e 16.</p>
    </div>
    <CalculadoraBases />
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
