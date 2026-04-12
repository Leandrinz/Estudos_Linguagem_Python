lista_geral = []
lista_pares = []
lista_impares = []

# Recebe valores e adiciona na lista geral, impares e pares
while True:
    numero = int(input('Digite um número: '))
    lista_geral.append(numero)
    if numero % 2 == 0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)


    resposta = str(input('Quer continuar?[S/N]:')).upper()
    if resposta == 'N':
        break
lista_pares.sort
lista_geral.sort
lista_impares.sort
print(f'Lista geral: {lista_geral}')
print(f'Lista de impares: {lista_impares}')
print(f'Lista de pares: {lista_pares}')