def leiaint(numero):
    while True:
        try: 
            numero = int(input(numero))
        except ValueError:
            print('ERRO! Digite um valor inteiro!!!')
        else:
            return numero



n = leiaint(('Digite um número: '))
print(f'Você digitou o número {n}')
