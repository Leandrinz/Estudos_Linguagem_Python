def maior_numero(*num):
    total = 0
    maior = 0
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    print('Analisando Valores passados...')
    if len(num) == 0:
        print('Foram informados 0 valores ao todo!')
        print('O maior valor informado foi 0.')
    else: 
        for c in num:
            print(f'{c}', end=' ')
            if total == 0:
                maior = c
            total += 1
            if c > maior:
                maior = c
        print(f' foram informados {total} valores ao todo.')
        print(f'O maior valor informado foi {maior}')
        print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')



maior_numero(4,5,2,1)
maior_numero(4,7,0)
maior_numero(1)
maior_numero()
    


    