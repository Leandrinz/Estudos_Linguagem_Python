maiores_18anos = 0
homens = 0
mulheres_menos_20anos = 0
decisao = ''
while True:
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo (M/F): ')).upper()
    if idade > 18:
        maiores_18anos += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres_menos_20anos += 1
    decisao = str(input('Quer continuar? (S/N)')).upper()
    if decisao == 'N':
        break
print(f'Maiores de 18 anos: {maiores_18anos}')
print(f'Homens: {homens}')
print(f'Mulheres com menos de 20 anos: {mulheres_menos_20anos}')
