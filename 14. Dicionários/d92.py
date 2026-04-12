perfil = {}
# Recebe nome, ano de nascimento, carteira de trabalho (mostrando idade) e etc
perfil['Nome'] = str(input('Nome: '))
perfil['Ano de Nascimento'] = int(input('Ano de Nascimento: '))
perfil['Idade'] = 2025 - perfil['Ano de Nascimento']
perfil['Carteira de Trabalho'] = int(input('Carteira de trabalho (0 não tem): '))
if perfil['Carteira de Trabalho'] != 0:
    perfil['Ano de Contratação'] = int(input('Ano de Contratação: '))
    perfil['Salário'] = float(input('Salário: '))
    perfil['Aposentadoria'] = perfil['Idade']+ 35 - (2025 - perfil['Ano de Contratação'])
print('-=' * 20)
for k,v in perfil.items():
    print(f'{k} = {v}')
