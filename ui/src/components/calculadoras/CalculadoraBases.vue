<script setup>
import { ref } from 'vue'
import { useApi } from '../../composables/useApi.js'

const { callApi } = useApi()

const activeSubTab = ref('conversao')

// ── Conversão ─────────────────────────────────────────────────────
const convValor      = ref('')
const convBaseOrigem = ref(10)
const convBaseDestino = ref(2)
const convResultado  = ref('')
const convPassos     = ref([])
const convErro       = ref('')
const convLoading    = ref(false)

async function converterBase() {
  convErro.value = ''
  convResultado.value = ''
  convPassos.value = []
  if (!convValor.value.trim()) { convErro.value = 'Informe um valor.'; return }
  convLoading.value = true
  try {
    const res = await callApi('converter_base', convValor.value, convBaseOrigem.value, convBaseDestino.value)
    if (res.erro) convErro.value = res.erro
    else { convResultado.value = res.resultado; convPassos.value = res.passos }
  } catch {
    convErro.value = 'Erro de comunicação com o backend.'
  } finally {
    convLoading.value = false
  }
}

// ── Operações ─────────────────────────────────────────────────────
const opValor1   = ref('')
const opValor2   = ref('')
const opBase     = ref(2)
const opOperacao = ref('soma')
const opResultado = ref('')
const opErro     = ref('')
const opLoading  = ref(false)

async function operarBase() {
  opErro.value = ''
  opResultado.value = ''
  if (!opValor1.value.trim() || !opValor2.value.trim()) {
    opErro.value = 'Informe os dois valores.'
    return
  }
  opLoading.value = true
  try {
    const res = await callApi('operar_base', opValor1.value, opValor2.value, opBase.value, opOperacao.value)
    if (res.erro) opErro.value = res.erro
    else opResultado.value = res.resultado
  } catch {
    opErro.value = 'Erro de comunicação com o backend.'
  } finally {
    opLoading.value = false
  }
}

const opLabel = { soma: '+', subtracao: '−', multiplicacao: '×' }
</script>

<template>
  <div class="calc-container">
    <!-- Sub-tabs -->
    <div class="sub-tabs">
      <button
        :class="activeSubTab === 'conversao' ? '' : 'ghost'"
        @click="activeSubTab = 'conversao'"
      >
        Conversão de Bases
      </button>
      <button
        :class="activeSubTab === 'operacoes' ? '' : 'ghost'"
        @click="activeSubTab = 'operacoes'"
      >
        Operações em Bases
      </button>
    </div>

    <!-- ── CONVERSÃO ── -->
    <div v-if="activeSubTab === 'conversao'">
      <h2 class="calc-section-title">Conversão entre Bases</h2>
      <p class="calc-desc">Converte um valor entre as bases 2, 10 e 16, mostrando o passo a passo.</p>

      <div class="calc-form-row">
        <div class="calc-form-group">
          <label>Valor</label>
          <input
            v-model="convValor"
            class="calc-input"
            placeholder="Ex: 1010, 42, 1F"
            @keyup.enter="converterBase"
          />
        </div>
        <div class="calc-form-group sm">
          <label>Base de origem</label>
          <select v-model="convBaseOrigem" class="calc-select">
            <option :value="2">Binário (base 2)</option>
            <option :value="10">Decimal (base 10)</option>
            <option :value="16">Hexadecimal (base 16)</option>
          </select>
        </div>
        <div class="calc-form-group sm">
          <label>Base de destino</label>
          <select v-model="convBaseDestino" class="calc-select">
            <option :value="2">Binário (base 2)</option>
            <option :value="10">Decimal (base 10)</option>
            <option :value="16">Hexadecimal (base 16)</option>
          </select>
        </div>
        <button :disabled="convLoading" @click="converterBase">
          {{ convLoading ? 'Convertendo…' : 'Converter' }}
        </button>
      </div>

      <div v-if="convErro" class="calc-erro">{{ convErro }}</div>

      <div v-if="convResultado" class="calc-resultado-box">
        <div class="calc-resultado-label">
          Resultado (base {{ convBaseDestino }})
        </div>
        <div class="calc-resultado-valor">{{ convResultado }}</div>
      </div>

      <div v-if="convPassos.length" class="calc-passos-box">
        <div class="calc-passos-title">Passo a passo</div>
        <ol class="calc-passos-list">
          <li v-for="(p, i) in convPassos" :key="i" class="calc-passo">{{ p }}</li>
        </ol>
      </div>
    </div>

    <!-- ── OPERAÇÕES ── -->
    <div v-if="activeSubTab === 'operacoes'">
      <h2 class="calc-section-title">Operações em Bases</h2>
      <p class="calc-desc">
        Soma, subtração ou multiplicação de dois valores na mesma base.
        Subtração com resultado negativo não é suportada.
      </p>

      <div class="calc-form-row">
        <div class="calc-form-group">
          <label>Valor 1</label>
          <input
            v-model="opValor1"
            class="calc-input"
            placeholder="Primeiro operando"
            @keyup.enter="operarBase"
          />
        </div>
        <div class="calc-form-group">
          <label>Valor 2</label>
          <input
            v-model="opValor2"
            class="calc-input"
            placeholder="Segundo operando"
            @keyup.enter="operarBase"
          />
        </div>
        <div class="calc-form-group sm">
          <label>Base</label>
          <select v-model="opBase" class="calc-select">
            <option :value="2">Binário (base 2)</option>
            <option :value="10">Decimal (base 10)</option>
            <option :value="16">Hexadecimal (base 16)</option>
          </select>
        </div>
        <div class="calc-form-group sm">
          <label>Operação</label>
          <select v-model="opOperacao" class="calc-select">
            <option value="soma">Soma (+)</option>
            <option value="subtracao">Subtração (−)</option>
            <option value="multiplicacao">Multiplicação (×)</option>
          </select>
        </div>
        <button :disabled="opLoading" @click="operarBase">
          {{ opLoading ? 'Calculando…' : 'Calcular' }}
        </button>
      </div>

      <div v-if="opErro" class="calc-erro">{{ opErro }}</div>

      <div v-if="opResultado" class="calc-resultado-box">
        <div class="calc-resultado-label">
          {{ opValor1 }} {{ opLabel[opOperacao] }} {{ opValor2 }} (base {{ opBase }})
        </div>
        <div class="calc-resultado-valor">= {{ opResultado }}</div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.sub-tabs {
  display: flex;
  gap: 0.5rem;
  margin-bottom: 1.5rem;
}
</style>
