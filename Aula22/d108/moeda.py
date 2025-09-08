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