import os
os.system("cls || clear")

def positivo_negativo(numero):
    if numero < 0:
        ("Número Negativo.")
    else:
        print("Número positivo.")

print("= POSITIVO OU NEGATIVO =")
numero = int(input("Digite um número: "))
positivo_negativo(numero)
