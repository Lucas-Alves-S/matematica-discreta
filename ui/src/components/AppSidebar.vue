<script setup>
import { ref, watch } from 'vue'

const props = defineProps({
  activeRoute: String,
  open: { type: Boolean, default: true },
})

const emit = defineEmits(['navigate', 'update:open'])

const open = ref(props.open)
watch(() => props.open, (val) => { open.value = val })

const navSections = [
  {
    label: 'Exercícios',
    items: [
      { route: 'calculadora-bases', label: 'Calc. de Bases',        icon: 'calculate' },
      { route: 'euclides',          label: 'Algoritmo de Euclides',  icon: 'functions' },
      { route: 'crivo',             label: 'Crivo de Eratóstenes',   icon: 'filter_list' },
    ],
  },
]
</script>

<template>
  <div class="sidebar-wrap">
    <aside class="sidebar" :class="{ collapsed: !open }">

      <!-- Logo -->
      <div class="sidebar-logo">
        <div class="logo-content">
          <div class="logo-icon">
            <span class="material-symbols-outlined">function</span>
          </div>
          <span class="logo-text">Mat. Discreta</span>
        </div>
      </div>

      <!-- Nav -->
      <nav class="sidebar-nav">
        <div v-for="section in navSections" :key="section.label" class="nav-section">
          <div class="nav-section-label-wrap">
            <p class="nav-section-label">{{ section.label }}</p>
          </div>
          <ul class="nav-list">
            <li v-for="item in section.items" :key="item.route">
              <button
                class="nav-item"
                :class="{ active: activeRoute === item.route }"
                :title="!open ? item.label : undefined"
                @click="emit('navigate', item.route)"
              >
                <span class="material-symbols-outlined">{{ item.icon }}</span>
                <span class="nav-label">{{ item.label }}</span>
              </button>
            </li>
          </ul>
        </div>
      </nav>

    </aside>

    <!-- Toggle -->
    <button
      class="sidebar-toggle"
      :title="open ? 'Recolher menu' : 'Expandir menu'"
      @click="open = !open; emit('update:open', open)"
    >
      <span class="material-symbols-outlined">{{ open ? 'chevron_left' : 'chevron_right' }}</span>
    </button>
  </div>
</template>

<style scoped>
.sidebar-wrap {
  position: relative;
  flex-shrink: 0;
  display: flex;
}

.sidebar-toggle {
  position: absolute;
  right: -12px;
  top: 50%;
  transform: translateY(-50%);
  width: 24px;
  height: 24px;
  border-radius: 50%;
  background: var(--color-background-mantle);
  border: 1px solid var(--color-border);
  color: var(--color-subtext);
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 20;
  transition: background-color 0.15s, color 0.15s, border-color 0.15s;
  padding: 0;
}

.sidebar-toggle:hover {
  background: var(--color-primary);
  border-color: var(--color-primary);
  color: #fff;
}

.sidebar-toggle .material-symbols-outlined {
  font-size: 1rem;
}

.sidebar {
  width: 100%;
  height: 100vh;
  background-color: var(--color-background-mantle);
  border-right: 1px solid var(--color-border);
  display: flex;
  flex-direction: column;
  position: sticky;
  top: 0;
  overflow: hidden;
}

/* ── Logo ─────────────────────────────────────────────────────────── */
.sidebar-logo {
  height: 3.5rem;
  display: flex;
  align-items: center;
  padding: 0 0.75rem;
  flex-shrink: 0;
}

.logo-content {
  display: flex;
  align-items: center;
  gap: 0.55rem;
  flex: 1;
  min-width: 0;
  overflow: hidden;
}

.logo-icon {
  width: 1.9rem;
  height: 1.9rem;
  border-radius: 6px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.logo-icon .material-symbols-outlined {
  font-size: 1.5rem;
  color: var(--color-primary);
  font-variation-settings: 'FILL' 1;
}

.logo-text {
  font-size: var(--text-md);
  font-weight: var(--weight-bold);
  color: var(--color-text);
  white-space: nowrap;
  overflow: hidden;
}

/* ── Nav ──────────────────────────────────────────────────────────── */
.sidebar-nav {
  flex: 1;
  padding: 0.8rem 0.4rem;
  display: flex;
  flex-direction: column;
  overflow-y: auto;
  overflow-x: hidden;
}

.nav-section {
  display: flex;
  flex-direction: column;
  margin-top: 0.6rem;
}

.nav-section:first-child {
  margin-top: 0;
}

.nav-section-label-wrap {
  display: grid;
  grid-template-rows: 1fr;
  opacity: 1;
  transition: grid-template-rows 0.22s ease, opacity 0.18s ease;
}

.collapsed .nav-section-label-wrap {
  grid-template-rows: 0fr;
  opacity: 0;
}

.nav-section-label {
  min-height: 0;
  overflow: hidden;
  font-size: var(--text-2xs);
  font-weight: var(--weight-bold);
  letter-spacing: 0.08em;
  color: var(--color-subtext);
  padding: 0.25rem 0.55rem 0.2rem;
  white-space: nowrap;
}

.nav-list {
  list-style: none;
  padding: 0;
  display: flex;
  flex-direction: column;
  gap: 0.15rem;
}

.nav-item {
  display: flex;
  align-items: center;
  gap: 0.55rem;
  width: 100%;
  padding: 0.45rem 0.6rem;
  border-radius: 6px;
  background: none;
  border: none;
  color: var(--color-subtext);
  cursor: pointer;
  font-family: inherit;
  font-size: var(--text-sm);
  font-weight: var(--weight-semibold);
  text-align: left;
  white-space: nowrap;
  transition: background-color 0.15s, color 0.15s;
}

.nav-item .material-symbols-outlined {
  font-size: 1.25rem;
  flex-shrink: 0;
  font-variation-settings: 'FILL' 0, 'wght' 300;
  padding: 0.1rem 0;
}

.nav-label {
  overflow: hidden;
  opacity: 1;
  transition: opacity 0.15s ease;
}

.collapsed .nav-label {
  opacity: 0;
}

.nav-item:hover {
  background-color: var(--color-surface);
  color: var(--color-text);
}

.nav-item.active {
  background-color: var(--color-primary);
  color: #fff;
}

.nav-item.active .material-symbols-outlined {
  font-variation-settings: 'FILL' 1, 'wght' 400;
}

/* ── Mobile (≤640px) ───────────────────────────────────────────────── */
@media (max-width: 640px) {
  .sidebar-wrap {
    position: fixed;
    top: 0;
    left: 0;
    height: 100dvh;
    z-index: 100;
    pointer-events: none;
  }

  .sidebar {
    width: 240px;
    height: 100dvh;
    position: relative;
    pointer-events: auto;
    transform: translateX(-100%);
    transition: transform 0.25s cubic-bezier(0.25, 1, 0.5, 1), box-shadow 0.25s ease;
  }

  .sidebar:not(.collapsed) {
    transform: translateX(0);
    box-shadow: 8px 0 32px rgba(0, 0, 0, 0.2);
  }

  .sidebar-toggle { display: none; }
  .nav-label { opacity: 1; }
  .nav-section-label-wrap { grid-template-rows: 1fr; opacity: 1; }
}
</style>
