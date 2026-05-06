<script setup>
import { ref, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import AppSidebar from '../components/AppSidebar.vue'

const route = useRoute()
const router = useRouter()

const SIDEBAR_KEY = 'sidebar-open'
const sidebarOpen = ref(
  window.innerWidth <= 640 ? false : localStorage.getItem(SIDEBAR_KEY) !== 'false'
)

watch(sidebarOpen, (val) => {
  if (window.innerWidth > 640) localStorage.setItem(SIDEBAR_KEY, String(val))
})

const activeRoute = ref(route.name)
watch(() => route.name, (name) => { activeRoute.value = name })

function handleNavigate(routeName) {
  if (window.innerWidth <= 640) sidebarOpen.value = false
  router.push({ name: routeName })
}
</script>

<template>
  <div class="app-layout" :class="{ 'sidebar-collapsed': !sidebarOpen }">
    <AppSidebar
      :active-route="activeRoute"
      :open="sidebarOpen"
      @update:open="sidebarOpen = $event"
      @navigate="handleNavigate"
    />

    <!-- Mobile backdrop -->
    <div v-show="sidebarOpen" class="mobile-backdrop" @click="sidebarOpen = false" />

    <main class="app-main">
      <header class="app-header">
        <div class="app-header-left">
          <button class="menu-btn" @click="sidebarOpen = !sidebarOpen" aria-label="Menu">
            <span class="material-symbols-outlined">{{ sidebarOpen ? 'close' : 'menu' }}</span>
          </button>
          <h1 class="page-title">{{ route.meta.title ?? '' }}</h1>
        </div>
      </header>

      <div class="app-body">
        <slot />
      </div>
    </main>
  </div>
</template>

<style scoped>
@property --sidebar-w {
  syntax: '<length>';
  initial-value: 196px;
  inherits: false;
}

.app-layout {
  --sidebar-w: 196px;
  display: grid;
  grid-template-columns: var(--sidebar-w) 1fr;
  min-height: 100vh;
  background-color: var(--color-background);
  transition: --sidebar-w 0.22s ease;
}

.app-layout.sidebar-collapsed {
  --sidebar-w: 56px;
}

.app-main {
  min-width: 0;
  display: flex;
  flex-direction: column;
  height: 100vh;
  overflow: hidden;
}

.app-header {
  height: 3.5rem;
  flex-shrink: 0;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 1.5rem;
  border-bottom: 1px solid var(--color-border);
  background-color: var(--color-background);
}

.app-header-left {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.page-title {
  font-size: var(--text-md);
  font-weight: var(--weight-semibold);
  color: var(--color-text);
}

.app-body {
  flex: 1;
  overflow-y: auto;
  min-height: 0;
}

/* ── Hamburger ──────────────────────────────────────────────────────── */
.menu-btn {
  display: none;
  align-items: center;
  justify-content: center;
  width: 2rem;
  height: 2rem;
  border: none;
  border-radius: 6px;
  background: transparent;
  color: var(--color-text);
  cursor: pointer;
  flex-shrink: 0;
  transition: background-color 0.15s;
}

.menu-btn:hover { background-color: var(--color-border); }
.menu-btn .material-symbols-outlined { font-size: 1.25rem; }

/* ── Mobile backdrop ───────────────────────────────────────────────── */
.mobile-backdrop {
  display: none;
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.4);
  z-index: 99;
}

/* ── Mobile (≤640px) ───────────────────────────────────────────────── */
@media (max-width: 640px) {
  .app-layout {
    --sidebar-w: 0px;
    grid-template-columns: 1fr;
  }

  .menu-btn { display: flex; }
  .mobile-backdrop { display: block; }
}
</style>
