'''
   Dados dois números inteiros positivos, determinar o Máximo Divisor 
   Comum (MDC) entre eles usando o Algoritmo de Euclides.
'''

import sys

try:
    num1 = int(input('Digite o primeiro numero inteiro positivo: '))
    num2 = int(input('Digite o segundo numero inteiro positivo: '))
except ValueError:
    sys.exit('ERRO: não foi informado um valor inteiro válido...')
except Exception as e:
    sys.exit(f'ERRO {e}')

else:
    if num1 < 0:
        sys.exit('ERRO: Digite um número positivo ...')

    if num2 < 0:
        sys.exit('ERRO: Digite um número positivo ...')

# 1000 é um valor grande

for _ in range(1000):
    resto = num1 % num2
    if resto == 0:
        print(f'o MDC é {num2}')
        break  # o break vai interromper o laço assim que encontrar o MDC
    num1, num2 = num2, resto