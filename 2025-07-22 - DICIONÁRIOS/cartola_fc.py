from logging import exception
import os, sys, json

strDirApp = os.path.dirname(__file__)

strNomeArq = f'{strDirApp}//cartola_fc_2024.json'

try:
    arqinput = open(strNomeArq, 'r', encoding='utf-8')
    strDados = arqinput.read()
    dictCartola = json.loads(strDados)
    arqinput.close()
except FileNotFoundError:
    sys.exit('ERRO: Arquivo não existe...')
except json.JSONDecodeError:
    sys.exit('ERRO: o conteudo do arquivo não esta no formato correto.')
except exception as erro:
    sys.exit(f'ERRO {erro}...')
else:
    lstChaves = list(dictCartola.keys())
    print(lstChaves)
    print(dictCartola{'atletas'})
finally:
    print('\nFIM DO PROGRAMA!')