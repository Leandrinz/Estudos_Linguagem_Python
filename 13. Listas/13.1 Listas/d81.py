lista = []
c5 = 0
t = 0
# Lê vários números
while True:
    numero = int(input('Digite um número: '))
    lista.append(numero)
    t += 1
    if numero == 5:
        c5 += 1

    resposta = str(input('Quer continuar? [S/N]: ')).upper()
    if resposta == 'N':
        break
lista.sort(reverse=True)
print(f'Os valores digitados {lista}')
if c5 > 0:
    print(f'O número 5 foi digitado {c5} vezes')
else:
    print('O número 5 não foi digitado!')
print(f'Foram digitados {t} valor(es)')