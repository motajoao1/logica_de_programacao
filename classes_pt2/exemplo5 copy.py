import os
from dataclasses import dataclass

os.system("cls || clear")

@dataclass
class Paciente:
    #Atributos: são variáveis que pertencem a classe
    nome: str
    idade: int

    # Método: é uma função que pertence a classe
    # Este método para exibir dados do paciente
    def exibir_dados(self):
        print(f"Nome: {self.nome} \nIdade: {self.idade}\n\n")

#Criando uma lista
lista_de_pacientes = []
QUANTIDADE_PACIENTES = 2

# Atribuindo dados ao paciente1
for i in range(QUANTIDADE_PACIENTES):
    paciente = Paciente(
                nome = input ("Digite seu nome: "),
                idade = int (input ("Digite sua idade: "))
            ) 
    lista_de_pacientes.append(paciente)

#Exibindo dados do paciente
print ("Exibindo dados do usuário: ")
for paciente in lista_de_pacientes:
    paciente.exibir_dados()