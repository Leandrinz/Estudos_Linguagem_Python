# Lê o sexo de uma pessoa, que só aceita M ou F
sexo = 'z'
while sexo != 'F' and sexo != 'M':
    sexo = input('Digite o seu sexo (F/M): ').strip().upper()
    if sexo != 'F' and sexo != 'M':
        print('Por favor, digite M ou F!')
