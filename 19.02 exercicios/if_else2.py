# Elabore um algoritmo para solicitar ao usuário um valor e escrever a mensagem: “É MAIOR QUE 10!”. 
# Se o valor lido for maior que 10, caso contrário escrever “NÃO É MAIOR QUE 10!”
# Verifique se o número digitado é igual a 10, caso seja, escreva a mensagem: “O número é igual a 10!”

import os
os.system("clear")

# Solicita ao usuário um valor
valor = int(input("Digite um valor: "))

# Verifica se o valor é maior que 10
if valor > 10:
    print("É MAIOR QUE 10!")
if valor == 10:
    print("É IGUAL A 10!")
if valor < 10:
    print("NÃO É MAIOR QUE 10!")