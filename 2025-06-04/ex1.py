'''
   Dados dois números inteiros positivos, determinar o Máximo Divisor 
   Comum (MDC) entre eles usando o Algoritmo de Euclides.
'''

import sys

try:
    num1 = int(input('Digite um numero inteiro positivo: '))
    num2 = int(input('Digite um numero inteiro positivo: '))
except ValueError:
    sys.exit('ERRO: não foi informado um valor inteiro válido...')
except Exception as e:
    sys.exit(f'ERRO {e}')

else:
    if num1 > num2 :
        divisao = num1 // num2
        resto = (num1 % num2) == 0
        print(f'MDC é divisor. ')

    else:
         sys.exit('ERRO: o {num1} e {num2} ')
