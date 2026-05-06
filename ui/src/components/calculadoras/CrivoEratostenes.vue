<script setup>
import { ref } from 'vue'
import { useApi } from '../../composables/useApi.js'

const { callApi } = useApi()

const inputN  = ref('')
const resultado = ref(null)
const erro    = ref('')
const loading = ref(false)

async function calcular() {
  erro.value = ''
  resultado.value = null
  if (!inputN.value) { erro.value = 'Informe o valor de n.'; return }
  loading.value = true
  try {
    const res = await callApi('crivo_eratostenes', inputN.value)
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
    <h2 class="calc-section-title">Crivo de Eratóstenes</h2>
    <p class="calc-desc">
      Encontra todos os números primos menores que <em>n</em> usando o crivo clássico.
      Limite máximo: 10000.
    </p>

    <div class="calc-form-row">
      <div class="calc-form-group sm">
        <label>n</label>
        <input
          v-model="inputN"
          class="calc-input"
          type="number"
          min="2"
          max="10000"
          placeholder="Ex: 50"
          @keyup.enter="calcular"
        />
      </div>
      <button :disabled="loading" @click="calcular">
        {{ loading ? 'Calculando…' : 'Calcular' }}
      </button>
    </div>

    <div v-if="erro" class="calc-erro">{{ erro }}</div>

    <template v-if="resultado">
      <div class="calc-resultado-box">
        <div class="calc-resultado-label">
          Primos encontrados ({{ resultado.primos.length }})
        </div>
        <div class="primos-grid">
          <span v-for="p in resultado.primos" :key="p" class="primo-badge">{{ p }}</span>
        </div>
      </div>

      <div class="calc-passos-box">
        <div class="calc-passos-title">Passo a passo do crivo</div>
        <ol class="calc-passos-list">
          <li v-for="(passo, i) in resultado.passos" :key="i" class="calc-passo">
            {{ passo }}
          </li>
        </ol>
      </div>
    </template>
  </div>
</template>

<style scoped>
.primos-grid {
  display: flex;
  flex-wrap: wrap;
  gap: 0.4rem;
  margin-top: 0.5rem;
}

.primo-badge {
  background: var(--color-primary-soft);
  border: 1px solid var(--color-primary);
  color: var(--color-primary);
  border-radius: 4px;
  padding: 0.15rem 0.5rem;
  font-size: var(--text-sm);
  font-family: 'Courier New', monospace;
  font-weight: var(--weight-semibold);
}
</style>
