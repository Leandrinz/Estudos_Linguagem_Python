tabela = ('Flamengo', 'Cruzeiro', 'Palmeiras', 'Bahia', 'Botafogo', 'Mirassol', 'São Paulo', 'Bragantino', 'Fluminense', 'Atlético-MG', 'Internacional', 'Ceará SC', 'Corinthians', 'Santos', 'Grêmio', 'EC Vitória', 'Vasco da Gama', 'Fortaleza', 'Juventude', 'Sport Recife')

# 5 primeiros colocados
print('G5: ')
for c in range (0,5):
    print(tabela[c])
print('')

# Os últimos 4 colocados
print('Z4: ')
for z in range (-4, 0):
    print(tabela[z])
print('')
# Ordem alfabética
print('Ordem alfabética: ')
print(sorted(tabela))
print('')
# Posição do Vasco da Gama
print(f'Posição do Vasco da Gama: {tabela.index('Vasco da Gama')}')