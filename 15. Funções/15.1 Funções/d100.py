import random
lista = []

# Função para preencher uma lista com 5 números
def sorteia():
    print('Sorteando 5 números...', end=' ')
    for c in range(0,5):
        n = random.randint(1,21)
        lista.append(n)
    print(lista, end=' ')
    print('Pronto!')
# Função para somar apenas os pares da lista
def somar():
    soma = 0
    for p in lista:
        if p % 2 == 0:
            soma += p
    print(f'Somando os valores pares de {lista} temos {soma}')

# Chama as funções
sorteia()
somar()