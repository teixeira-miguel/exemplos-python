import os
os.system("cls")

nivel = int(input("Digite o nível do professor (1, 2 ou 3): "))

aulas_semana = int(input("Digite a quantidade de aulas lecionadas por semana: "))

if nivel == 1:
    valor_hora = 12.00

elif nivel == 2:
    valor_hora = 17.00

elif nivel == 3:
    valor_hora = 25.00
    
else:
    valor_hora = 0.00
    print("Nível inválido.")

salario_final = aulas_semana * valor_hora

print(f"Salário final do professor: R$ {salario_final:.2f}")