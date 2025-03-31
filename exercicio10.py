import os 
os.system ("cls || clear")

salarios = 0
i = 0
j = 0
maior_idade = 0
menor_idade = 9999

while True:
    print( """
          Código \t Descrição
          1 \t Adicionar pessoa
          2 \t Exibir resultados
          3 \t Sair
    """)
    opcao = int (input("Digite o numero da opção desejada: "))
    match opcao:
        case 1:
            idd = int(input("Digite a idade: "))
            sexo = str(input("Digite o sexo M/F: "))
            salario = int(input("Digite o salário: "))
            salarios += salario
            i += 1
            total = salarios / i
            maior_idade = max(maior_idade, idd)
            menor_idade = min(menor_idade, idd)
            if sexo == 'F' and salario > 5000:
                j += 1
        case 2:
            print(f"A média de salário é: {total}")
            print(f"A menor idade é: {menor_idade} e a maior idade é: {maior_idade}")
            print(f"A quantidade de mulheres com salário maior que R$5K é: {j}")
        case 3:
            print("FIM DO PROGRAMA")
            break
