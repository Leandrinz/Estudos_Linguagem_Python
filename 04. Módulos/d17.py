import math

# Recebe valores dos catetos
ca = float(input('Digite o valor do cateto adjacente: '))
co = float(input('Digite o valor do cateto oposto: '))

# Calcula a hipotenusa
h = math.hypot(co,ca)

# Exibe resultado
print('O valor da hipotenusa é: {:.2f}'.format(h))
