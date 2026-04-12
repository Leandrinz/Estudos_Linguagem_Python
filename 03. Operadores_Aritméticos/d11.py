# Recebe valor da largura e altura da parede
altura = float(input('Digite a altura em metros da parede: '))
largura = float(input('Digite a largura em metros da parede: '))
# Calculo da área
area = altura * largura
# Calculo da tinta (l) necessária
tinta = area / 2
# Exibição do resultado
print('A quantidade em litros de tinta necessária para pintar uma parede de {} de área é {} Litros de tinta'.format(area,tinta))