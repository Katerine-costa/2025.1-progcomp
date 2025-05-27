'''
Como fazer a tabuada?

- o usuario informa o multiplicador.
5 * 1 = 5
'''
import sys

num = int(input('digite um numero de 1 a 10: '))
if num <= 10:
    print('ERRO: numero invalido. Informe um numero de 1 a 10.')

n1 = num * 1
n2 = num * 2
n3 = num * 3 
n4 = num * 4
n5 = num * 5
n6 = num * 6
n7 = num * 7
n8 = num * 8
n9 = num * 9
n10 = num * 10

print(f'multiplicação do {num} é: ',n1)
print(f'multiplicação do {num} é: ',n2)
print(f'multiplicação do {num} é: ',n3)
print(f'multiplicação do {num} é: ',n4)
print(f'multiplicação do {num} é: ',n5)
print(f'multiplicação do {num} é: ',n6)
print(f'multiplicação do {num} é: ',n7)
print(f'multiplicação do {num} é: ',n8)
print(f'multiplicação do {num} é: ',n9)
print(f'multiplicação do {num} é: ',n10)