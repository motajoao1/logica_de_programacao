import os
from dataclasses import dataclass
os.system('cls || clear')

def limpar():
    os.system("cls || clear")

@dataclass
class Usuario:
    nome: str
    data_nascimento: float
    rg: float
    cpf: float

    def exibir(self):
        print(f"\nNome: {self.nome} \nAutor:{self.data_nascimento} \nCategoria: {self.rg} \nPreço:{self.cpf} ")

Quantidade = 5
lista_livros = []

for i in range(Quantidade):
    Usuario = Usuario(
        nome=input("Digite o nome do usuário: "),
        data_nascimento=input("Digite seu nascimento: ")
        rg=input("Informe seu rg: ")
        cpf=input("Informe seu cpf: ")
    )
    limpar()

lista_livros.append(livros)

nome_arquivo = "olê.txt"
with open (nome_arquivo, "a", encoding="utf-8") as arquivo_livro:
    for livro in lista_livros:
        arquivo_livro.write(f"\nTítulo do livro: {livro.titulo}\Ano de publicação: {livro.ano}\Nome do autor: {livro.autor.nome} \Biografia do autor: {livro.autor.biografia}")
print(f"\t\nSalvando...")

try:
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            print(f"{linha.strip()}")
except FileNotFoundError:
    print("Arquivo não encontrado")


print ("\n= Dados Salvos = ")