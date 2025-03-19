import os
os.system("clear")

contador = 0
continua = 's'

while continua =='s':
    # comandos a serem repetidos
    print("Repetindo...")

    contador+=1
    continua=input("Tecle 's' so se deseja continuar: ").strip().lower()

if contador == 0:
    print("O bloco NÃO foi repetido.")
else:
    print("O bloco foi repetido {contador} vezes")