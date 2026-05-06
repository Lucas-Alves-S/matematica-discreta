import { createRouter, createWebHashHistory } from "vue-router";

const routes = [
  {
    path: "/",
    alias: "/calculadora-bases",
    name: "calculadora-bases",
    component: () => import("../views/CalculadoraBasesView.vue"),
    meta: { title: "Calculadora de Bases" },
  },
  {
    path: "/euclides",
    name: "euclides",
    component: () => import("../views/EuclidesEstendidoView.vue"),
    meta: { title: "Algoritmo de Euclides" },
  },
  {
    path: "/crivo",
    name: "crivo",
    component: () => import("../views/CrivoEratostenesView.vue"),
    meta: { title: "Crivo de Eratóstenes" },
  },
];

export default createRouter({
  history: createWebHashHistory(),
  routes,
});
