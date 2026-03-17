import os
os.system("cls")
print ("Bem vindo ao boletin")

nota1 = float(input("Digite a sua primeira nota: "))

nota2 = float(input("Digite a sua segunda nota: "))

nota3 = float(input("Digite a sua terceira nota: "))

mediafinal = (nota1 + nota2 + nota3) / 3

print ("Sua media final é ", mediafinal)

if (mediafinal >= 7):
   print("Aprovado")
elif(mediafinal>=4 and mediafinal <6):
   print("voce esta de recuperaçao")
else:
   print("Reprovado")
  