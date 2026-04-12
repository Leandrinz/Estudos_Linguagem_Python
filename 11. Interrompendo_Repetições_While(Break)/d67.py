# Mostra a tabuada de vários números e só para quando o usuário digitar um número negativo
# Tabuada
while True:
    numero = int(input('Digite um número para ver sua tabuada (se quiser parar o programa, digite um valor negativo!): '))
    contador = 1
    if numero < 0:
            break
    
    while contador <= 10:
        print(f'{numero} x {contador} = {numero * contador}')
        contador += 1

print('FIM DO PROGRAMA!!!')