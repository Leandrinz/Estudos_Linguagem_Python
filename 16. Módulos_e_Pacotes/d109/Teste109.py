import moeda

n = int(input('Digite seu salário: R$ '))
print(f'A metade de {n} é R${moeda.moeda(n, True)}')
print(f'O dobro de {n} é R${moeda.dobro(n, True)}')
print(f'Aumentando 10%, temos R${moeda.aumentar(n,10, True)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(n, 13, True)}')
