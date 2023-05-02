#  4) Faça uma função recursiva que permita somar os elementos de um vetor de inteiros.

def somar_lista(tamanho: int) -> int:
    if tamanho <= 1:
        return lis[0]
    return lis[tamanho - 1] + somar_lista(tamanho - 1)


if __name__ == '__main__':
    lis = [0]
    while True:
        try:
            novo_numero = int(input("Insira um inteiro para adicionar à lista. (0 ou negativo termina): "))
            if novo_numero <= 0:
                break
            else:
                lis.append(novo_numero)
        except ValueError:
            print("Caracter inválido.")
    n = len(lis)
    if n == 0:
        print("Lista vazia")
    else:
        print(somar_lista(n))
