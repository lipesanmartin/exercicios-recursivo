#  6) Crie um programa em Python, que contenha uma função recursiva que receba dois inteiros positivos k e n e
#  calcule k^n. Utilize apenas multiplicações. O programa principal deve solicitar ao usuário os valores de k e n
#  e imprimir o resultado da chamada da função.

def potenciacao(k: int, n: int) -> int:
    if n == 0:
        return 1
    if n == 1:
        return k
    return k * potenciacao(k, n - 1)


numero = int(input("Insira um numero inteiro: "))
potencia = int(input(f"Insira a potencia que gostaria de elevar {numero}: "))

print(f"{numero} elevado a {potencia} é {potenciacao(numero, potencia)}.")
