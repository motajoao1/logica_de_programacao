import os

from dataclasses import dataclass

os.system("cls || clear")

@dataclass
class Pessoa:
    nome: str
    email: str
    telefone: int
    endereço: str

    def exibindo_dados(self):
        print("Exibindo dados: ")
        print(f"Nome: {self.nome}, Email: {self.email}, Telefone: {self.telefone}, Endereço: {self.endereço}")

# Solicitando Dados
print("Solicitando dados")
nome = input("Digite seu nome: ")
email = input("Digite seu email: ")
telefone = input("Digite seu telefone: ")
endereço = input("Digite seu endereço: ")

pessoa1 = Pessoa(nome, email, telefone, endereço)
pessoa1.exibindo_dados()

