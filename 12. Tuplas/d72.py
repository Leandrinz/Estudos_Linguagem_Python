contagem = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
    numero = int(input('Digite um número de 0 a 20: '))
    if numero >= 0 and numero <= 20:
        break
    else: 
        print('Digite um número válido!!!')
        print('')

print(f'Você digitou o número {contagem[numero]}')