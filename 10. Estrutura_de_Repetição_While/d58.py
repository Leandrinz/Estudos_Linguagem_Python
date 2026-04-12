import random
numero_tentativas = 0
# Sorteia o número
pensamento_computador = random.randint(0,10)

# Pergunta ao usuário qual número ele acha que é, em um loop até acertar
chute_jogador = int(input('Chute um número de 0 a 10: '))
while chute_jogador != pensamento_computador:
    numero_tentativas +=1
    print('Eita, você errou, tenta dnv')
    chute_jogador = int(input('Digite outro número: '))

# Exibe qual era o valor e diz quantas tentativas foram
print('Você acertou!!!')
print('O número era {}'.format(pensamento_computador))
print('Número de tentativas: {}'.format(numero_tentativas))