import os
os.system("cls")

print("Bem vindo a sua compra")

produto = (input("Digite o nome do seu produto: "))

quantidade = int(input("Digite a quantidade de profuto adquirido: "))

preco_unitario = float(input("Digite o preço unitario: "))

total = quantidade * preco_unitario

if quantidade <5: 
 desconto = preco_unitario * 0.02

elif quantidade >5 and quantidade <=10: 
 desconto = preco_unitario * 0.03

elif quantidade > 10:
 desconto = preco_unitario * 0.05 

total_a_pagar = total - desconto 
 
print("=" * 25)
print("Resumo da compra")
print("Produto: ",produto)
print("Quantidade: ",quantidade)
print("Total sem desconto: ",total)
print(f"Desconto: {desconto:.2f}")
print("Total a pagar: ",total_a_pagar)
