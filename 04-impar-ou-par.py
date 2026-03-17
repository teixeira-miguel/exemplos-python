import os
os.system("cls")
print("Bem vindo ao impar ou par ")

numero = int(input("Digite seu numero: "))

if numero % 2 == 0:
    print("O numero é par")
else:
    print("O numero é impar")