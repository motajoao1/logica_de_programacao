import os
from dataclasses import dataclass
os.system("cls || clear")

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

@dataclass
class Usuario:
    nome: str
    data_nascimento: str
    rg: str
    cpf: str

    def exibir(self):
        print(f"\nNome: {self.nome}\nData de nascimento: {self.data_nascimento}\nRG: {self.rg}\nCPF: {self.cpf}")

QUANTIDADE = 2
lista = []

for i in range(QUANTIDADE):
    usuario = Usuario(
        nome=input("Digite o nome do usuário: "),
        data_nascimento=input("Digite sua data de nascimento: "),
        rg=input("Informe seu RG: "),
        cpf=input("Informe seu CPF: ")
    )
    lista.append(usuario)
    limpar()

nome_arquivo = "Funcionarios.txt"
with open(nome_arquivo, "a", encoding="utf-8") as arquivo_usuario:
    for usuario in lista:
        arquivo_usuario.write(
            f"\nNome: {usuario.nome}"
            f"\nData de nascimento: {usuario.data_nascimento}"
            f"\nRG do usuário: {usuario.rg}"
            f"\nCPF do usuário: {usuario.cpf}\n"
        )

print("*Dados salvos com sucesso*\nSalvando . . .\n")

try:
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            print(linha.strip())
except FileNotFoundError:
    print("Arquivo não encontrado.")

