import random
# Par ou Ímpar, só para quando o Jogador perder
vitorias_consecutivas = 0
par_impar = 0

while True:
    par_impar = 0
    # Decidindo se quer ímpar ou par
    while par_impar != 1 and par_impar != 2:
        print("""                 1      -      Par
                 2      -      Ímpar """)
        par_impar = int(input('Escolha ímpar ou par: '))
        print('\n')

        # Alerta em caso de Digito inválido
        if par_impar != 1 and par_impar != 2:
            print('Digite apenas 1 ou 2!!!')
            print('\n')
    
    # Condições Gerais
    jogada_computador = random.randint(1,2)
    jogada_jogador = int(input('Digite o número que quer jogar: '))
    resultado = jogada_computador + jogada_jogador
    
    # Condições a partir da escolha Ímpar ou Par

    # PAR
    if par_impar == 1:
        if resultado % 2 == 0:
            vitorias_consecutivas += 1
            print('Você venceu!!!')
            print(f'O resultado foi {resultado}.')
            print('Você escolheu Par!') 
            print('\n')
        else:
            print('Você perdeu!!!')
            print(f'Resultado: {resultado}')
            print('Você escolheu par!')
            print('\n')
            break
    # Ímpar
    else:
        if resultado % 2 != 0:
            vitorias_consecutivas += 1
            print('Você venceu!!!')
            print(f'O resultado foi {resultado}.')
            print('Você escolheu ímpar!')
            print('\n') 
        else:
            print('Você perdeu!!!')
            print(f'Resultado: {resultado}')
            print('Você escolheu ímpar')
            print('\n')
            break

# Exibe quantas vitórias consecutivas o jogador teve
print(f'Vitórias consecutivas: {vitorias_consecutivas}')
        
