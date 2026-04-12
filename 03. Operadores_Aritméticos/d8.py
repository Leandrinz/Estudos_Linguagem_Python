# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros
# Recebe valor em metros
vm = float(input('Informe o valor em metros: ')) 
# Conversões
cm = vm * 100 
mlm = vm * 1000 
# Exibição
print('Metros: {}, centimetros: {}, milimetros: {}'.format(vm,cm,mlm))