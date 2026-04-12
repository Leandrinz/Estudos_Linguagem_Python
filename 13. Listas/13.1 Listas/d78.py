lista = []
maior = 0
menor = 0
pma = []
pme = []
# Recebe 5 números e os armazena em uma lista
for c in range(0,5):

    numero = int(input(f'Digite um número para a posição {c}: '))
    lista.append(numero)
    # Verifica o maior e menor número e armazena suas posições
    if c == 0:
        maior = menor = numero
    if numero > maior:
        maior = numero
        pma = [c]
    elif numero == maior:
        pma.append(numero)

    if numero < menor:
        menor = numero
        pme = [c]
    elif numero == menor:
        pme.append(c)
    
    


# Exibe a lista, o maior e menor número e suas respectivas posições
print(f'Você digitou os números: {lista}')
print(f'O maior número foi {maior} digitado nas posições ', end='')
for i,v in enumerate(lista):
    if v == maior:
        print(f'{i}... ', end = '')
print()
print(f'O menor número foi {menor} digitado nas posições ', end = '')
for i,v in enumerate(lista):
    if v == menor:
        print(f'{i}... ',end='')