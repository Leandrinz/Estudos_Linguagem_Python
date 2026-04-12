import random
print('-------- JOKENPÔ --------')
print("""        Bem vindo
     1    -   Pedra
     2    -   Papel
     3    -   Tesoura """)

# Recebe jogada do usuário
jogadas = {1: 'Pedra', 2: 'Papel', 3: 'Tesoura'}
jogada_usuario = int(input('Por favor, escolha sua jogada: '))
jogada_maquina = random.randint(1,3)
print('Processando resultado...')

# Verifica resultado
if jogada_usuario == jogada_maquina:
    print('Empate')
elif jogada_usuario == 1 and jogada_maquina == 2:
    print('Vitória do computador!')
elif jogada_usuario == 1 and jogada_maquina == 3:
    print('Você venceu!')
elif jogada_usuario == 2 and jogada_maquina == 1:
    print('Você venceu!')
elif jogada_usuario == 2 and jogada_maquina == 3:
    print('Vitória do computador!')
elif jogada_usuario == 3 and jogada_maquina == 1:
    print('Vitória do computador!')
else:
    print('Você venceu!')
print("""Sua jogada: {}. 
Jogada do computador: {}""".format(jogadas[jogada_usuario], jogadas[jogada_maquina]))