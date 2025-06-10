'''
   Programa para ao digitar uma palavra ela seja escrita da seguinte forma 
   (como exemplo iremos usar a palavra PROGRAMAÇÃO).

   p
   PR
   PRO
   PROG
   ...
   PROGRAMAÇÃO  
'''

strtexto = input('digite uma palavra: ')

iposicao = 0
while iposicao < len(strtexto):
    print(strtexto[0:iposicao + 1])
    iposicao += 1