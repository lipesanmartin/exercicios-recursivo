#  Faça uma função recursiva que receba um número inteiro positivo par N
#  e imprima todos os números pares de 0 até N em ordem decrescente.

def pares_decrescentes(n: int) -> int:
    if n <= 0:
        return 0
    return 1 + pares_decrescentes(n - 1)

# print(pares_crescentes(10))

while True:
    numero = int(input("Insira um numero par: "))
    if numero % 2 == 0:
        break
    else:
        print("Número inválido, tente novamente.")

for x in range(numero, -1, -2):
    print(pares_decrescentes(x))
