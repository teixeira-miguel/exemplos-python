import os
os.system("cls")

def somar(n1,n2):
    resultado = n1 + n2
    return resultado

def subtrair(n1,n2):
    resultado = n1 - n2
    return resultado

def multiplicar(n1,n2):
    resultado = n1 * n2
    return resultado

def dividir(n1,n2):
    resultado = n1 / n2
    return resultado

def encerrar_programa():
    print("Opção invalida")
    input("Precione ENTER para continuar")
    exit()

print("Bem vindo a calculadora")

n1 = int(input("informe o primeiro numero: "))
n2 = int(input("Informe o segundo numero: "))

print("Escolha uma das opções abaixo")
print(" [1] - Somar\n [2] - Subtrair\n [3] - Multiplicar\n [4] - Dividir")

opcao = int(input("Escolha uma opção: "))

if(opcao == 1):
   os.system("cls")
   print(f"A soma é {somar(n1,n2)}")

elif(opcao == 2):
   os.system("cls")
   print(f"A subtração é {subtrair(n1,n2)}")

elif(opcao == 3):
    os.system("cls")
    print(f"A multiplicação é {multiplicar(n1,n2)}")

elif(opcao == 4):
    os.system("cls")
    print(f"A divisão é {dividir(n1,n2)}")

else:
    os.system("cls")
    encerrar_programa()
    