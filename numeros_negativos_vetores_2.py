import os 
os.system("cls || clear")

QUANTIDADE_NUMEROS = 5
lista_numeros = []

n = 0

print("= LISTA DE NÚMEROS =")
for i in range(QUANTIDADE_NUMEROS):
    numero = int(input(f"Digite o {i+1}° número: "))
    if numero < 0:
        n=0
    lista_numeros.append(numero)

for numero in lista_numeros:
    print(f"Número: {numero}")