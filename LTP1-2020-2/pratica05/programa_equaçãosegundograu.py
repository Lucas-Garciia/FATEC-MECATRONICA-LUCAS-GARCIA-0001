#EQUAÇAO DE SEGUNDO GRAU
A = int(input('informe o valor de A'))
B = int(input('informe o valor de B')) 
C = int(input('informe o valor de C')) 

Delta = (B*B)-4*A*C
if Delta < 0:
  print ('valor de Delta menor que Zero, nao possui raizes reais')
elif Delta > 0:
 x1 = (-B + Delta**0.5)/(2*A)
   x2 = (-B - Delta**0.5)/(2*A)
   print('Raizes:', x1, x2 )
 else:
   x2 = (-B - Delta**0.5)/(2*A)
   print ('Raiz', x2)
