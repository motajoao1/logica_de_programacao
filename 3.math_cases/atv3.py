import os
os.system("clear")


opcao = int(input( """
Código \t Prato \t\t Valor
    1 \t Picanha \t\t R$25,00
    2 \t Lasanha \t\t R$20,00
    3 \t Strogonoff \t\t R$18,00
    4 \t Bife Acebolado \t R$25,00
    5 \t Pão com ovo \t\t R$5,00


Digite a opção desejada:
"""))


match opcao:
    case 1:
        print("Picanha - R$25,00")
    case 2:
        print("Lasanha - R$20,00")
    case 3:
        print("Strogonoff - R$18,00")
    case 4:
        print("Bife Acebolado - R$25,00")
    case 5:
        print("Pão com ovo - R$5,00")
    case _:
        print("Opção Inválida!")