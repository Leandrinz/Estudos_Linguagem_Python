tupla = 'Vasco', 'Gama', 'Maior', 'Mundo'
vogais = 'aeiou'

for c in tupla:
    print(f'\nNa palavra {c.upper()} temos as vogais: ', end = '')
    for letra in c:
        if letra.lower() in vogais:
            print(letra, end=' ')