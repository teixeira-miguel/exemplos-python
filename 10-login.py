import os
os.system("cls")

nome_de_usuario = input("Digite o nome de usuario: ")

senha = input("Digite a senha: ")

if nome_de_usuario == "admin" and senha == "123":
 print("Acesso liberado")
else:
 print("Acesso negado")