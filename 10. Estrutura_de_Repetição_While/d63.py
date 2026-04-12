# Sequência de Fibonacci
numero = int(input('Digite o número: '))
numero1_anterior = numero - 1
numero2_anterior = 0
termo_atual = numero + numero1_anterior
c = 1
termos = int(input('Quantos termos você quer que sejam executados: '))

while c < termos:
    print(termo_atual)
   
    numero2_anterior = numero1_anterior
    numero1_anterior = termo_atual
    termo_atual = numero1_anterior + numero2_anterior

    c += 1 