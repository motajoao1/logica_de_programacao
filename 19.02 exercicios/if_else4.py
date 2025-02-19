#Elabore um algoritmo para solicitar dois números e ao final mostre na tela: A média, a soma, o produto, o menor valor e o maior valor.
#Usando uma linha para cada resultado.

numero = int(input("Digite um numero: "))
numero2 = int(input("Digite um numero: "))
media = float
soma = int
produto = int

media = (numero + numero2) /2
soma = numero + numero2
produto = numero * numero2

if numero > numero2:
  print("Esta é a média: ", media)
  print("Esta é a soma: ", soma)
  print("Este é o produto: ", produto)
  print("Este é o menor valor: ", numero2)
  print("Este é o menor valor: ", numero)
if numero < numero2:
  print("Esta é a média: ", media)
  print("Esta é a soma: ", soma)
  print("Este é o produto: ", produto)
  print("Este é o menor valor: ", numero)
  print("Este é o menor valor: ", numero2)

