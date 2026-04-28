import os
os.system("cls")

def valor_individual(valor_total,total_de_pessoas):
    resultado = valor_total / total_de_pessoas
    return resultado

print("Bem vindo ao divida a sua conta")
valor_total = float(input("Informe o valor da conta:R$"))
total_de_pessoas = int(input("Digite o número de pessoas:"))

resultado = valor_individual(valor_total, total_de_pessoas)

input("Precione ENTER para continuar")

os.system("cls")
print(f"\nTotal da conta:R${valor_total}")
print(f"Total de pessoas:{total_de_pessoas}")
print(f"Valor total por pessoa:R${resultado}")
