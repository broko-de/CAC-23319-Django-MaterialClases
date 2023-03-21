def mcm(n, m):
    """Función que calcula el mínimo común múltiplo de dos números.
    Parámetros:
        - n: Es un número entero.
        - m: Es un número entero.
    Devuelve:
        El mínimo común múltiplo de n y m.
    """
    if n > m:
        mayor = n
    else:
        mayor = m
    while (mayor % n != 0) or (mayor % m != 0):
        mayor += 1
    return mayor
