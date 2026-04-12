import random
# Sorteia um número de 0 a 5 
ns = random.randint(0,5)

# Pergunta ao usuário qual número ele acha que é
r = int(input('Diga um número de 0 a 5 e veja se acertou: '))

# Verifica se acertou
if r == ns:
    print('Parabéns!!!! Você acertou, o número era: {}'.format(ns))
else:
    print('Você errou. Seu palpite: {}. Número sorteado: {}'.format(r,ns))

print('----------- FIM ------------')