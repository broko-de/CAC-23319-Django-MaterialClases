import math


def mcd(n, m):
    """Función que calcula el máximo común divisor de dos números utilizando el algoritmo de eucliedes.
    Parámetros:
        - n: Es un número entero.
        - m: Es un número entero.
    Devuelve:
        El máximo común divisor de n y m.
    """
    dividendo = 0
    while(m > 0):
        dividendo = m
        m = n % m
        n = dividendo
    return n


mcd(7, 21)


def mcd_2(n, m):
    return math.gcd(n, m)
