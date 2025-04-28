import os

from dataclasses import dataclass

os.system("cls || clear")

@dataclass
class Pessoa:
    nome: str
    idade: int
    peso: int
    altura: float

# Atribuindo valores
pessoa1= Pessoa("Guilherme", 17, 61, 1.70)
pessoa2= Pessoa("Jão", 24, 68, 1.78)


print(f"Nome: {pessoa1.nome}, Idade: {pessoa1.idade}, Peso: {pessoa1.peso}, Altura: {pessoa1.altura}")
print(f"Nome: {pessoa2.nome}, Idade: {pessoa2.idade}, Peso: {pessoa2.peso}, Altura: {pessoa2.altura}")

