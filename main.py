import pytest


def imprimir_oi(nome):
    print(f'Oi, {nome}')


def somar(numero_a, numero_b):
    return numero_a + numero_b

def dividir(numero_a, numero_b):
    try:
        return numero_a / numero_b
    except ZeroDivisionError:
        return 'Não dividiras por zero'

def subtrair(numero_a, numero_b):
    return numero_a - numero_b

def multiplicar(numero_a, numero_b):
    return numero_a * numero_b


if __name__ == '__main__':
    imprimir_oi('Luciana')

    # Chamar a definição somar e mostrar o resultado
    resultado = somar(7, -6)
    print(f'A soma: {resultado}')

    # Chamar a definição subtrair e mostrar o resultado
    resultado = subtrair(25, 8)
    print(f'A subtração: {resultado}')

