import os
import time

os.system("cls || clear")

print("CONTAGEM REGRESSIVA")

for i in range(1, 20):
    if i % 2 != 0:
        print(f"Números ímpares: {i}")
        time.sleep(1)

print("FIM DO PROGRAMA")