import os 
os.system("cls || clear")

QUANTIDADE_NUMEROS = 5

def solicitar_dados():
    lista_numeros = []
    for i in range(QUANTIDADE_NUMEROS):
        numero = int(input(f"Digite o {i+1}° número: "))
        lista_numeros.append(numero)
    return lista_numeros

def verificar_positivos_negativos(lista):
    quantidade_negativos = 0
    soma_positivos = 0
    for numero in lista:
        if numero < 0:
            quantidade_negativos += 1
    else:
        soma_positivos += numero
    return quantidade_negativos, soma_positivos

lista = solicitar_dados()
quantidade_negativos, soma_positivos = verificar_positivos_negativos(lista)

print(f"\nQuantidade de números negativos: {quantidade_negativos}")
print(f"Soma de números positivos: {soma_positivos}")