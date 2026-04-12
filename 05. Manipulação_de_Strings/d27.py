# Recebe nome
nome = str(input('Digite seu nome: '))

# Exibe o primeiro e ultimo nome
partes = nome.split()
print('primeiro: {}'.format(partes[0]))
print('último: {}'.format(partes[-1]))