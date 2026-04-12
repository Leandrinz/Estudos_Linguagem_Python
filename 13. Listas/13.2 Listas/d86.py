# Matriz 3 x 3
lista = [[0,0,0], [0,0,0], [0,0,0]]
# Armazena valores na matriz
for c in range (0,3):
    for l in range (0,3):
        n = int(input(f'Digite o valor da posição [{c}][{l}]da matriz: '))
        lista[c][l] = n
# Exibe a matriz
print('+=' * 15)
print('MATRIZ')
for c in range(0,3):
    for l in range(0,3):
        print(lista[c][l], end=' ' )
    print('')