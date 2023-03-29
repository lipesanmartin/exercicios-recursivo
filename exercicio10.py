#  10) Escreva uma função recursiva que determine quantas vezes um dígito K ocorre em um número natural N.
#  Por exemplo, o dígito 2 ocorre 3 vezes em 762021192.
from functools import cache


@cache
def contar_caracteres(n, k):
    if n == 0:
        return 0
    ultimo_digito = n % 10
    if ultimo_digito == k:
        return 1 + contar_caracteres(n // 10, k)
    else:
        return contar_caracteres(n // 10, k)


num = int(input("Insira o numero: "))
char = int(input("Insira qual numero quer contar a ocorrencia: "))

print(contar_caracteres(num, char))
