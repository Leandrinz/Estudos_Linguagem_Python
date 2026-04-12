maior = 'Vasco da Gama'
cores = {'limpa' :'\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'Preto e Branco': '\033[7;30m'}

print('\033[1;34;44mVasco da Gama\033[m')
print('\033[1;31;45mVASCO DA GAMA\033[m')
print('\033[1;31;41mVASCO DA GAMA\033[m')
print('\033[1;31;41mVASCO DA GAMA\033[m')


print('O maior time do mundo é o \033[1;30;46mVasco da Gama\033[m')
print('O maior time do mundo é o {}{}{}'.format(cores['amarelo'],maior,cores['limpa']))
#\033[0;30;41m
#\033[4;33;44m
#\033[1;35;43m
#\033[30;42m
#\033[m
#\033[7;30m
