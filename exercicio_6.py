import os
os.system("cls || clear")

def converter_centimetros(numero):
    return metros * 100;

print("= CONVERTER CENTIMETROS PARA METROS = ")
metros = float(input("Digite um número: "))

centimetros = converter_centimetros(metros)

print("\n= RESULTADOS = ")
print(f"{metros} metros é igual a {centimetros} centímetros.")