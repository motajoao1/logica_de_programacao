import os
os.system("clear")

num = int(input("Digite um número: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

print("Fim do programa!")