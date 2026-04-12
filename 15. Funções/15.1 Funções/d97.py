def l(txt):
    print('-=' * ((len(txt) / 2).__round__() + 1))
    print(txt)
    print('-=' * ((len(txt) / 2).__round__() + 1))


msg = str(input('Digite a frase que quer mostrar na tela: '))
l(msg)