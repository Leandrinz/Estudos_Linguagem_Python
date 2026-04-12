# Recebe primeiro  termo e razão de uma PA

pt = int(input('Digite o primeiro termo: '))
r = int(input('Qual a razão da PA (progressão aritmética): '))

# Exibe os 10 primeiros termos da PA
print (pt)
for c in range(1,11):
    pt +=  r
    print(pt)
print('Fim')