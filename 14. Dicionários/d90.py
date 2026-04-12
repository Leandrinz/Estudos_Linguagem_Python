boletim = {}
boletim['Nome'] = str(input('Nome: '))
boletim['Media'] = float(input(f'Média de {boletim["Nome"]}: '))
if boletim['Media'] >= 7:
    boletim['Situação'] = 'Aprovado'
else:
    boletim['Situação'] = 'Reprovado'
for k,v in boletim.items():
    print(f'{k} é igual a {v}')