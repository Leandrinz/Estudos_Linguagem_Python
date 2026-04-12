# Recebe 3 retas
r1 = float(input('Digite o valor da primeira reta: '))
r2 = float(input('Digite o valor da segunda reta: '))
r3 = float(input('Digite o valor da terceira reta: '))

# Verifica se os valores formam um triângulo e se é equilátero, isósceles ou escaleno
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:

    if r1 == r2 and r2 == r3:
        print('O triângulo é Equilátero')
    
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('O triângulo é Isósceles')
    
    else:
        print('O triângulo é Escaleno')
else:
    print('Os valores das retas fornecidos não formam um triângulo!')