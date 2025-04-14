import os
os.system("cls || clear")

#criando uma lista
lista_notas = []
Quantidade_notas = 3

#Adicionando 3 notas em uma lista
for i in range(Quantidade_notas):
    nota = float(input("Digite uma nota: "))
    lista_notas.append(nota)

#media 
media = sum(lista_notas) / Quantidade_notas

#Exibindo todos os valores em uma lista
print()
for nota in lista_notas: # ForEach
    print(nota)

print(f"Média: {media}")