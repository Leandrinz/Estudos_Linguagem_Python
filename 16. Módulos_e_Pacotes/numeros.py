import uteis


num = int(input('Digite um número: '))
fat = uteis.fatorial(num)
print(f'O número {num} é {fat}')
print(f'O dobro de {num} é {uteis.dobro(num)}')
print(f'O triplo de {num} é {uteis.triplo(num)}')
# Finja que o código começa a ficar bem grande, então podemos pegar
# todas essas funcionalidades e separar em um arquivo chamado 'uteis.py'.
# Mas agora, como vamos conectar os arquivos?
# Coloca antes da função: uteis.(nome da função)