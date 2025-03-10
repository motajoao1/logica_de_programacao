import os
os.system("clear")

matricula = int(input("Digite a matricula do empregado(código): " ))
idade = int(input("Digite o ano de nascimento: " ))
idd = int
idd = 2025 - idade
tempo_de_trabalho = int(input("Digite o tempo de trabalho: " ))

print(f"O código do empregado é: {matricula}")
print(f"A idade do empregado é: {idd}")
print(f"O tempo de trabalho do empregado é: {tempo_de_trabalho}")

if tempo_de_trabalho >= 30 and idd >= 65:
    print("O empregado requer aposentadoria")
else:
    print("O empregado NÃO requer aposentadoria")
