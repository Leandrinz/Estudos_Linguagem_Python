# Recebe data de nascimento do usuário
print('------ ALISTAMENTO ------')
data_nascimento = int(input('Qual o ano em que você nasceu: '))
idade_usuario = 2025 - data_nascimento

# Informa situação do usuário
if idade_usuario > 18:
    print('Já faz {} ano(s) que você deveria ter se alistado'.format(idade_usuario - 18))
elif idade_usuario == 18:
    print('Está na hora de se alistar!')
else:
    print('Ainda falta {} ano(s) para você se alistar!'.format(18 - idade_usuario))
print('------ FIM ------')