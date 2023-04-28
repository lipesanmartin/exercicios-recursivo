#  16) A função fatorial duplo é definida como o produto de todos os números naturais ímpares de 1 até algum
#  número natural ímpar N. Assim, o fatorial duplo de 5 é 5!! = 1 * 3 * 5 = 15 Faça uma função recursiva que receba
#  um número inteiro positivo ímpar N e retorne o fatorial duplo desse número.


def fatorial_duplo(n: int) -> int:
    if n <= 1:
        return 1
    return n * fatorial_duplo(n - 2)


if __name__ == '__main__':
    while True:
        num = int(input("Insira um número impar positivo: "))
        if num % 2 == 0 or num < 1:
            print("Número inválido:")
        else:
            print(fatorial_duplo(num))
            break

