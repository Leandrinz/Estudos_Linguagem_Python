# Recebe preço original do produto
po = float(input('Digite o preço do produto: '))
# Calcula o preço pós desconto de 5%
pa = po - (po * 0.05)
# Exibe o novo preço
print('O valor do produto de {} reais, ficou por {} após desconto de 5%'.format(po,pa))