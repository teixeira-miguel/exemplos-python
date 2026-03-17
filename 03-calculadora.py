import os
os.system ("cls")
print ("Bem vindo a calculadora")

valor1 = float(input("Digite o primeiro numero: "))

valor2 = float(input("Digite o segundo numero: "))

operacao = int(input("Digite a operação que deseja fazer: \n1- soma \n2- subtração \n3- multiplicação \n4- divisão \n")) 

if operacao == 1:
 resultado = valor1 + valor2
 print("\n O resultado da soma é ",resultado)

elif operacao == 2:
 resultado = valor1 - valor2
 print("\n O resultado da sua subtração é: ",resultado)

elif operacao == 3:
 resultado = valor1 * valor2
 print("\n O resultado da sua multiplicação é: ",resultado)

elif operacao == 4:
 resultado = valor1 / valor2
 print("\n O resultado da sua divisão é: ",resultado)