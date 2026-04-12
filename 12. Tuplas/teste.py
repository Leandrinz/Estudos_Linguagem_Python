lanche = ('Hamburguer', 'Pizza', 'Suco', 'Pudim')
# Pra tupla, você usa parênteses ()

print(lanche)
print(lanche[1])
print(lanche[1:])
print(lanche[-1])
print(len(lanche))

# Existe três formas de colocar no for e printar a variável:

# Primeira
for c in range(0,len(lanche)):
    print(f'Eu vou comer {lanche[c]} na posição {c}')
print('\n')

# Segunda
for c in lanche:
    print(c)
print('')

print(lanche[-2])
# Terceira
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi demais')
print('')

# Mostra em ordem 
print(sorted(lanche))
# Ele até transforma em lista pra exibir, tendo em vista que tuplas são IMUTÁVEIS
