import math


class CrivoEratostenes:
    """Crivo de Eratóstenes: encontra todos os primos menores que n."""

    def crivo_eratostenes(self, n: int) -> dict:
        """Retorna a lista de primos e o passo a passo do crivo."""
        try:
            n = int(n)
            if n < 2:
                return {'primos': [], 'passos': ['Não há primos menores que 2.']}
            if n > 10_000:
                return {'erro': 'Limite máximo: 10000'}

            sieve = [True] * n
            sieve[0] = sieve[1] = False
            limite = math.isqrt(n - 1)
            passos = [
                f'Marque todos os números de 2 a {n - 1} como potencialmente primos.',
                f'Serão testados apenas primos p ≤ √{n - 1} ≈ {limite} (múltiplos de primos maiores já terão sido eliminados).',
            ]

            p = 2
            while p * p < n:
                if sieve[p]:
                    start = p * p
                    mults = list(range(start, n, p))
                    for m in mults:
                        sieve[m] = False
                    passos.append(
                        f'{p} é primo → eliminar múltiplos de {p} a partir de {p}² = {start}: {mults}'
                    )
                p += 1

            primos = [i for i in range(2, n) if sieve[i]]
            passos.append(f'Números não eliminados são primos: {primos}')
            return {'primos': primos, 'passos': passos}
        except Exception as e:
            return {'erro': str(e)}
