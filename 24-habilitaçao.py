import os
os.system("cls")

print("Exemplo de habilitaçao com while ")
 
resposta = "sim"
while resposta == "sim":

    nome = input("Digite o seu nome: ")
    idade = int(input("Digite sua idade: "))

    if idade >= 18: 
        habilitacao = int(input("Possui a habilitação (1- SIM ou 2- NÃO): "))
        
        if habilitacao == 1 :
            print("Voce pode dirigir")
        else: 
            print("Voce não possui habilitação")

    else:
        print("voce é menor de idade")
    
    resposta = input("Voce gostaria de executar novamente? (SIM ou NÃO): ")
    if resposta == "sim":
        os.system("cls")

print("Fim do programa, espero ter ajudado")