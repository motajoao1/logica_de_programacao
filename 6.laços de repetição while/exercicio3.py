import os
os.system("clear")

while True:
    login = str(input("Digite login: "))
    senha = int(input("Digite sua senha: "))
 
    if login != 'open' or senha != 1234:
        print("Login e/ou senha incorretos!\n")
    else:
        break

print("Seja bem-vindo!")