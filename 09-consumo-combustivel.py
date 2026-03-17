import os
os.system("cls")

print("Calculadora de combustivel")

quilometros_percorridos = float(input("Digite os kilometros percorridos: "))

combustivel_gasto = float(input("Digite quantos litros de combustivel foram gastos: "))

consumo_medio = quilometros_percorridos / combustivel_gasto

print("O consumo medio do seu carro é: ", consumo_medio, "km por litro")
