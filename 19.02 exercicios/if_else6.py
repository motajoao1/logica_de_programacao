login_cadastrado = "marta"
senha_cadastrada = "123"

login = input("Digite o login: ")
senha = input("Digite a senha: ")

if login == login_cadastrado and senha == senha_cadastrada:
    print("Bem-vindo")
else:
    print("Login ou senha inválidos!")