# Recebe a velocidade de um carro
v = float(input('Qual a velocidade que o carro estava?: '))

# Verifica se ultrapassou o limite (80km/h)
if v>=80.0:
    m = 7 * (v-80)
    print('Você ultrapassou a velocidade limite! Valor da multa: {}R$'.format(m))
else:
    print('Você estava nos limites de velocidade! Continue assim!')