# Recebe 3 números
m = 0
n1 = int(input('Digite o primeiro número: '))
if n1 > m:
    m = n1
n2 = int(input('Digite o segundo número: '))
if n2 > m:
    m = n2
    me = n1
else:
    me = n2
n3 = int(input('Digite o terceiro número: '))
if n3 > m:
    m = n3
if n3 < me:
    me = n3
print('O maior número foi: {} e o menor: {}'.format(m,me))
