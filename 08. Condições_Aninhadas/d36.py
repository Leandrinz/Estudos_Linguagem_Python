# Recebe valor da casa, salário e em quantos anos o usuário irá pagar
vc = float(input('Digite o valor da casa: '))
s = float(input('Digite seu salário: '))
qa = int(input('Em quantos anos você pretende pagar: '))

# Calcula a quantidade de parcelas e prestação mensal
qtdp = qa * 12
pm = vc / qtdp

if pm > (s * 0.3):
    print('Infelizmente você não pode financiar esta casa!')
else:
    print("""O financiamento pode ser feito com sucesso!
             Prestação mensal: {:.2f}
             Quantidade de parcelas: {}""".format(pm,qtdp))
