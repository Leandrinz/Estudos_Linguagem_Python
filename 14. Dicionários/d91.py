import random
import time
import operator 
# Sorteia valores para 4 jogadores
ranking = {'jogador1': random.randint(1,6),
           'jogador2': random.randint(1,6),
           'jogador3': random.randint(1,6),
           'jogador4': random.randint(1,6)}
ordem = {}
# Exibe quanto cada jogador tirou
for k,v in ranking.items():
    print(f'{k} tirou {v}')
    time.sleep(1)
# Coloca em ordem e exibe vencedor
print('-=' * 20)
print('== RANKING DE JOGADORES ==')
ordem = sorted(ranking.items(), key = operator.itemgetter(1), reverse=True)
for k,v in enumerate(ordem):
    print(f'{k + 1}o. lugar: {v[0]} com {v[1]}. ')

    