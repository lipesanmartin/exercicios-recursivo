# 7) Crie um programa em Python que receba um vetor de números reais com 100 elementos.
#  Escreva uma função recursiva que inverta ordem dos elementos presentes no vetor.

def inverter_vetor(vetor, inicio, fim):
    if inicio < fim:
        vetor[inicio], vetor[fim] = vetor[fim], vetor[inicio]
        inverter_vetor(vetor, inicio + 1, fim - 1)


numeros = [i for i in range(1, 101)]
print("Vetor original:", numeros)
inverter_vetor(numeros, 0, 99)
print("Vetor invertido:", numeros)
