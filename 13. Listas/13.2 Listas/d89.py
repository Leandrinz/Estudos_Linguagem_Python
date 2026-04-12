lista = []
lista_aluno = []
resposta = ''
while True:
    # Recebe nome, duas notas e a média do aluno até a quebra do laço
    lista_aluno.append(str(input('Digite o nome do aluno: ')))
    lista_aluno.append(float(input('Digite a primeira nota: ')))
    lista_aluno.append(float(input('Digite a segunda nota: ')))
    media = (lista_aluno[-1] + lista_aluno[-2]) / 2
    lista_aluno.append(media)
    lista.append(lista_aluno[:])
    lista_aluno.clear()
    media = 0
    resposta = str(input('Quer continuar? [S/N]:  ')).upper()
    if resposta == 'N':
        break

# Exibe os resultados individualmente
for p in lista:
        print(f'Aluno: {p[0]} / Média {p[3]}')
