# Recebe nome do usuário
nome = str(input('Digite seu nome: '))

# Exibe o nome com letras maiúsculas
print('Nome em maiúsculo: {}'.format(nome.upper()))

# Exibe o nome com letras minúsculas
print('Nome em minúsculo: {}'.format(nome.lower()))

# Exibe quantas letras tem ao todo
nd = nome.split()
nd = ''.join(nd)
print('O número de letras é: {}'.format(len(nd)))

# Exibe quantas letras tem  o primeiro nome
print('A quantidade de letras do primeiro nome é: {}'.format( len(nome.split()[0])))
