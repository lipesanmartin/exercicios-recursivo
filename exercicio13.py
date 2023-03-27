#  13) Faça uma função recursiva que receba um número inteiro positivo N
#  e imprima todos os números naturais de 0 até N em ordem decrescente.

def ordem_decrescente(n: int) -> int:
    if n <= 0:
        return n
    return ordem_decrescente(n - 1) + 1

lim = int(input("Escolha o limitador: "))
print(f"Numeros de 0 até {lim}:")
for x in range(lim, -1, -1):
    print(ordem_decrescente(x))
