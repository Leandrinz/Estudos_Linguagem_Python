import time
import random
# Palpites Mega Sena
lista = []
print('------------------------')
print('  JOGA NA MEGA SENA')
print('------------------------')
# Recebe quantos jogos o usuário quer fazer
repeticoes = int(input('Quantos jogos você quer que eu sorteie? '))
print(f' -=-=-= SORTEANDO {repeticoes} JOGOS -=-=-=')
for c in range(0,repeticoes):
    # Sorteio de 6 números pra lista x
    lista = random.sample(range(1,61),6) # 6 números únicos de 1 a 60
    lista.sort()
    
    # Exibe o palpite dos jogos
    print(f'Jogo {c + 1}: {lista}')
    lista.clear()
    time.sleep(1)
print('-=-=-=-=-= BOA SORTE -=-=-=-=-=')