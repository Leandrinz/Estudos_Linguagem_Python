import random

# Recebe o nome dos 4 alunos
a1 = str(input('Digite o nome do 1º Aluno: '))
a2 = str(input('Digite o nome do 2º Aluno: '))
a3 = str(input('Digite o nome do 3º Aluno: '))
a4 = str(input('Digite o nome do 4º Aluno: '))

# Cria lista com alunos
alunos = [a1,a2,a3,a4]

# Sorteio 
s = random.choice(alunos)

# Exibe resultado
print('O aluno sorteado foi {}'.format(s))