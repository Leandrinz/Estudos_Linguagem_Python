resposta = ''
lista = []
# Recebe valores e só aceita os números que ainda não estiverem na lista
while True:
    # Recebe valor
    numero = int(input('Digite um valor inteiro para ser inserido na lista: '))
    
    # Verifica se está presente na lista
    if numero in lista:
        print(f'{numero} já esta na lista!')
    else:
        lista.append(numero)
        print('Número adicionado com sucesso!')
    resposta = str(input('Quer continuar? (S/N):')).upper()
    if resposta == 'N':
        break
lista.sort()
print(f'Números digitados: {lista}')