'''
Faça um programa que solicite um valor inteiro ao usuario e em seguida calcule e exiba o fatorial do numero informado.

n! = n * (n - 1) * (n-2) * (n-3) * ... *  1
'''

import sys

try:
    valor = int(input('digite um numero inteiro: '))

    if valor < 0:
        print('não é fatorial')

    else: 
        numeros = []
        contador = 1

    while contador <= valor:
        numeros = numeros + [contador]
        contador += 1
    fatorial = 1

    for n in numeros:
        fatorial *= n

    print(f'o fatorial do {valor} é {fatorial}. ')

except ValueError:
    sys.exit('ERRO: valor não é inteiro...')