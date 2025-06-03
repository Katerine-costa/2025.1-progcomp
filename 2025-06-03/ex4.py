import sys

try:
    num = int(input('digite um numero inteiro: '))
    if num <= 0:
        print('este numero nao é primo: ')

except ValueError:
    sys.exit('ERRO: não foi...')
except Exception as e:
   sys.exit(f'ERRO {e}')

'''else:
    divisor = 1
    contador_divisor = 0
    while divisor <= num:
        if (num % divisor) == 0:
            contador_divisor += 1
        divisor += 1'''

for intcontadordiv in range(2, ):

    if intcontadordiv == 2:
        print(f'{num} é primo.')
    else:
        print(f'{num} não é um numero primo. ')