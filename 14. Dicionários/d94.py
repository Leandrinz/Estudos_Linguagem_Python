perfil = {}
lista = []
pessoas_cadastradas = 0
soma = 0
# Cria um loop até que o usuário quebre
while True:
    # Recebe Nome, Sexo e Idade e adiciona no dicionário
    perfil['Nome'] = str(input('Nome: '))
    perfil['Sexo'] = str(input('Sexo [M/F]: ')).upper()
    perfil['Idade'] = int(input('Idade: '))

    # Conta total de pessoas cadastradas
    pessoas_cadastradas += 1
    
    # Soma da idade para uma futura média
    soma += perfil['Idade']

    # Adiciona o Perfil da Pessoa x a Lista
    lista.append(perfil.copy())
    
    # Limpa o Perfil em caso de recomeço
    perfil.clear()
    
    # Quebra do laço
    resposta = str(input('Quer continuar? [S/N]: ')).upper()
    if resposta == 'N':
        break

# Faz a média de idade
media = soma / pessoas_cadastradas
print('-=' * 20)

# Exibe Quantas pessoas foram cadastradas, média de idade do grupo, Lista de todas as mulheres, Lista com todos acima da idade média
print(f'Pessoas cadastradas: {pessoas_cadastradas}')

print(f'A média de idade do Grupo foi de {media:.2f}')

print('Mulheres do Grupo:')
for p in lista:
    if p["Sexo"] == 'F':
        print(f'{p["Nome"]}.')

print('Pessoas acima da média de idade: ')
for c in lista:
    if c["Idade"] > media:
        print(f'=> {c["Nome"]} com {c["Idade"]} anos.')
