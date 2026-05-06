from ..utils.conversao_bases import (
    base_str_to_decimal,
    base_to_decimal_steps,
    decimal_to_base_steps,
    binary_to_hex_steps,
    hex_to_binary_steps,
)


class CalculadoraBases:
    """Conversão entre bases e operações aritméticas em base 2, 10 e 16."""

    # ── Operações binárias bit a bit ──────────────────────────────────

    def _add_binary(self, a: str, b: str) -> str:
        ml = max(len(a), len(b))
        a, b = a.zfill(ml), b.zfill(ml)
        result, carry = [], 0
        for i in range(ml - 1, -1, -1):
            s = int(a[i]) + int(b[i]) + carry
            result.append(str(s % 2))
            carry = s // 2
        if carry:
            result.append('1')
        return ''.join(reversed(result))

    def _sub_binary(self, a: str, b: str) -> tuple[str, bool]:
        """Subtrai b de a em binário. Retorna (resultado, is_negative)."""
        ml = max(len(a), len(b))
        a_p, b_p = a.zfill(ml), b.zfill(ml)
        if a_p < b_p:
            return '', True
        result, borrow = [], 0
        for i in range(ml - 1, -1, -1):
            d = int(a_p[i]) - int(b_p[i]) - borrow
            if d < 0:
                d += 2
                borrow = 1
            else:
                borrow = 0
            result.append(str(d))
        return ''.join(reversed(result)).lstrip('0') or '0', False

    def _mul_binary(self, a: str, b: str) -> str:
        result = '0'
        for i, bit in enumerate(reversed(b)):
            if bit == '1':
                result = self._add_binary(result, a + '0' * i)
        return result

    # ── API pública ───────────────────────────────────────────────────

    def converter_base(self, valor: str, base_origem: int, base_destino: int) -> dict:
        """Converte valor de base_origem para base_destino com passo a passo."""
        try:
            valor = valor.strip().upper()
            base_origem = int(base_origem)
            base_destino = int(base_destino)
            if not valor:
                return {'erro': 'Valor não pode ser vazio'}
            if base_origem == base_destino:
                return {'resultado': valor, 'passos': ['Bases iguais — nenhuma conversão necessária.']}

            # Binário → Hex: agrupamento direto de bits
            if base_origem == 2 and base_destino == 16:
                resultado, passos = binary_to_hex_steps(valor)
                return {'resultado': resultado, 'passos': passos}

            # Hex → Binário: expansão direta por dígito
            if base_origem == 16 and base_destino == 2:
                resultado, passos = hex_to_binary_steps(valor)
                return {'resultado': resultado, 'passos': passos}

            # Demais casos: via decimal intermediário
            passos: list[str] = []
            if base_origem != 10:
                passos.append(f"Passo 1 — {valor} (base {base_origem}) → Decimal")
                decimal_val, sub = base_to_decimal_steps(valor, base_origem)
                passos.extend(sub)
            else:
                decimal_val = int(valor)
                passos.append(f"Valor decimal de entrada: {decimal_val}")

            if base_destino != 10:
                passos.append(f"Passo 2 — {decimal_val} (Decimal) → base {base_destino}")
                resultado, sub = decimal_to_base_steps(decimal_val, base_destino)
                passos.extend(sub)
            else:
                resultado = str(decimal_val)

            return {'resultado': resultado, 'passos': passos}
        except Exception as e:
            return {'erro': f'Erro: {e}'}

    def operar_base(self, valor1: str, valor2: str, base: int, operacao: str) -> dict:
        """Realiza operação aritmética entre dois valores na base dada."""
        try:
            valor1 = valor1.strip().upper()
            valor2 = valor2.strip().upper()
            base = int(base)

            if base == 2:
                if operacao == 'soma':
                    resultado = self._add_binary(valor1, valor2)
                elif operacao == 'subtracao':
                    resultado, neg = self._sub_binary(valor1, valor2)
                    if neg:
                        return {'erro': 'esse tipo de operação não é suportada'}
                elif operacao == 'multiplicacao':
                    resultado = self._mul_binary(valor1, valor2)
                else:
                    return {'erro': 'Operação inválida'}
            else:
                a = base_str_to_decimal(valor1, base)
                b = base_str_to_decimal(valor2, base)
                if operacao == 'soma':
                    res = a + b
                elif operacao == 'subtracao':
                    if a < b:
                        return {'erro': 'esse tipo de operação não é suportada'}
                    res = a - b
                elif operacao == 'multiplicacao':
                    res = a * b
                else:
                    return {'erro': 'Operação inválida'}
                resultado, _ = decimal_to_base_steps(res, base)

            return {'resultado': resultado}
        except Exception as e:
            return {'erro': str(e)}
