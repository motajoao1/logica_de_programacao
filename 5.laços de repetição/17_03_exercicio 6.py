import os
import time

os.system("cls || clear")

print("SOMANDO NÚMEROS")
soma = 0

for i in range(5):
    num = int(input(f"Digite o {i+1}° número: "))
    soma += num

print()
print(f"Soma total: {soma}")