import os
import time

os.system("cls || clear")

print("CONTAGEM REGRESSIVA")
i = int(input("Digite um número: "))

for i in range(i, 0, -1):
    print(f"Contagem regressiva: {i}")
    time.sleep(1)

print("FIM DO PROGRAMA")