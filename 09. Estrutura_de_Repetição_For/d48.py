# Exibe a soma entre números ímpares que são múltiplos de 3 entre 1 até 500
s = 0
for c in range (1,501,2):
    if c % 3 == 0:
        s += c 
print('A soma dos números ímpares que são múltiplos de 3 é igual a: {}'.format(s))