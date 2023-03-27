#  14) Faça uma função recursiva que receba um número inteiro positivo par N
#  e imprima todos os números pares de 0 até N em ordem crescente.


def pares_crescentes(n: int) -> int:
    if n <= 0:
        return 0
    return 1 + pares_crescentes(n - 1)


while True:
    numero = int(input("Insira um numero par: "))
    if numero % 2 == 0:
        break
    else:
        print("Número inválido, tente novamente.")

print(f"Numeros pares de 0 a {numero}:")
for x in range(0, numero + 1, 2):
    print(pares_crescentes(x))
