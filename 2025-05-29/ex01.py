'''
dado que um numero primo é um numero que só possui dois divisores (1 e ele mesmo), faça um programa que solicite ao usuario um numero 
inteiro e informe se ele é primo ou não.
'''

num = int(input('digite um numero inteiro: '))
if num <= 0:
        print('este numero nao é primo: ')

numeros = ()
i = 1
while i <= num:
    numeros += (i,)
    i += 1

divisor = 0

for n in numeros:
    if num % n == 0:
        divisor += 1

if divisor == 2:
    print(f'{num} é primo.')
else:
    print(f'{num} não é primo')