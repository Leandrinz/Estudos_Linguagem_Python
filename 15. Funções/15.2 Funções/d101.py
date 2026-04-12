def l():
    print('-=' * 20)
def vota(nascimento):
    global idade 
    idade = 2025 - nascimento
    if idade >= 18:
        return 'OBRIGATÓRIO'
    elif idade < 16:
        return 'NEGADO'
    else:
        return 'OPCIONAL'

l()
data_nascimento = int(input('Ano de nascimento: '))
vota(data_nascimento)
print(f'Com {idade} anos: SITUAÇÃO - {vota(data_nascimento)}')