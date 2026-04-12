# Caixa eletrônico
valor_sacado = int(input('Digite o valor a ser sacado: '))
notas_50 = notas_20 = notas_10 = notas_1 = 0
resto = valor_sacado
# Contagem de notas de 50
while True:
    while resto >= 50:
        resto -= 50
        notas_50 += 1

    while resto >= 20:
        resto -= 20
        notas_20 += 1
    
    while resto >= 10:
        resto -= 10
        notas_10 += 1
    
    while resto >= 1:
        resto -= 1
        notas_1 += 1
    
    break
print(f"""Notas de 50 = {notas_50}
Notas de 20 = {notas_20}
Notas de 10 = {notas_10}
Notas de 1 = {notas_1} """)
