# Recebe preço normal de um produto e condição de pagamento
print('-------- BEM - VINDO(A) --------')
print('Por favor, abaixo digite o preço do produto selecionado e em seguida escolha a forma de pagamento!')
preco_normal = float(input('Digite o preço: '))
print(""" Código | Forma de pagamento | Descontos 
            1    | À Vista / Dinheiro | Desconto de 10%
            2    | À Vista / Cartão   | Desconto de 5%
            3    |  Até 2x no cartão  | Preço normal
            4    |  3x ou + cartão    | Juros de 20%""")
forma_pagamento = int(input('Digite o código correspondente a forma de pagamento desejada: '))
if forma_pagamento == 1:
    valor_total = preco_normal * 0.90 
elif forma_pagamento == 2: 
    valor_total = preco_normal * 0.95
elif forma_pagamento == 3:
    valor_total = preco_normal
else:
    forma_pagamento = preco_normal * 1.20
print('O valor total a ser pago é igual a: {}'.format(valor_total))