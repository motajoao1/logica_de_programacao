import os
os.system("clear")

lista_pratos = []
precos_pratos = []

soma = 0
while True:
    print( """
          Código \t Prato \t\t Valor
          1 \t Picanha \t\t R$25,00
          2 \t Lasanha \t\t R$20,00
          3 \t Strogonoff \t\t R$18,00
          4 \t Bife Acebolado \t R$15,00
          5 \t Pão com ovo \t\t R$5,00
""")
    opcao = int (input("Digite o numero da opção desejada: "))
    
    match opcao:
        case 1:
            prato = "Picanha"
            preco = 25
        case 2:
            prato = "Lasanha"
            preco = 20
        case 3:
            prato = "Strogonoff"
            preco = 18
        case 4:
            prato = "Bife Acebolado"
            preco = 15
        case 5:
            prato = "Pão com ovo"
            preco = 5
            
    soma += preco
    continuar = input("Deseja escolher outro prato? \nDigite 'S' ou 'N': ").lower()
    if continuar == "n":
        break
    os.system("cls || clear")

    lista_pratos.append(prato)
    precos_pratos.append(preco)

    continuar = input("Dseja escolher outro prato? \nResponda com 'S' ou 'N': ").lower()
    if continuar == "n":
        break
    os.system("cls || clear")

print("\n= PRATOS ESCOLHIDOS =")
for prato in lista_pratos:
    print(f"Prato: {prato}")

print(f"\nTotal: {sum(precos_pratos)}")
