import os
os.system("clear")


dia = int(input("Digite o dia da semana: " ))


match dia:
    case 1:
        print ("Hoje é Domingo. Final de semana.")
    case 2:
        print ("Hoje é segunda-feira. Dia útil!")
    case 3:  
        print ("Hoje é terca-feira. Dia útil!")
    case 4:
        print ("Hoje é quarta-feira. Dia útil!")
    case 5: 
        print ("Hoje é quinta-feira. Dia útil!")
    case 6:
        print ("Hoje é sexta-feira. Dia útil!")
    case 7:
        print ("Hoje é Sábado. Final de semana.")
    case _:
        print("Opção Inválida!")