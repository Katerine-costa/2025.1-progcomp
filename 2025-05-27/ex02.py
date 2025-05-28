'''
programa para executar um produto de 2 numeros inteiros positivos utilizando apenas o operador soma (+) 
exemplo: 5 * 7 = 7 + 7 + 7 + 7 + 7

'''
import sys

try:
    intbase = int(input('digite a base: '))
    intpotencia = int(input('digite a potencia: '))
except ValueError:
    sys.exit('ERRO: não foi informado um valor inteiro válido...')
except Exception as e:
   sys.exit(f'ERRO {e}')
else: 
    if intbase <= 0:
        sys.exit('ERRO: informe base positivo...')

    if intpotencia <= 0:
        sys.exit('ERRO: informe potencia positivo...')

intpotenciacao = 1
intcontador = 1
while intcontador <= intpotencia:
    intpotenciacao *= intbase
    intcontador += 1

print(f'resultado é: ')