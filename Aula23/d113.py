def leiaint():
    while True:
        try: 
            numero = int(input("Digite um valor inteiro: "))
        except ValueError:
            print('ERRO! Digite um valor inteiro!!!')
        except KeyboardInterrupt:
            print("O usuário não digitou o número!")
        else:
            return numero
        


def leiaFloat():
    while True:
        try:
            numero = float(input("Digite um valor float: "))
        except ValueError:
            print("Digite um valor float!")
        except KeyboardInterrupt:
            print("O usuário sofreu de amnésia e não digitou o dado!")
        else:
            return numero
    


numero_inteiro = leiaint()
numero_real = leiaFloat()
print(f"O valor inteiro digitado foi {numero_inteiro} e o real foi {numero_real}")