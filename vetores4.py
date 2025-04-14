import os
os.system("cls || clear")

#criando uma lista
lista_numero = []
Quantidade_numero = 5

#Adicionando 3 notas em uma lista
for i in range(Quantidade_numero):
    nuumero = int(input("Digite um número: "))
    lista_numero.append(nuumero)

#maior e menor 
maior = max(lista_numero)
menor = min(lista_numero)

for i, nuumero in enumerate(lista_numero, start=1):
    print(f"{i}° número: {nuumero}")
   
print(f"Maior número: {maior} e Menor número: {menor}")