# Recebe o número e razão da progressão aritmética
numero = int(input('Digite o número: '))
razao = int(input('Digite a razão da PA: '))
termos = int(input('Digite quantos termos: '))

termo_n = numero + (termos - 1) * razao
termo = numero

# Mostra os termos
while True:
    while termo <= termo_n:
        print(termo)
        termo += razao
    
    adiciona = int(input('Quer mostrar mais termos? (aperte 0 para encerrar): '))
    if adiciona == 0:
        break
    termos += adiciona
    termo_n = numero + (termos - 1) * razao

print('====================')
print('  FIM DO PROGRAMA')
print('====================')