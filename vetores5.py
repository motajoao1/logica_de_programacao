import os
os.system("cls || clear")

#criando uma lista
lista_numero = []
Quantidade_numero = 6

def pares_impares(lista):
    pares = 0
    impares = 0
    for numero in lista:
        if numero % 2 ==0:
            pares +=1
        else:
            impares += 1
    return pares, impares

print("= SOLICITANDO NÚMEROS =")
for i in range(Quantidade_numero):
    numero = int(input(f"Digite o {i+1}° número: "))
    lista_numero.append(numero)

pares, impares= pares_impares(lista_numero)