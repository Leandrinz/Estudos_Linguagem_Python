c = ('\033[m', # 0 - sem cores
     '\033[0;30;41m', # 1 - vermelho
     '\033[0;30;42m', # 2 - Verde
     '\033[0,30,43m', # 3 - Amarelo
     '\033[0,30,44m', # 4 - Azul
     '\033[0,30,45m', # 5 - Roxo
     '\033[0,30m'     # 6 - Branco
     )


def ajuda(com):
    título(f'Acessando o manuel do comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')


def título(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(msg)
    print('~' * tam)
    print(c[0], end='')


while True:
    título('Sistema de ajuda pyhelp')
    comando = str(input('Função ou Biblioteca: '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
    título('ATÉ LOGO', 2)