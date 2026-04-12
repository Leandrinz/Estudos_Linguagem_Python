import random
tupla = random.sample(range(1,101), 5)
maior = tupla[0]
menor = tupla[0]
for c in range(0, len(tupla)):
    if tupla[c] > maior:
        maior = tupla[c]
    if tupla [c] < menor:
        menor = tupla[c]
print(tupla)
print(f'Maior: {maior}')
print(f'Menor: {menor}')