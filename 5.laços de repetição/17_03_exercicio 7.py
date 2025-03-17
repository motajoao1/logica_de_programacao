import os
import time

os.system("cls || clear")

print("PARES E ÍMPARES")
pares = 0
impares = 0

for i in range(5):
    num = int(input(f"Digite o {i+1}° número: "))
    if num % 2 != 0:
        impares += 1
    if num % 2 == 0:
        pares += 1
        
print()        
print(f"Números pares: {pares}")
print(f"Números ímpares: {impares}")