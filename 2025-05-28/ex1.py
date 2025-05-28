'''
programa que solicite ao usuario numeros inteiros aleatoriamente ate que seja informado o valor 0

quando for digitado o valor 0, o programa deverá informar:

A) quantos números inteiros foram digitados;
B) a soma dos numeros inteiros positivos;
C) a media dos numeros inteiros positvos;

o valor 0 digitado nao deve ser considerado em nenhum dos itens acima
'''

intvalor = 'nome'
intsomapositivos = 0
intQtValores = 0
intQtValpositivos = 0

import sys

while intvalor != 0:

    try:
        intvalor = int(input('digite um valor inteiros: '))
    except ValueError:
        sys.exit('ERRO: não foi informado um valor inteiro válido...')
    except Exception as e:
        sys.exit(f'ERRO {e}')
    else: 
        if intvalor >  0:
            intsomapositivos += intvalor
            intQtValpositivos += 1
            
        if intvalor != 0:
            intQtValores += 1

print(f'quantos numeros inteiros foram positivos: ')