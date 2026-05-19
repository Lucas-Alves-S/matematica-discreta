"""Funções utilitárias de conversão de bases, compartilhadas entre calculadoras."""


def hex_char_to_decimal(c: str) -> int:
    c = c.upper()
    if '0' <= c <= '9':
        return int(c)
    return ord(c) - ord('A') + 10


def decimal_to_hex_char(n: int) -> str:
    if n < 10:
        return str(n)
    return chr(ord('A') + n - 10)


def base_str_to_decimal(valor: str, base: int) -> int:
    """Converte string em dada base para int decimal, manualmente."""
    result = 0
    for c in valor.upper():
        d = hex_char_to_decimal(c) if base == 16 else int(c)
        result = result * base + d
    return result


def base_to_decimal_steps(valor: str, base: int) -> tuple[int, list[str]]:
    """Converte string para decimal com expansão posicional. Retorna (valor, passos)."""
    valor = valor.upper().strip()
    length = len(valor)
    parts = []
    result = 0
    for i, c in enumerate(valor):          # MSB first (left to right)
        power = length - 1 - i
        d = hex_char_to_decimal(c) if base == 16 else int(c)
        contrib = d * (base ** power)
        result += contrib
        parts.append(f"  {c} × {base}^{power} = {d} × {base ** power} = {contrib}")
    return result, parts + [f"Soma = {result}"]


def decimal_to_base_steps(n: int, base: int) -> tuple[str, list[str]]:
    """Converte decimal para base alvo via divisões sucessivas. Retorna (resultado, passos)."""
    if n == 0:
        return '0', [f"  0 ÷ {base} = 0  (resto 0)"]
    steps: list[str] = []
    remainders: list[str] = []
    current = n
    while current > 0:
        q = current // base
        r = current % base
        rem_str = decimal_to_hex_char(r) if base == 16 else str(r)
        steps.append(f"  {current} ÷ {base} = {q}  (resto {rem_str})")
        remainders.append(rem_str)
        current = q
    result = ''.join(reversed(remainders))
    steps.append(f"Restos de baixo para cima: {result}")
    return result, steps


def binary_to_hex_steps(valor: str) -> tuple[str, list[str]]:
    """Binário → Hex agrupando 4 bits por vez. Retorna (resultado, passos)."""
    steps: list[str] = []
    pad_len = (4 - len(valor) % 4) % 4
    padded = '0' * pad_len + valor
    if pad_len:
        steps.append(f"Preenchendo com zeros à esquerda: {padded}")
    steps.append("Agrupando em blocos de 4 bits:")
    result = ''
    for i in range(0, len(padded), 4):
        group = padded[i:i + 4]
        d = sum(int(b) * (2 ** (3 - j)) for j, b in enumerate(group))
        h = decimal_to_hex_char(d)
        steps.append(f"  {group} = {d} → {h}")
        result += h
    steps.append(f"Resultado: {result}")
    return result, steps


def hex_to_binary_steps(valor: str) -> tuple[str, list[str]]:
    """Hex → Binário convertendo cada dígito em 4 bits. Retorna (resultado, passos)."""
    valor = valor.upper()
    steps = ["Convertendo cada dígito hex em 4 bits:"]
    raw = ''
    for c in valor:
        d = hex_char_to_decimal(c)
        bits = ''
        temp = d
        for _ in range(4):
            bits = str(temp % 2) + bits
            temp //= 2
        steps.append(f"  {c} = {d} → {bits}")
        raw += bits
    stripped = raw.lstrip('0') or '0'
    if stripped != raw:
        steps.append(f"Removendo zeros à esquerda: {stripped}")
    steps.append(f"Resultado: {stripped}")
    return stripped, steps
