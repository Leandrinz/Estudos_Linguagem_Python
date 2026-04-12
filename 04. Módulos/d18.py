import math

# Recebe ângulo em graus
ang = float(input('Digite o valor do ângulo: '))

# Converte para radianos
rad = math.radians(ang)

# Calculo do seno, cosseno e tangente do ângulo
sen = math.sin(rad)
cos = math.cos(rad)
tang = math.tan(rad)

# Exibe resultado
print('Ângulo: {} \n Seno: {:.2f} \n Cosseno: {:.2f} \n Tangente: {:.2f}'.format(ang, sen, cos, tang))