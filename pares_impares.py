import os 
os.system("cls || clear")

QUANTIDADE_NUMEROS = 6
lista_numeros = []
pares = 0
impares = 0

#solicitando dados
print("= LISTA DE NÚMEROS =")
for i in range(QUANTIDADE_NUMEROS):
    numero = int(input(f"Digite o {i+1}° número: "))
    lista_numeros.append(numero)

    if numero % 2 == 0:
        pares+=1
    else:
        impares+=1

# Exibindo números da lista.
print("\n= ITENS DA LISTA =")
for i, numero in enumerate(lista_numeros, start=1):
    print(f"{i}: {numero}")

print(f"\nPares: {pares}")
print(f"Ímpares: {impares}")