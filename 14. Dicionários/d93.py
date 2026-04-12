# Cria o dicionário (perfil_jogador)
perfil_jogador = {}
total = 0

# Adiciona Nome, Quantidade de partidas
perfil_jogador['Nome'] = str(input('Nome do Jogador: '))
numero_partidas = int(input(f'Quantas partidas {perfil_jogador["Nome"]} jogou? '))
soma_gols = []
for c in range(0,numero_partidas):
    gols = int(input(f'Gols na partida {c + 1}: '))
    soma_gols.append(gols)
    total += gols

# Adiciona campos de gols e total de gols
perfil_jogador['Gols'] = soma_gols
perfil_jogador['Total de Gols'] = total

# Exibe Nome, gols e total de gols do jogador
print('-=' * 20)
for k,v in perfil_jogador.items():
    print(f'{k} = {v}')
print('-=' * 20)
print(f'O {perfil_jogador["Nome"]} jogou {numero_partidas} partidas.')

# Exibe os gols específicos nas partidas
for c in range(0,numero_partidas):
    print(f'=> Na partida {c+1}, fez {soma_gols[c]} gols.')
print(f'Totalizando {perfil_jogador["Total de Gols"]} gols.')