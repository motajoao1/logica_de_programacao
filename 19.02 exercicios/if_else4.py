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
  print(media, soma, produto, numero2, numero)
if numero < numero2:
  print(media, soma, produto, numero, numero2)

