# Matemática Discreta

Desktop app with interactive calculators for discrete mathematics topics. Built with a Python/pywebview backend and a Vue 3 frontend.

## Calculators

- **Calculadora de Bases** — convert numbers between binary, decimal, and hexadecimal, and perform arithmetic (addition, subtraction, multiplication) directly in each base, with a full step-by-step breakdown.
- **Algoritmo de Euclides Estendido** — compute GCD(a, b) and the Bézout coefficients s and t such that `s·a + t·b = gcd(a, b)`, showing the full division sequence.
- **Crivo de Eratóstenes** — find all prime numbers up to n (max 10 000), with each elimination step shown.

## Tech stack

| Layer    | Technology                        |
| -------- | --------------------------------- |
| Desktop  | pywebview + PyQt6 (Qt on Linux)   |
| Backend  | Python 3.13+                      |
| Frontend | Vue 3 + vue-router + Vite         |

## Requirements

- Python 3.13+, managed with [uv](https://github.com/astral-sh/uv)
- Node.js with [pnpm](https://pnpm.io)

## Setup

```bash
# Install Python dependencies
uv sync

# Install frontend dependencies
cd ui && pnpm install
```

## Running

### Production mode

Build the frontend first, then launch the app:

```bash
cd ui && pnpm build && cd ..
uv run main.py
```

### Development mode

Runs Vite's dev server alongside the app (hot reload for the frontend):

```bash
uv run main.py --dev
```
