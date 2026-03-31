import os
import random  

vida_pokemon1 = 100
vida_pokemon2 = 100

os.system("cls")

pokemon_jogador = int(input("Qual Pokémon você escolhe para jogar? (1 ou 2): "))

if pokemon_jogador == 1:
    pokemon_inimigo = 2
else:
    pokemon_inimigo = 1

turno = 1 

while vida_pokemon1 > 0 and vida_pokemon2 > 0:
    os.system("cls")
    print("HP Pokémon 1:", vida_pokemon1, "| HP Pokémon 2:", vida_pokemon2)
   
    # TURNO 1: A sua vez
   
    if turno == 1:
        print("SUA VEZ!")
        acao = int(input("O que você quer fazer? Ataque (1),Cura (2) Fugir (3): "))

        if acao == 1:
            print("Você atacou!")
            if pokemon_jogador == 1:
                vida_pokemon2 = vida_pokemon2 - random.randint(10, 20)
            elif pokemon_jogador == 2:
                vida_pokemon1 = vida_pokemon1 - random.randint(10, 20)
                
        elif acao == 2:
            print("Você usou cura!")
            if pokemon_jogador == 1:
                vida_pokemon1 = vida_pokemon1 + 5
                # Trava 
                if vida_pokemon1 > 100:
                    vida_pokemon1 = 100
            elif pokemon_jogador == 2:
                vida_pokemon2 = vida_pokemon2 + 5
                # Trava 
                if vida_pokemon2 > 100:
                    vida_pokemon2 = 100
        elif acao == 3:
            #  Fuga (50% de chance)
            if random.randint(1, 2) == 1:
                print("Você fugiu da batalha com sucesso!")
                break # Encerra o loop 
            else:
                print("Você tentou fugir, mas falhou!")
        
        # Passa a vez para o computador
        turno = 2 
        input("\nPressione ENTER para continuar...")

    # TURNO 2: vez do pc
   
    elif turno == 2:
        print("VEZ DO INIMIGO...")
        
        #saber se pode curar
        vida_atual_inimigo = vida_pokemon2 if pokemon_inimigo == 2 else vida_pokemon1
        
        if vida_atual_inimigo == 100:
            acao_inimigo = 1
        else:
          
            acao_inimigo = random.choice([1, 3])
            
        if acao_inimigo == 1:
            print("O inimigo atacou você!")
            if pokemon_inimigo == 1:
                vida_pokemon2 = vida_pokemon2 - random.randint(10, 20)
            elif pokemon_inimigo == 2:
                vida_pokemon1 = vida_pokemon1 - random.randint(10, 20)
                
        elif acao_inimigo == 2:
            print("O inimigo usou cura!")
            if pokemon_inimigo == 1:
                vida_pokemon1 = vida_pokemon1 + 5
                if vida_pokemon1 > 100:
                    vida_pokemon1 = 100
            elif pokemon_inimigo == 2:
                vida_pokemon2 = vida_pokemon2 + 5
                if vida_pokemon2 > 100:
                    vida_pokemon2 = 100
        elif acao_inimigo == 3:
            if random.randint(1, 3) == 1:
                print("O inimigo fugiu! A batalha acabou.")
                break
            else:
                print("O inimigo tentou fugir, mas não conseguiu!")

        # Passa a vez de volta 
        turno = 1 
        input("\nPressione ENTER para continuar...")

os.system("cls")
print("--- FIM DE BATALHA ---")
if vida_pokemon1 <= 0:
    print("Pokémon 1 foi derrotado!")
elif vida_pokemon2 <= 0:
    print("Pokémon 2 foi derrotado!")