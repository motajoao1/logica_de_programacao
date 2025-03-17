import os
import time

os.system("cls || clear")

print("MÉDIA")
media = 0
for i in range(3):
    num = int(input(f"Digite a {i+1}° nota: "))
    media += num / 3
        
print()        
print(f"A média é: {media}")

if media >= 7:
    print("Você está aprovado!")
if media >= 4 and media < 6:
    print("Você está na recuperação!")
if media < 4:
    print("Você foi reprovado!")
