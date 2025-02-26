import os
os.system("clear")


n1 = int(input("Digite um número: "))
operador = input("Digite a operação que deseja (+ - * /): ")
n2 = int(input("Digite um número: "))


match operador:
    case "+":
        resultado = n1 + n2
    case "-":
        resultado = n1 - n2
    case "*":
        resultado = n1 * n2
    case "/":
        resultado = n1 / n2
    case _:
        resultado = "Opção inválida"

print(f"Primeiro número: {n1}")
print(f"Operação: {operador}")
print(f"Segundo número: {n2}")
print(f"Resultado: {resultado}")