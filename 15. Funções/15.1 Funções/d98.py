# Função contador
import time
def contador(inicio, fim, passo):
    # Corrige passo se for 0:
    if passo == 0:
        passo = 1
    
    # Corrige sinal do passo
    if inicio < fim and passo < 0:
        passo = -passo
    elif inicio > fim and passo < 0:
        passo = -passo
    

    if fim > inicio:
        print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        print(f'Contagem de {inicio} até  {fim} de {passo} em {passo}')
        for c in range(inicio,fim+1,passo):
            print(c, end=' ',flush=True)
            time.sleep(1)
        print('FIM!')
        time.sleep(1)
        print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        time.sleep(1)
    else:
        print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        print(f'Contagem de {inicio} até  {fim} de {passo} em {passo}')
        for c in range(inicio,fim-1, -passo):
            print(c, end=' ', flush=True)
            time.sleep(1)
        print('FIM!')
        print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        time.sleep(1)

# Contador de 1 até 10, passo 1 / Contador de 10 até 0, passo 2
contador(1,10,1)
contador(inicio = 10, fim = 0, passo = 2)

# Contador personalizao pelo usuário
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i,f,p)