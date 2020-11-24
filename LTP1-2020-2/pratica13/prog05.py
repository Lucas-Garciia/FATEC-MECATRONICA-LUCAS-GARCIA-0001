menor_preco = float("inf")
melhor_loja = ""

continuar = True

while continuar == True:
  preco = float(input("preço:"))
  loja = input("loja:")
  if preco < menor_preco:
    menor_preco = preco
    melhor_loja = loja
  continuar = input("deserja continuar?").lower()== "s"

print("melhor loja: %s com o preço R$%.2f"%(melhor_loja, menor_preco))
