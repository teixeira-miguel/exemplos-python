import os
os.system("cls")

print("Vamos avaliar seu tempo de estudo: ")

tempo_de_estudo = float(input("Digite seu tempo de estudo: "))

if tempo_de_estudo <= 2:
 print("Pouco estudo")

elif tempo_de_estudo >2 and tempo_de_estudo <4:
 print("Estudo medio")

elif tempo_de_estudo > 4:
 print("Muito estudo")