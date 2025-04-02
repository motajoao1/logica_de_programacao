import os 
os.system("Cls || clear")

def logo_senai():   
    os.system("Cls || clear")
    print(" === SENAI DENDEZEIROS ===")

def calcular_soma(primeiro_numero, segundo_numero):   
    soma = primeiro_numero  + segundo_numero
    return soma

logo_senai()
primeiro_numero = int(input("Digite o primeiro número: "))

logo_senai()
segundo_numero = int(input("Digite o segundo número: "))

calcular_soma = calcular_soma(primeiro_numero, segundo_numero)

logo_senai()
print(f"Soma: {calcular_soma}")