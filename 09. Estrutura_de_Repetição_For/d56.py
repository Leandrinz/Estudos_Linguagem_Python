# Lê nome, idade e sexo de 4 pessoas e exibe média de idade, nome do homem mais velho, quantas mulheres tem mais de 20 anos
s = 0
idade_mais_velho = 0
mais_velho = ''
mulheres_menos_20anos = 0
for c in range(1,5):
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo (M/F): '))
    s += idade
    if sexo == 'M' and idade > idade_mais_velho:
        mais_velho = nome
    if sexo == 'F' and idade < 20:
        mulheres_menos_20anos += 1

m = s / 4
print('Média de idade: {}'.format(m))
print('Homem mais velho: {}'.format(mais_velho))
print('Número de mulheres com menos de 20 anos: {} '.format(mulheres_menos_20anos))