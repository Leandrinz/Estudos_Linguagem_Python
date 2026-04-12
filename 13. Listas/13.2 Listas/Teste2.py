#galera = [['João', 19], ['Joaquim', 13], ['Maria', 45]]
#print(galera[2][1])
#for p in galera:
 #   print(f'Nome: {p[0]} / Idade: {p[1]}')

dados = []
galera = []
total_maior = 0
total_menor = 0
for c in range(0,3):
    dados.append(str(input('Digite seu nome: ')))
    dados.append(int(input('Digite sua idade: ')))
    galera.append(dados[:]) # [:] Copia os dados
    dados.clear() # Limpa a lista de dados
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        total_maior += 1
    else:
        print(f'{p[0]} é menor de idade')
        total_menor += 1
print(f'Maiores de idade: {total_maior}')
print(f'Menores de idade: {total_menor}')