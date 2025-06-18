'''
fazer um programa que solicite ao usuario nomes de pessoas.

o programa deverá parar de solicitar nomes quando o usuario digitar 'FIM'

no final o programa deverá listar os nomes informados
'''

# cria 
listnomes = list()

while True:
    strnome = input('digite um nome: ').strip()

    if strnome.lower() == 'fim':
        break

    if len(strnome) > 0:
        listnomes.append(strnome)

listnomes.sort()

print(listnomes)