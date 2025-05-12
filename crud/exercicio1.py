import os
import time

os.system("cls || clear")

# Função para adicionar.
def adicionar_nome(lista_nomes):
    nome = str (input("Digite o nome que deseja adicionar: "))
    lista_nomes.append(nome)
    print(f"\n{nome} adicionado com sucesso.")


# Função para add nascimento.
def adicionar_data_de_nascimento(lista_nasc):
    nasc = float (input ("Digite a data de nascimento: "))
    lista_nasc.append(nasc)
    print(f"\n{nasc} adicionado com sucesso.")


# Função para add cpf.
def adicionar_cpf(lista_cpf):
    cpf = int (input("Digite seu cpf: "))
    lista_cpf.append(cpf)
    print(f"\n{cpf} adicionado com sucesso.")
    


# Função para add func.
def adicionar_funcao(lista_func):
    func = input("Digite sua função: ")
    lista_func.append(func)
    print(f"\n{func} adicionado com sucesso.")


# Criando listas.
nomes = []
nasc = []
cpf = []
func = []

# Mostrando menu.
while True:
    print("""
    - Informações -
    1 - Nome
    2 - Data de Nascimento
    3 - CPF
    4 - Função
    5 - Sair
    """)
    opcao = int(input("Digite uma das opções acima: "))

    match opcao:
        case 1:
            adicionar_nome(nomes)
        case 2:
            adicionar_data_de_nascimento(nasc)
        case 3:
            adicionar_cpf(cpf)
        case 4:
            adicionar_funcao(func)
        case 5:
            print("\nSaindo do programa.")
            break
        case _:
            print("\nOpção inválida.\nTente novamente.")
    if opcao != 1:
        time.sleep(3)
    os.system("cls || clear")