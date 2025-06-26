'''
   Fazer um programa que:
   
      1) Solicite ao usuário um valor inteiro N positivo (valor máximo para N -> 100);
   
      2) Gere uma lista com N valores inteiros aleatórios entre 0 e 1.000 (inclusive)
         sem repetições;

      3) A partir da lista gerada, gere uma segunda uma lista com as raízes quadradas 
         dos valores da lista anterior;
'''

import sys, random

try:
    intnum = int(input('informe um valor positvo para N (máximo 100): '))

    if intnum < 0 or intnum > 100:
        print('ERRO: Nota inválida. Informe entre 0 e 100...')

except ValueError:
    sys.exit('/nERRO: informe um valor inteiro válido.../n')
except Exception as erro:
    sys.exit(f'/nERRO: {erro}.../n')
else:
    lista = list()
    
# Gera uma lista com N valores inteiros aleatórios entre 0 e 1000

    for _ in range(intnum):
        lista.append(random.randint(0, 1000))

# Exibe a raiz quadrada dos valores da lista

    raizes = []

    for numero in lista:
        raiz = numero ** 0.5
        raizes.append(raiz)
            
# Exibe o resultado

print('lista')
print(lista)
print('Raízes quadradas dos valores da lista')
print(raizes)