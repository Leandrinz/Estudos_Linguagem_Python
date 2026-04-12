# Recebe dois valores
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

# Exibe o maior número ou se são iguais
if n1 > n2:
    print('{} é maior que {}'.format(n1,n2))
elif n2 > n1:
    print('{} é maior que {}'.format(n2,n1))
else:
    print('Os dois números são iguais!')
