import os

strDir = os.path.dirname(__file__)

try:

    arqLeitura = open(f'{strDir}\\carta.txt','r', encoding='utf-8')
except FileNotFoundError:
    print('ERRO: arquivo não encontrado!')
except Exception as erro:
    print(f'ERRo: {erro}!')

else:
    strConteudo = arqLeitura.readline() 
    # read separa por lista 
    # ser for readlines ele transforma em string 
    # read vai exibir somente o primeiro paragrafo.
    arqLeitura.close()
    print(strConteudo)

while True:
    strConteudo = arqLeitura.readline()
    if not strConteudo: break
    print('_' * 80)
    print(strConteudo.strip())
    arqLeitura.close()