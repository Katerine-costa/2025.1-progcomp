'''
Como fazer a tabuada?

- o usuario informa o multiplicador.
5 * 1 = 5
'''
import sys

try:
    intmultiplicador = int(input('digite o multiplicador: '))
    intmultiplicando = int(input('digite o multiplicando: '))
except ValueError:
    sys.exit('ERRO: não foi informado um valor inteiro válido...')
except Exception as e:
   sys.exit(f'ERRO {e}')
else: 
    if intmultiplicador <= 0:
        sys.exit('ERRO: informe multiplicador positivo...')
    if intmultiplicando <= 0:
        sys.exit('ERRO: informe multiplicando positivo...')

intproduto = 0 
