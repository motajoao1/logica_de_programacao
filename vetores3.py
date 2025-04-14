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
def medias (media):
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"

media = sum(lista_notas) / Quantidade_notas
resultado = medias (media)

#Exibindo todos os valores em uma lista
print()
for nota in lista_notas: # ForEach
    print(nota)

print(f"Média: {media}")
print(f"Resultado: {resultado}")