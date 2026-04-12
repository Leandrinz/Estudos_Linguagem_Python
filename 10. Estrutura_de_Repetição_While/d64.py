# Programa que lê vários números inteiros, calculando a soma de todos, quantos números foram digitados e só para quando o usuário digitar 999
print('Digite vários números e quando quiser parar, digite 999! ')
numero = 0
somatorio = 0
quantidade_digitada = 0
while numero != 999:
    numero = int(input('Digite um número: '))
    if numero != 999:
        somatorio += numero
        quantidade_digitada += 1
print('A soma dos números, exceto com o 999, foi: {}'.format(somatorio))
print('A quantidade de números digitados (exceto o 999): {}'.format(quantidade_digitada))