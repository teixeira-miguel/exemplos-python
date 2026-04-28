import os 
os.system("cls")

def escreva():
    print("hello word")

escreva()

def exibir_dados(nome,idade,email):
    print(f"Nome: {nome}")
    print(f"Idade: {idade}") 
    print(f"Email: {email}")
    print("=" * 100) 

exibir_dados("Caio",38,"caio@gmail.com")
exibir_dados("Rebecca",16,"rebeccacurisousa@gmail.com")

def somar(num1,num2):
    resultado = num1 + num2
    return resultado
 
total = somar(10,20)
#ou 
print(f"O total será: {somar(10,20)}")

