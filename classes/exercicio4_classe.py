import os

from dataclasses import dataclass

os.system("cls || clear")

@dataclass
class Endereco:
    logradouro: str
    numero: str
    cidade: str

@dataclass
class Pessoa:
    nome: str
    idade: int
    endereco: Endereco # Classe endereço.

    #Método da classe (função que pertence a uma classe).
    def exibindo_dados(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}, Logradouro: {self.endereco.logradouro}, Número: {self.endereco.numero}, Cidade: {self.endereco.cidade}")

# Solicitando Dados
print("Solicitando dados")
nome = input("Digite seu nome: ")
email = input("Digite seu email: ")
número = input("Digite o número da sua residência: ")
logradouro = input("Digite seu endereço: ")
cidade = input("Digite o nome da cidade: ")

endereco1 = Endereco(logradouro, número, cidade)
pessoa1 = Pessoa(nome, email, endereco1)


print("Dados das pessoas: ")
pessoa1.exibindo_dados()

