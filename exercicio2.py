# 2) Faça uma função recursiva que calcule e retorne o N-ésimo termo da sequência
# Fibonacci. Alguns números desta sequência são: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89….

from functools import lru_cache


@lru_cache
def fibonacci_sequence(n: int) -> int:
    """Sequência Fibonacci with memoization"""
    if n < 1:
        return 0
    if n <= 2:
        return 1
    return fibonacci_sequence(n - 1) + fibonacci_sequence(n - 2)


if __name__ == "__main__":
    n = int(input("Insira o limitador da sequencia: "))
    for i in range(n):
        print(fibonacci_sequence(i))
