resposta = ''
numero = int(input('Digite um número: '))
media = 0
soma = numero
maior = numero
menor = numero
quantidade_numeros = 1
resposta = str(input('Quer continuar?(S/N):')).upper()

while resposta != 'N':

    numero = int(input('Digite um número: '))
    
    soma += numero
    
    quantidade_numeros += 1
    
    if numero > maior:
        maior = numero
    
    if numero < menor:
        menor = numero

    resposta = str(input('Quer continuar?(S/N):')).upper()
media = soma / quantidade_numeros

print('A média total foi: {:.2f}'.format(media))
if maior != menor:
    print('Maior: {}'.format(maior))
    print('Menor: {}'.format(menor))
else:
    print('Não houve número maior, nem menor. Ambos os números foram iguais {}'.format(menor))
