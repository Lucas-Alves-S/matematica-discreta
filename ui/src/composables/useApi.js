/**
 * Composable para chamar a API do PyWebView de forma segura.
 * Aguarda o evento 'pywebviewready' caso a bridge ainda não esteja pronta.
 */
export function useApi() {
  async function callApi(method, ...args) {
    await new Promise((resolve) => {
      if (window.pywebview?.api) return resolve()
      window.addEventListener('pywebviewready', resolve, { once: true })
    })
    return window.pywebview.api[method](...args)
  }

  return { callApi }
}
