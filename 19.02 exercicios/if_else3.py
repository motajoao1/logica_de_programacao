#Elabore um algoritmo para solicitar ao usuário três notas. 
#Calcule a média do aluno. 
#Caso a média do aluno seja menor que 7, o aluno está reprovado. 
#Mostrar: média e se está aprovado ou reprovado.

valor = int(input("Digite um valor: ")) 
valor2 = int(input("Digite um valor: "))
valor3 = int(input("Digite um valor: "))
media = float

media = (valor + valor2 + valor3) / 3

if media >= 7:
    print(media, "Aprovado")
else:
    print(media, "Reprovado")