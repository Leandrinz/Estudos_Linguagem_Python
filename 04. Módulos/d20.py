import random

# Recebe nome dos alunos
a1 = str(input('Digite o nome do 1° aluno: '))
a2 = str(input('Digite o nome do 2° aluno: '))
a3 = str(input('Digite o nome do 3° aluno: '))
a4 = str(input('Digite o nome do 4° aluno: '))

# Criação da lista dos alunos
alunos = [a1,a2,a3,a4]

# Sorteio da ordem
s = random.sample(alunos,4)

# Exibe ordem
print('A ordem da apresentação: {}'.format(s))