lista = [[], []]
for c in range(0,7):
    n = int(input(f'Digite o {c+1}o. valor: '))
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)
lista[0].sort()
lista[1].sort()
print(f'Números pares: {lista[0]}')
print(f'Números ímpares: {lista[1]}')