#  3) Faça uma função recursiva que permita inverter um número inteiro N. Ex: 123 – 321

def inverter_inteiro(numero):
    if numero < 10:
        return numero
    ultimo_digito = numero % 10
    resto_do_numero = numero // 10
    numero_invertido = inverter_inteiro(resto_do_numero)
    return int(str(ultimo_digito) + str(numero_invertido))

if __name__ == '__main__':
    print(inverter_inteiro(123456789))
