# Recebe Valor em real
real = float(input('Digite quanto dinheiro em real você tem: '))
# Conversão 
dol = real / 3.27
# Exibe quantos dólares ela pode ter
print('Você pode comprar {:.1f} dólares'.format(dol))