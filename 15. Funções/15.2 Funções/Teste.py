def contador (a=0,b=0,c=0):
    """
    -> Faz a soma de 3 valores passados pelo usuário na chamada 
    da função.
    A: Primeiro Valor
    B: Segundo Valor
    C: Terceiro Valor
    S: Armazena os 3 valores.
    """
    s = 0
    s = a + b + c
    print(f'A soma vale {s}')


contador(1)
print(contador.__doc__)