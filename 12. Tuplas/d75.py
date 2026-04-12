n1 = int(input('Digite um valor: '))
n2 = int(input('Digite um valor: '))
n3 = int(input('Digite um valor: '))
n4 = int(input('Digite um valor: '))
tupla = n1, n2, n3, n4
print(tupla)
print(f'O número 9 aparece {tupla.count(9)} vezes')
print(f'Posição da primeira aparição do 3: {tupla.index(3)}')
print('Números pares: ')
for c in range(0, len(tupla)):
    if tupla[c] % 2 == 0:
        print(tupla[c])
