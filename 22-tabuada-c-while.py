import os
os.system("cls")

numero = int(input("Digite um numero: "))

contador = 0

mutiplicador = int(input("Digite quantas vezes voce deseja multiplicar: "))

while(contador <= mutiplicador ):
    print(f"{numero} x {contador} = {numero * contador}")
    contador+=1