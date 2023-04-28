#  5) Crie uma função recursiva que receba um número inteiro positivo N e calcule o somatório dos números de 1 a N.

def somatorio(n: int) -> int:
    if n < 1:
        return 0
    return n + somatorio(n - 1)

if __name__ == '__main__':
    while True:
        numero = int(input("Insira um numero inteiro positivo: "))
        if numero > 0:
            print(f"Soma dos números de 1 até {numero}: {somatorio(numero)}")
            break
        else:
            print("Número precisa ser positivo")