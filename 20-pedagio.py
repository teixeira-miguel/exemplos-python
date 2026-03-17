import os
os.system("cls")

print("Tipos de veículo:")
print("1 - Carro")
print("2 - Moto")
print("3 - Caminhão")

tipo = input("Digite o número correspondente ao tipo de veículo: ")

if tipo == "1":
    print("Valor do pedágio: R$ 10,00")
elif tipo == "2":
    print("Valor do pedágio: R$ 5,00")
elif tipo == "3":
    print("Valor do pedágio: R$ 20,00")
else:
    print("Tipo inválido")