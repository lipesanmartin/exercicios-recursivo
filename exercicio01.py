#  1) Faça uma função recursiva que calcule e retorne o fatorial de um número inteiro N.

def fatorial(n: int) -> int:
    if n == 1 or n == 0:
        return 1
    return n * fatorial(n - 1)


if __name__ == '__main__':
    numero = int(input("Insira um numero inteiro: "))
    print(f"{numero}! = {fatorial(numero)}")
