# Recebe a data de nascimento de 7 pessoas e vê quantas são ou não maiores de idade
maior = 0
menor = 0
for c in range(1,8):
    data_nascimento = int(input('Digite sua data de nascimento: '))
    if 2025 - data_nascimento >= 18:
        maior += 1
    else:
        menor += 1
print('Pessoas maiores de idade: {}'.format(maior))
print('Pessoas menores de idade: {}'.format(menor))