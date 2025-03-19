import os
os.system("clear")

for i in range(3):
    login = str(input("Digite login: "))
    senha = int(input("Digite sua senha: "))
        
    if login != 'open' or senha != 1234:
        print("Login e/ou senha incorretos!\n")
    else:
        print("Seja bem-vindo!")
        break