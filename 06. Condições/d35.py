# Recebe 3 retas
r1 = float(input('Digite o valor da reta 1: '))
r2 = float(input('Digite o valor da reta 2: '))
r3 = float(input('Digite o valor da reta 3: '))

# Verifica se pode ser um triângulo
if (r1 < r2 + r3) and (r2 < r1 + r3) and (r3 < r1 + r2):
    print('Pode ser um triângulo!')
else:
    print('Não pode ser um triângulo!')