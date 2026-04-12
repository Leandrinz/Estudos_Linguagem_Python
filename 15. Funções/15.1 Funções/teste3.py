def contador(*num):
    print(f'Numero de parâmetros passados: {len(num)}')
    print(f'Parâmetros passados: {num}')
def dobra(lista):
    pos = 0
    while pos < len(lista):
       lista[pos] = lista[pos] * 2
       pos += 1
    print(lista)
   
    


contador(2, 1, 7)
contador(0, 8)
contador(3, 4, 5, 6)
valores = [7,6,5,4,3,2,1]
dobra(valores)

