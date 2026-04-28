import funcoes_conversor_moedas as funcoes
def main():
    funcoes.limpar_tela()
    funcoes.exibir_menu()

    opcao = int(input("Escolha uma opção: "))

    if(opcao == 1):
        funcoes.limpar_tela()
        quantia_dolar = float(input("Informe a quantia de dolares: $ "))
        cotacao = float(input("Informe a cotacao: R$ ").replace(",", "."))
        resultado = funcoes.converter_dolar_real(quantia_dolar, cotacao)
        print(f"O total da conversão é : R$ {resultado}")

    elif(opcao == 2):
        funcoes.limpar_tela()
        quantia_real = float(input("Informe a quantia de reais: R$"))
        cotacao = float(input("Informe a cotação: $").replace(",", "."))
        resultado = funcoes.converter_real_dolar(quantia_real, cotacao)
        print(f"O total da converção é: ${resultado:.2f}")
        
    elif(opcao == 3):
        funcoes.sair()

main()