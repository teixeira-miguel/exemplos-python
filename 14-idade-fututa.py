import os
os.system("cls")

idade_atual = int(input("Digite sua idade atual: "))
ano_atual = int(input("Digite o ano atual: "))

idade_2035 = idade_atual + (2035 - ano_atual)

print(f"No ano de 2035 você terá {idade_2035} anos.")