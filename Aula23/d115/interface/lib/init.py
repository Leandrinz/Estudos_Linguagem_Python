def leiaint(msg = 0):
    while True:
        try: 
            msg = int(input(f"\033[32mSua opção: \033[32m"))
        except ValueError:
            print('ERRO! Digite um valor inteiro!!!')
        except KeyboardInterrupt:
            print("O usuário não digitou o número!")
        else:
            return msg
        


def linha(tam = 42):
    return('-' * tam)


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho("MENU PRINCIPAL".center(42))
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[33m - \033[34m{item}\033[34m')
        c += 1
    print(linha())
    opc = leiaint()
    return opc

