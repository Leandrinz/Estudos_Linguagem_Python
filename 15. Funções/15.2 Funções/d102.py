def fatorial(num, show = 0):
    """
    -> Calcula o fatorial de um número
    : para n: O número a ser calculado
    : Para show: (opcional) Mostrar ou não a conta
    : return: O valor fatorial de um número    
    """
    f = 1
    if show == 'True':
        for c in range(num,0,-1):
            f *= c
            if c != 1:
                print(f'{c} X', end=' ')
            else: 
                print(f'{c} = {f}')
    else:
        for c in range(num,0,-1):
            f *= c
    return f


n = int(input('Digite um valor para ver seu fatorial:'))
m = str(input('Mostrar calculo = True / Não mostrar: False: '))
res = fatorial(n,m)
