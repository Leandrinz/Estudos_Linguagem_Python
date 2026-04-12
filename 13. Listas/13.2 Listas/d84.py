# Recebe nome e peso de várias pessoas
lista = []
dados = []
resposta = ''
total_pessoas = 0
pos = 0
while True:
    # Recebe o dado da pessoa x
    dados.append(str(input('Digite seu nome: ')))
    dados.append(float(input('Digite seu peso: ')))
    lista.append(dados[:])
    dados.clear()
         
    # Conta a quantidade de pessoas cadastradas
    total_pessoas += 1

    # Quebra do laço
    resposta = str(input('Quer continuar? [S/N]')).upper()
    if resposta == 'N':
        break


# Adiciona a uma lista dos mais pesados / leves
print(f'Números de pessoas cadastradas: {total_pessoas}')    
lista.sort(reverse=True)
print(f'O maior peso foi de {lista[0][1]}kg. Peso de {lista[0][0]}')
lista.sort()
print(f'O menor peso foi de {lista[0][1]}kg. Peso de {lista[0][0]}')