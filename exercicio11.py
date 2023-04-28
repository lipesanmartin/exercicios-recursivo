#  11) A multiplicação de dois números inteiros pode ser feita através de somas sucessivas.
#  Proponha um algoritmo recursivo Multip_Rec(n1,n2) que calcule a multiplicação de dois inteiros.

def multip_recursiva(n1: int, n2: int) -> int:
    if n2 == 0:
        return 0
    if n2 == 1:
        return n1
    return n1 + multip_recursiva(n1, n2 - 1)


if __name__ == '__main__':
    numero1 = int(input("Insira o primeiro fator: "))
    numero2 = int(input("Insira o segundo fator: "))

    print(f"{numero1} x {numero2} = {multip_recursiva(numero1, numero2)}")
