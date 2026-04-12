# Recebe um número de 0 a 9999
n = str(input('Digite um número de 0 a 9999: '))

# Mostra unidade, dezena, centena e milhar
print('Unidade: {}'.format(n[3]))
print('Dezena: {}'.format(n[2]))
print('Centena: {}'.format(n[1]))
print('Milhar: {}'.format(n[0]))
