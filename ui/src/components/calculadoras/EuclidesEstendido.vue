<script setup>
import { ref } from 'vue'
import { useApi } from '../../composables/useApi.js'

const { callApi } = useApi()

const inputA  = ref('')
const inputB  = ref('')
const resultado = ref(null)
const erro    = ref('')
const loading = ref(false)

async function calcular() {
  erro.value = ''
  resultado.value = null
  if (!inputA.value || !inputB.value) {
    erro.value = 'Informe os dois valores.'
    return
  }
  loading.value = true
  try {
    const res = await callApi('euclides_estendido', inputA.value, inputB.value)
    if (res.erro) erro.value = res.erro
    else resultado.value = res
  } catch {
    erro.value = 'Erro de comunicação com o backend.'
  } finally {
    loading.value = false
  }
}
</script>

<template>
  <div class="calc-container">
    <h2 class="calc-section-title">Algoritmo Estendido de Euclides</h2>
    <p class="calc-desc">
      Calcula mdc(a, b) e os coeficientes s e t tais que
      <span class="mono">mdc(a, b) = s·a + t·b</span>.
    </p>

    <div class="calc-form-row">
      <div class="calc-form-group sm">
        <label>a</label>
        <input
          v-model="inputA"
          class="calc-input"
          type="number"
          min="1"
          placeholder="Ex: 48"
          @keyup.enter="calcular"
        />
      </div>
      <div class="calc-form-group sm">
        <label>b</label>
        <input
          v-model="inputB"
          class="calc-input"
          type="number"
          min="1"
          placeholder="Ex: 18"
          @keyup.enter="calcular"
        />
      </div>
      <button :disabled="loading" @click="calcular">
        {{ loading ? 'Calculando…' : 'Calcular' }}
      </button>
    </div>

    <div v-if="erro" class="calc-erro">{{ erro }}</div>

    <template v-if="resultado">
      <div class="calc-passos-box">
        <div class="calc-passos-title">Sequência de divisões</div>
        <ol class="calc-passos-list">
          <li v-for="(eq, i) in resultado.equacoes" :key="i" class="calc-passo">
            {{ eq }}
          </li>
        </ol>
      </div>

      <div class="calc-resultado-box">
        <div class="calc-resultado-label">Resultado final</div>
        <div class="calc-resultado-valor">{{ resultado.resultado_final }}</div>
        <div class="mdc-info">
          mdc = {{ resultado.mdc }} &nbsp;|&nbsp;
          s = {{ resultado.s }} &nbsp;|&nbsp;
          t = {{ resultado.t }}
        </div>
      </div>
    </template>
  </div>
</template>

<style scoped>
.mono {
  font-family: 'Courier New', monospace;
  font-size: var(--text-sm);
  color: var(--color-text);
}

.mdc-info {
  margin-top: 0.5rem;
  font-size: var(--text-sm);
  color: var(--color-subtext);
  font-family: 'Courier New', monospace;
}
</style>
