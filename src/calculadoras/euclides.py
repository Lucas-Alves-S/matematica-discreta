class EuclidesEstendido:
    """Algoritmo Estendido de Euclides: calcula mdc(a,b) e coeficientes de Bézout."""

    def euclides_estendido(self, a: int, b: int) -> dict:
        """Retorna mdc, coeficientes s e t, e a sequência de divisões."""
        try:
            a, b = int(a), int(b)
            if a <= 0 or b <= 0:
                return {'erro': 'Insira inteiros positivos'}
            orig_a, orig_b = a, b

            # Sequência de divisões (algoritmo de Euclides)
            equacoes: list[str] = []
            curr_a, curr_b = a, b
            while curr_b != 0:
                q = curr_a // curr_b
                r = curr_a % curr_b
                equacoes.append(f'{curr_a} = {curr_b} × {q} + {r}')
                curr_a, curr_b = curr_b, r
            gcd = curr_a

            # Coeficientes de Bézout via algoritmo estendido
            old_s, s = 1, 0
            old_t, t = 0, 1
            curr_a, curr_b = a, b
            while curr_b != 0:
                q = curr_a // curr_b
                curr_a, curr_b = curr_b, curr_a - q * curr_b
                old_s, s = s, old_s - q * s
                old_t, t = t, old_t - q * t

            s_final, t_final = old_s, old_t
            return {
                'mdc': gcd,
                's': s_final,
                't': t_final,
                'equacoes': equacoes,
                'resultado_final': f'mdc({orig_a},{orig_b}) = {s_final}·{orig_a} + {t_final}·{orig_b}',
            }
        except Exception as e:
            return {'erro': str(e)}
