# Verifica se um número é primo
n = int(input('Digite um número para verificar se ele é primo: '))
nd = 0

# Conta número de divisores
for c in range (n, 0, -1):
    if n % c == 0:
        nd += 1
if nd > 2:
    print('{} não é um número primo!'.format(n))
else:
    print('{} é um número primo!'.format(n))