def ficha(nome = 'Desconhecido', gols = 0):
    if nome == '':
        nome = 'Desconhecido'
    print(f'O jogador {nome} marcou {gols} gol(s) no campeonato!')
    



print('----------')
n = str(input('Digite o nome do Atleta: '))
gol = int(input('Número de gols: '))
ficha(n,gol)
