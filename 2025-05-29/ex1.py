'''
dado que um numero primo é um numero que só possui dois divisores (1 e ele mesmo), faça um programa que solicite ao usuario um numero 
inteiro e informe se ele é primo ou não.
'''

import sys

try:
    num = int(input('digite um numero inteiro: '))
    if num <= 0:
        print('este numero nao é primo: ')

except ValueError:
    sys.exit('ERRO: não foi...')
except Exception as e:
   sys.exit(f'ERRO {e}')

else:
    divisor = 1
    contador_divisor = 0
    while divisor <= num:
        if (num % divisor) == 0:
            contador_divisor += 1
        divisor += 1

    if contador_divisor == 2:
        print(f'{num} é primo.')
    else:
        print(f'{num} não é um numero primo. ')