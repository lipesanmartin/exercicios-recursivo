#  8) O máximo divisor comum dos inteiros x e y é o maior inteiro que é divisível por x e y.
#  Escreva uma função recursiva MDC em Python, que retorna o máximo divisor comum de x e y.
#  O MDC de x e y é definido como segue: se y é igual a 0, então MDC(x,y) é x; caso contrário,
#  MDC(x,y) é MDC (y, x%y), onde % é o operador resto.

def mdc(x, y):
    if y == 0:
        return x
    return mdc(y, x % y)

if __name__ == '__main__':
    numero1 = int(input("Insira o primeiro numero: "))
    numero2 = int(input("Insira o segundo numero: "))

    print(mdc(numero1, numero2))
