import moeda

n = int(input('Digite seu salário: R$ '))
print(f'A metade de {n} é R${moeda.metade(n)}')
print(f'O dobro de {n} é R${moeda.dobro(n)}')
print(f'Aumentando 10%, temos R${moeda.aumentar(n,10)}')
print(f'Reduzindo 10%, temos R${moeda.diminuir(n,10)}')