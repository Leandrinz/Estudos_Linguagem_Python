# Recebe a palavra 
palavra = str(input('Digite a palavra: '))
palavraz = palavra.strip()
palavraz = palavraz.lower()
palavraz = palavraz.replace(' ', '')
pi = ''

# Verifica se é palíndromo

for c in range(len(palavraz) - 1, -1, -1):
    pi += palavraz[c]
if pi == palavraz:
    print('{} é Palíndroma!'.format(palavra))
else:
    print('{} não é Palíndroma!'.format(palavra))
print(palavraz)
print(pi)
