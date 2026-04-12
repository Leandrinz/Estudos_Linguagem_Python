# Recebe notas do usuário e calcula sua média
n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
m = (n1 + n2) / 2

# Exibe situação do usuário
if m >= 7:

    print('Média: {:.2f}. Parabéns, você foi aprovado!'.format(m))

elif (m >=5) and (m < 7):

    print('Média: {:.2f}. Você está na recuperação!'.format(m))

else:
    print('Média: {:.2f}. Infelizmente você está reprovado!'.format(m))
