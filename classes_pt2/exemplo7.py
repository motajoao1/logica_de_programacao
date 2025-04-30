import os
from dataclasses import dataclass

os.system("cls || clear")

@dataclass
class livros:
    #Atributos: são variáveis que pertencem a classe
    nome: str
    autor: str
    categoria: str
    preco: float

    # Método: é uma função que pertence a classe
    # Este método para exibir dados do paciente
    def exibir_dados(self):
        print(f"Nome: {self.nome} \nAutor: {self.autor} \nCategoria: {self.categoria} \nPreço: {self.preco}\n\n")

#Criando uma lista
lista_de_livros = []
QUANTIDADE_LIVROS = 3

# Atribuindo dados dos livros
for i in range(QUANTIDADE_LIVROS):
    livro = livros(
                nome = input ("Digite o nome: "),
                autor = str (input ("Digite o autor: ")),
                categoria = str (input ("Digite a categoria: ")),
                preco = float (input ("Digite o preco: "))
            ) 
    lista_de_livros.append(livro)
    print()

#Salvando em um arquivo .txt
nome_arquivo = "Dados_livro.txt"
with open(nome_arquivo, "a", encoding="utf-8") as arquivos_livros:
    for livro in lista_de_livros:
        arquivos_livros.write(f"{livro.nome},{livro.autor}, {livro.categoria}, {livro.preco} \n")


#Exibindo dados do livros
print ("Exibindo dados do usuário: ")
for livro in lista_de_livros:
    livro.exibir_dados()