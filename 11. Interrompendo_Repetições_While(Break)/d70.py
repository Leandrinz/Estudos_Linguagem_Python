
nome = str(input('Digite o nome do produto: '))
preco = float(input(f'Digite o preço do {nome} : '))
preco_barato = preco
barato = nome
produtos_1000_reais = 0
soma = 0
while True:
    if preco > 1000:
        produtos_1000_reais += 1
    soma += preco
    decisao = str(input('Quer continuar? (S/N)')).upper()
    if decisao == 'N':
        break
    nome = str(input('Digite o nome do produto: '))
    preco = float(input(f'Digite o preço do {nome} : '))
    if preco < preco_barato:
        preco_barato = preco
        barato = nome
print(f'Total gasto: {soma}')
print(f'Produtos acima de 1000 Reais: {produtos_1000_reais} ')
print(f'Produto mais barato: {barato}')
