import os 
os.system("cls || clear")

QUANTIDADE_NUMEROS = 5
lista_numeros = []

n = 0
soma=0
positivo=0

print("= LISTA DE NÚMEROS =")
for i in range(QUANTIDADE_NUMEROS):
    numero = int(input(f"Digite o {i+1}° número: "))
    lista_numeros.append(numero)

    if numero < 0:
        n+=1
    elif numero % 2 == 0:
        soma += numero

# Exibindo números da lista.
print("\n= ITENS DA LISTA =")
print(f"Negativos: {n}")
print(f"Soma dos positivos: {soma}")
