# Cria o dicionário (perfil_jogador)
perfil_jogador = {}
lista = []
total = 0
while True:
    # Adiciona Nome, Quantidade de partidas de vários jogadores
    perfil_jogador['Nome'] = str(input('Nome do Jogador: '))
    numero_partidas = int(input(f'Quantas partidas {perfil_jogador["Nome"]} jogou? '))
    soma_gols = []
    for c in range(0,numero_partidas):
        gols = int(input(f'Gols na partida {c + 1}: '))
        soma_gols.append(gols)
        total = sum(soma_gols)

    # Adiciona campos de gols e total de gols
    perfil_jogador['Gols'] = soma_gols
    perfil_jogador['Total de Gols'] = total

    # Adiciona jogador a Lista:
    lista.append(perfil_jogador.copy())
    resposta = str(input('Quer continuar?[S/N]: ')).upper()
    if resposta == 'N':
        break

# Exibe Nome, gols e total de gols do jogador
print('-=' * 20)
print('cod  nome          gols     total')
print('-----------------------------------------')
for i, p in enumerate(lista):
    
    print(f'{i:<4} {p["Nome"]:<15} {p["Gols"]}    {p["Total de Gols"]}')
    
print('-----------------------------------------')

while True:
    j = int(input('Mostrar Levantamento de qual jogador? (999 sai)'))
    if j == 999:
        break
    if j < 0 or j > len(lista):
        print('Digite um valor válido! ')
    else:   
        # Exibe o levantamento do jogador em escolha
       for i,g in enumerate(lista[j]["Gols"]):
           print(f'Na partida {i+1}, fez {g} gols.')
       print(f'Totalizando {lista[j]["Total de Gols"]} gols.')