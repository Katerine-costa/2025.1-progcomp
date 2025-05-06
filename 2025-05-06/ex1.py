# Programa para cálcular movimento retilíneo e solicitar os valores ao usuário
# DADOS: veloc_inicial e 'm/s', aceleração em 'm/s ** 2', tempo em 's'

from os import system
import sys

veloc_inicial = int(input('Digite o valor da velocidade positiva em m/s:'))
if veloc_inicial <=0:
    sys.exit('Informe velocidade positiva')

aceleração = int(input('Digite o valor da aceleração em m/s ** 2: '))
if aceleração <=0:
    sys.exit('Informe aceleraçaõ positiva')

tempo = int(input('Digite o valor do tempo em s: '))
if tempo <=0:
    sys.exit('Informe tempo positivo')

DeltaS = veloc_inicial * tempo + ((aceleração * tempo ** 2) / 2 )

print(f'O valor de deltaS é {DeltaS} em m/s')