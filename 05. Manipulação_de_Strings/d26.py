# Recebe uma frase
frase = str(input('Digite uma frase qualquer: '))

# Exibe o total de letras A, em que posição aparece pela primeira e última vez

fm = frase.lower()
print('Número de vezes em que a letra A aparece: {}'.format(fm.count('a')))
print('Primeira aparição na posição: {}'.format(fm.find('a')))
print('Ultima aparição na posição: {}'.format(fm.rfind('a')))