import os
from dataclasses import dataclass
os.system('cls || clear')

@dataclass
class Autor:
    nome: str
    bibliografia:str

@dataclass
class Livro:
    titulo: str
    ano: int
    autor: Autor

    def exibir_detalhes(self):
        print(f'Título: {self.titulo} \Ano: {self.ano} \nAutor: {self.autor.nome}')

print ("= SOLICITANDO DADOS PARA O USUÁRIO =")

livro = Livro(
    titulo = input ("Digite título do livro: "),
    ano = int(input("Digite o ano da publicação: ")),
    autor = Autor (
        nome=input("Digite o nome do autor: "),
        bibliografia=input ("Digite as informações de bibliografia do autor: ")
    )
)

print ("\n= Salvando Dados = ")