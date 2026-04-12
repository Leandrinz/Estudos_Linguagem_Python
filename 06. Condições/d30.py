# Recebe número inteiro
n = int(input('Digite um número: '))

# Verifica se é par ou impar
if n%2 == 0:
    print('O número {} é par!'.format(n))
else:
    print('O número {} é impar!'.format(n))