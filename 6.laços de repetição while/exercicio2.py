import os
os.system("clear")

q_notas = 2
soma = 0

for i in range(q_notas):
   while True:
    nota = float(input("Digite sua nota: "))
 
    if nota < 0 or nota > 10:
        print("A nota deve ser entre 0 e 10\n")
    else:
        soma += nota
        break

media = soma / q_notas

print(f"Média: {media}")