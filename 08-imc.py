import os
os.system("cls")

peso = float(input("Digite o seu peso (em kg): "))

altura = float(input("Digite a sua altura (em metros): "))

imc = peso / (altura * 2)

if imc <= 16.9:
    classificacao = "Muito abaixo do peso"

elif imc <= 18.4:
    classificacao = "Abaixo do peso"

elif imc <= 24.9:
    classificacao = "Peso normal"

elif imc <= 29.9:
    classificacao = "Acima do peso"

elif imc <= 34.9:
    classificacao = "Obesidade grau I"

elif imc <= 40:
    classificacao = "Obesidade grau II"

else:
    classificacao = "Obesidade grau III"

print("\nSeu IMC é: ",imc)

print("Situação: ",classificacao)