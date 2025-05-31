'''
Faça um programa que solicite um valor inteiro ao usuario e em seguida calcule e exiba o fatorial do numero informado.

n! = n * (n - 1) * (n-2) * (n-3) * ... *  1
'''

import sys

try: 
    valor = int(input('digite um numero inteiro: '))

except ValueError:
    sys.exit('ERRO: valor não é inteiro...')
except Exception as e:
   sys.exit(f'ERRO {e}')

else:
    if valor <= 0:
        print('não é fatorial')

    elif valor <= 2:
        print(f'{valor}! = 1')

    else:
        fatorial = valor
        intAux = valor
        while intAux >=2:
            intAux -= 1
            fatorial *= intAux

        print(f'{valor}! = {fatorial}')