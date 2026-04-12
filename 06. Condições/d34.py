# Recebe salário do funcionário
s = float(input('Digite o seu salário: '))

# Calcula reajuste
if s > 1250.0:
    sr = s * 1.10
else:
    sr = s * 1.15
print('O seu salário foi reajustado de {:.2f} para {:.2f}'.format(s,sr))
