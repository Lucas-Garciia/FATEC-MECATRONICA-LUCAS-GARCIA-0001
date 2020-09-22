#CALCULADORA
operacao = input('informe a operacao desejada')

if operacao == '+':
  valor01 = float(input('valor 1:'))
  valor02 = float(input('valor 2:'))
  resultado = valor01 + valor02
  print(resultado)
elif operacao == '-':
  valor01 = float(input('valor 1:'))
  valor02 = float(input('valor 2:'))
  resultado = valor01 - valor02
  print(resultado)
elif operacao == '*':
  valor01 = float(input('valor 1:'))
  valor02 = float(input('valor 2:'))
  resultado = valor01 * valor02
  print(resultado)
elif operacao == '/':
  valor01 = float(input('valor 1:'))
  valor02 = float(input('valor 2:'))
  if valor02 == 0:
    print('Tentativa de divisão por Zero')
  else:
    resultado = valor01 / valor02
    print (resultado)
else:
  print('operação invalida')
