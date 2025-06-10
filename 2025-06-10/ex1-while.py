'''
   Programa para ao digitar uma palavra ela seja escrita da seguinte forma 
   (como exemplo iremos usar a palavra PROGRAMAÇÃO).

   p
   R
   O
   G
   ...
   O  
'''

strtexto = input('digite uma palavra: ')

'''
for strletra in strtexto:
    print(strletra)
'''

intposicao = 0
while intposicao < len(strtexto):
    print(strtexto [intposicao])
    intposicao += 1