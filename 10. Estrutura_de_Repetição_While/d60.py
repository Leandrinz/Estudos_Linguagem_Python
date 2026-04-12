# Fatorial
n = int(input('Digite um valor para ver seu fatorial: '))
f = n
c = n - 1

while c != 0:
    f = f * c
    c = c - 1
print('O fatorial de {} é {}'.format(n,f)) 