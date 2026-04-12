# Recebe nome
print('Vamos verificar se o nome começa com SANTO!')
nome = str(input('Digite o nome: '))

# Verifica se começa com SANTO
pn = nome.split()[0]
print(pn) 
print('Santo' in pn)