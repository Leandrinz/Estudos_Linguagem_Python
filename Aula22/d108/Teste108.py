import moeda

n = int(input('Digite seu salário: R$ '))
print(f'A metade de {moeda.moeda(n)} é R${moeda.moeda(n)}')
print(f'O dobro de {moeda.moeda(n)} é R${moeda.moeda(moeda.dobro(n))}')
print(f'Aumentando 10%, temos R${moeda.moeda(moeda.aumentar(n,10))}')
print(f'Reduzindo 10%, temos R${moeda.moeda(moeda.diminuir(n,10))}')