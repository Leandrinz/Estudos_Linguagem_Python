# Recebe dois valores
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

# Exibe um menu e executa até determinada ação do usuário
c = 0
while c != 5:
    print("""        ---- MENU DE OPERAÇÕES ---- 
         CÓDIGO    |     AÇÃO
            1      |     SOMAR
            2      |  MULTIPLICAR
            3      |     MAIOR
            4      |  NOVOS NÚMEROS
            5      | SAIR DO PROGRAMA""") 
    c = int(input('Por favor, digite a operação desejada: '))
    if c == 1:
        print('SOMA: {}'.format(n1 + n2))
    elif c == 2:
        print('MULTIPLICAÇÃO: {}'.format(n1 * n2))
    elif c == 3: 
        if n1 > n2:
            print('Maior: {}'.format(n1))
        elif n1 == n2:
            print('Os dois são iguais')
        else:
            print('Maior: {}'.format(n2))
    elif c == 4:
        n1 = int(input('Digite o novo valor: '))
        n2 = int(input('Digite outro valor: '))
    else:
        print("==================")
        print(' FIM DO PROGRAMA')
        print("==================")