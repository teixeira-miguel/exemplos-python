import os
os.system("cls")

saldo = 1000

while True:

    os.system("cls")

    print("Bem vindo a sua conta")
    print("\nO que deseja fazer")
    print("\n 1- Saque \n 2- Deposito \n 3- Consultar saldo \n 4- Sair ")

    escolha = int(input("Qual a sua escolha: "))

    if escolha == 1:
        saque = int(input("Quanto deseja sacar? R$"))
        
        if saque <= saldo or saque == saldo:
            saldo -= saque
            print("Saque realizado")
        else:
            print("Saldo insuficiente")
    elif escolha == 2:
        deposito = int(input("Quanto deseja depositar? R$ "))
        saldo += deposito  
        print("Depósito realizado!")

    elif escolha == 3:
        print(f"Seu saldo atual é: R$ {saldo}")

    elif escolha == 4:
        print("Saindo... Volte sempre!")
        break 

    else:
        print("Opção inválida!")


    input("\nPressione ENTER para continuar...")