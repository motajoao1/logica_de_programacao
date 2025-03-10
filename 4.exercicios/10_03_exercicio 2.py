import os
os.system("clear")

nome_aluno = str(input("Digite o nome do aluno: " ))
nota1 = float(input("Digite a primeira nota: " ))
nota2 = float(input("Digite a segunda nota: " ))
média = float
média = (nota1 + nota2)/2

if média >= 9:
    print("A, Aprovado")
if média >= 7.5 and média < 9:
    print("B, Aprovado")
if média >= 6 and média < 7.5:
    print("C, Aprovado")
if média >= 4 and média < 6:
    print("D, Reprovado")
if média < 4:
    print("E, Reprovado")
