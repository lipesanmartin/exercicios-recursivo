#  1) Faça uma função recursiva que calcule e retorne o fatorial de um número inteiro N.

def fatorial(n: int) -> int:
    if n == 1 or n == 0:
        return 1
    return n * fatorial(n - 1)

if __name__ == '__main__':
    for x in range(1, 6):
        fatorial = x * (x + 1)
    print(fatorial)

    x = [1, 2, 3]
    y = x
    x.append(4)
    print(y)
