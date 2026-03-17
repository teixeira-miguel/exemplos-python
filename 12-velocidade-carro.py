import os
os.system("cls")

print("Vamos ver se voce foi acima do limite de velocidade")

velocidade = int(input("Digite a sua velocidade: "))

if velocidade > 80:
    print("Voce foi multado")

else:
    print("Dentro do limite")