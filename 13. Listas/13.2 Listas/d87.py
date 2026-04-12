# Matriz 3 x 3
lista = [[0,0,0], [0,0,0], [0,0,0]]
soma_pares = 0
soma_terceiracoluna = 0

# Recebe os valores das posições da matriz
for c in range (0,3):
    for l in range (0,3):
        n = int(input(f'Digite o valor da posição [{c}][{l}]da matriz: '))
        # Verifica o maior número da segunda linha
        if c == 1:
            if c == 1 and l == 0:
                maior_s = n
            if n > maior_s:
                maior_s = n
        # Verifica o maior número da matriz
        if c == 0 and l == 0:
            maior = n    
        if n > maior:
            maior = n 
        # Soma dos pares
        if n % 2 == 0:
            soma_pares += n
        # Soma da terceira coluna
        if l == 2:
            soma_terceiracoluna += n
        
        lista[c][l] = n

# Exibe a matriz
print('+=' * 15)
print('MATRIZ')
for c in range(0,3):
    for l in range(0,3):
        print(lista[c][l], end=' ' )
    print('')
# Exibe soma dos pares, soma da terceira coluna e maior valor da matriz
print(f'A soma dos pares foi: {soma_pares}')
print(f'A soma dos valores da terceira coluna: {soma_terceiracoluna} ')
print(f'Maior valor da matriz: {maior}')
print(f'Maior número da segunda linha: {maior_s}')