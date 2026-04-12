# Recebe a distância da viagem
dv = float(input('Qual a distância da viagem: '))

# Calcula preço
if dv <= 200.0:
    tp = 0.50 * dv
    print('O total a pagar será: {}R$'.format(tp))
else:
    tp = 0.45 * dv
    print('O total a pagar será: {}R$'.format(tp))
print('----- FIM -----')