# Recebe data de nascimento do atleta
data_nascimento = int(input('Digite o ano de seu nascimento: '))
idade_atleta = 2025 - data_nascimento

# Exibe a categoria para o usuário
if idade_atleta <= 9:
    print('Categoria: Mirim')

elif idade_atleta > 9 and idade_atleta <= 14:
    print('Categoria: Infantil')

elif idade_atleta > 14 and idade_atleta <=19:
    print('Categoria: Junior')

elif idade_atleta > 19 and idade_atleta <=20:
    print('Categoria: Sênior')

else:
    print('Categoria: Master')
