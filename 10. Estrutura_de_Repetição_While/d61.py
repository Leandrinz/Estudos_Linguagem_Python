# Progressão Aritmética com while
n = int(input('Digite um número: '))
r = int(input('Digite a razão da PA: '))
dt = n + (10 - 1) * r
termo = n
while termo <= dt:
    print(termo)
    termo += r