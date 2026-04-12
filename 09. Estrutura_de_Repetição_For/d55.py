# Lê peso de 5 pessoas e mostra o maior e o menor peso
peso = float(input('Digite seu peso: '))
maior = peso
menor = peso

for c in range (2,6):
    peso = float(input('Digite seu peso: '))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print('Maior peso: {}'.format(maior))
print('Menor peso: {}'.format(menor))