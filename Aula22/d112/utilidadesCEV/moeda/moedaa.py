def metade(n, format = False):
    res = n/2
    return res if format is False else moeda(res)


def dobro(n, format =False):
    res = n * 2
    return res if format is False else moeda(res)


def aumentar(n,p, format=False):
    res = n + (n * p/100)
    return res if format is False else moeda(res)


def diminuir(n,p, format=False):
    res = n - (n * (p/100))
    return res if format is False else moeda(res)

def moeda(p = 0, moeda = 'R$'):
    return f'{moeda}{p:.2f}'.replace('.', ',')

def resumo(p = 0, taxaa = 10, taxar = 5):
    print("-" * 30)
    print("RESUMO DO VALOR".center(30))
    print("-" * 30)
    print(f"Preço analisado: {moeda(p)}")
    print(f"Dobro do preço: {dobro(p, True)}")
    print(f"Metade do preço: {metade(p, True)}")
    print(f"Com {taxaa}% de aumento: {aumentar(p, taxaa, True)}")
    print(f"Com {taxar}% de redução: {diminuir(p, taxar, True)}")
    print("-" * 30)
