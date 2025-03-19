import os
os.system("clear")

while True:
    nota = float(input("Digite sua nota: "))
    
    if nota < 0 or nota > 10:
        print("A nota deve ser entre 0 e 10\n")
    else:
        break

print(f"Nota: {nota}")