'''
programa para executar um produto de 2 numeros inteiros positivos utilizando apenas o operador soma (+) 
exemplo: 5 * 7 = 7 + 7 + 7 + 7 + 7

'''

import sys

try:
   
   num1 = int(input('digite quantas vezes voce quer que eu some: '))
   num2 = int(input('digite um numero inteiro positivo: '))
except ValueError:
   sys.exit('ERRO: digite um numero inteiro.')
except Exception as e:
   sys.exit(f'ERRO {e}')

numero_vezes = 0
resultado  = 0

while numero_vezes < num1:
 resultado = resultado + num2
 print(num2, "+")
 numero_vezes = numero_vezes + 1

print('=', resultado)