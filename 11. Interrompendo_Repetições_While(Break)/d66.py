# Recebe vários números inteiros, parando apenas no número 999. Ao final será exibido quantos números foram digitados e a soma deles (exceto o 999 que é uma flag)
numero = 0
soma = 0
numeros_digitados = 0
while True:
    numero = int(input('Digite um número inteiro (se quiser parar, digite 999): '))
    if numero == 999:
        break
    soma += numero
    numeros_digitados += 1
print(f'O total de números digitados foi igual a: {numeros_digitados}')
print(f'A soma dos números: {soma}')
