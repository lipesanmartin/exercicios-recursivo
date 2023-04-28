# 12) Faça uma função recursiva que receba um número inteiro positivo N e
#     imprima todos os números naturais de 0 até N em ordem crescente.

def ordem_crescente(n: int) -> int:
    if n <= 0:
        return n
    return 1 + ordem_crescente(n - 1)

if __name__ == '__main__':
    lim = int(input("Escolha o limitador: "))
    print(f"Numeros de 0 até {lim}:")
    for x in range(0, lim + 1):
        print(ordem_crescente(x))
