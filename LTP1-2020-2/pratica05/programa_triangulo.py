#triangulo
A = int(input('informe o valor do primeiro lado'))
B = int(input('informe o valor do segundo lado'))
C = int(input('informe o valor do terceiro lado'))

if (A>0) and (B>0) and (C>0):
  if (A+B)>C and (B+C)>A and (A+C)>B:
    print('Essas medidas podem formar um triangulo')
else: 
  print('essas medidas nao podem formar um triangulo')
