primeiro_numero = int(input("Digite o primeiro número: "))
segundo_numero = int(input("Digite o segundo número: "))

if primeiro_numero > segundo_numero:
    maior = primeiro_numero
    menor = segundo_numero
else:
    maior = segundo_numero
    menor = primeiro_numero


print()
print(f"Primeiro número: {primeiro_numero}")
print(f"Segundo número: {segundo_numero}")
print(f"Maior numero: {maior}")
print(f"Menor numero: {menor}")