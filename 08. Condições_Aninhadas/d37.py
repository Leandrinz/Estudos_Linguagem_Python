# Recebe número e a conversão desejada
n = int(input('Digite um número: '))
b = bin(n)[2:]
o = oct(n)[2:]
h = hex(n)[2:]
print('----------- CONVERSÃO ----------')
print(' 1 - Binário')
print(' 2 - Octal')
print(' 3 - Hexadecimal')
print('--------------------------------')
c = int(input('Escolha qual conversão deseja fazer: '))

if c == 1:
    print('Binário: {}'.format(b))

elif c == 2:
    print('Octal: {}'.format(o))

elif c == 3:
    print('Hexadecimal: {}'.format(h))
    
else:
    print('Número inválido, por favor tente novamente!')