import os
os.system("cls")

quantidade_estoque = int(input("Digite a quantidade de produtos em estoque: "))

if quantidade_estoque < 5:
    print("Estoque baixo!")
else:
    print("Estoque OK")