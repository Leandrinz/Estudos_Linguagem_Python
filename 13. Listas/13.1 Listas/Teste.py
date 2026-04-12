num = [2, 5 , 6 , 8]
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4')
print(num)


valores = []
for c in range (0,5):
    valores.append(int(input('Digite um número: ')))

print(valores)

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
