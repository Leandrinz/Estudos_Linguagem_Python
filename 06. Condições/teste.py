nome = str(input('Qual é o seu nome: '))
if nome == 'Leandro':
    print('Que nome lindo!')
else:
    print('Seu nome é tão normal kk')
print('Bom dia {}'.format(nome))


n1 = float(input('Digite sua nota: '))
n2 = float(input('Digite a outra nota: '))
m = (n1 + n2) / 2
print('Sua média foi: {}'.format(m))
if m >= 7.0:
    print('Sua nota foi boa! PARABÉNS')
else:
    print('Sua nota foi abaixo da média, estude mais na próxima!')