import os 
os.system ("cls || clear")

i = 0
notas = 0

while True:
    nota = int(input("Digite uma nota: "))

    if nota < 0:
        break
    notas += nota
    i += 1

resultado = notas / i
print(resultado)