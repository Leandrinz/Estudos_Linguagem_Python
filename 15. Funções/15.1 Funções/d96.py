def l():
    print('-=' * 20)
def area(largura, comprimento):
    a = largura * comprimento
    print(f'A área tem {a} metros quadrados.')


l()
print('CONTROLE DE TERRENOS')
l()
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(l,c)