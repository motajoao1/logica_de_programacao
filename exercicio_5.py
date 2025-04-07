import os
os.system("cls || clear")

def soma(n1,n2):
    return n1+n2

def subtracao(n1,n2):
    return n1-n2

def multiplicacao(n1,n2):
    return n1*n2

def divisao(n1,n2):
    return n1/n2

print("= NUMEROS =")
n1 = float(input("Digite o primeiro numero: "))
n2 = float(input("Digite o segundo numero: "))

somar = soma(n1,n2)
subtrair = subtracao(n1,n2)
multiplicar = multiplicacao(n1,n2)
dividir = divisao (n1,n2)

print("\n= RESULTADOS =")
print(f"Somar: {soma}")
print(f"subtrair: {subtracao}")
print(f"multiplicar: {multiplicacao}")
print(f"dividir: {divisao}")