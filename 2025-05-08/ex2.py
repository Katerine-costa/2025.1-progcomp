'''
   Programa para informar em qual quadrante cartesiano o ponto esta.

   - O programa devera solicitar as duas coordenadas (x,y) de um ponto;

   - O ponto esta no 1º quadrante quando X e Y forem positivos;
   - O ponto esta no 2º quadrante quando X for negativo e Y for positivo;
   - O ponto esta no 3º quadrante quando X e Y forem negativos;
   - O ponto esta no 4º quadrante quando X for positivo e Y for negativo;
'''

# Solicitar as coordenadas do ponto
coordX = float(input('Digite a coordenada X: '))
coordY = float(input('Digite a coordenada Y: '))

# Verificar em qual quadrante o ponto esta
if coordX > 0 and coordY > 0:
   print('O ponto está no 1º quadrante.')
elif coordX < 0 and coordY > 0:
   print('O ponto está no 2º quadrante.')
elif coordX < 0 and coordY < 0:
   print('O ponto está no 3º quadrante.')
elif coordX > 0 and coordY < 0:
   print('O ponto está no 4 quadrante.')
else:
   print('O ponto esta na origem ou nos eixos coordenados.')