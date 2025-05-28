'''
programa para executar uma potenciação de 2 numeros inteiros utilizando apenas o operador produto (*)
'''

import sys

try:
    num1 = int(input('digite quantas vezes o programa deve multiplicar: '))
    num2 = int(input('digite um numero inteiro positivo: '))
except ValueError:
    sys.exit('ERRO: digite um numero inteiro..')
except Exception as e:
   sys.exit(f'ERRO {e}')

base = 0
resultado = 0

while base < num2:
    resultado = resultado * num1
    print(num2, '*')
    resultado = resultado * 1

print('=', resultado)