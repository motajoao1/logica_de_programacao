import os 

def logo_senai():   
    os.system("Cls || clear")
    print("== SENAI ==")
logo_senai()
nome = input("Digite seu nome: ")

logo_senai()
idade = int(input("Digite sua idade: "))

logo_senai()
print(f"Nome: {nome}")
print(f"Idade: {idade}")
