import os 
os.system ("cls || clear")

i = 0
j = 0
k = 0
numero = 0
pares = 0

while True:
    numeros = int(input("Digite um numero: "))

    if numeros % 2 != 0:
        j += 1
    if numeros % 2 == 0:
        k += 1
        pares += numeros
    if numeros == 0:
        break
    numero += numeros
    i += 1

resultado = numero / i
par = pares / k
print(k)
print(j)
print(par)
print(resultado)