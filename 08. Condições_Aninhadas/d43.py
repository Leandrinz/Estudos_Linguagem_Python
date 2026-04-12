# Recebe peso e altura do usuário
print('------- IMC -------')
peso = float(input('Digite o seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura ** 2)

# Exibe Status e IMC
if imc < 18.5:
    print('Status: Abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print('Status: Peso ideal')
elif imc >= 25 and imc < 30:
    print('Status: Sobrepeso')
elif imc >= 30 and imc < 40:
    print('Obesidade')
else:
    print('Status: Obesidade mórbida')
print('IMC : {:.2f}'.format(imc))