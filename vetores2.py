import os
os.system("cls || clear")

#criando uma lista
lista_notas = []
Quantidade_notas = 4

#Adicionando 4 notas em uma lista
for i in range(Quantidade_notas):
    nota = float(input("Digite uma nota: "))
    lista_notas.append(nota)

#media 
media = sum(lista_notas) / Quantidade_notas

if media >= 7:
    resultado = "Aprovado"
elif media >= 5:
    resultado = "Recuperação"
else:
    resultado = "Reprovado"

#Exibindo todos os valores em uma lista
print()
for nota in lista_notas: # ForEach
    print(nota)

print(f"Média: {media}")
print(f"Resultado: {resultado}")