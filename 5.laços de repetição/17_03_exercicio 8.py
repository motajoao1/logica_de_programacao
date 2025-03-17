import os
import time

os.system("cls || clear")

print("MÉDIA")
media = 0
for i in range(4):
    num = int(input(f"Digite o {i+1}° número: "))
    media += num / 4
        
print()        
print(f"A média é: {media}")
