import os
os.system("clear")

sexo = str(input("Digite o sexo: " ))
altura = float(input("Digite a altura: "))

match sexo:
    case "m":
       resultado = (72.7 * altura) - 58
       print(f"O peso ideal é: {resultado:.2f}")
    case "f":
       resultado = (62.1 * altura) - 44.7
       print(f"O peso ideal é: {resultado:.2f}") 
    case _:
       print("Opção inválida.")
      
