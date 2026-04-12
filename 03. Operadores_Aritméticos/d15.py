# Recebe a quantidade de dias que o carro foi alugado e quantos km rodou
dias = int(input('Digite quantos dias o carro esteve alugado: '))
km = float(input('Quantos km o carro rodou: '))
# Calcula valor total a ser pago
vt = (dias * 60) + (km * 0.15)
# Exibe resultado
print('O total a pagar será de {} reais!'.format(vt))
