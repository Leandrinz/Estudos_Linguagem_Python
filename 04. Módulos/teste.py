from math import sqrt
import random
import emoji


num = int(input('Digite um número: '))


raiz = sqrt(num)
print('A raiz de {} é {}'.format(num,raiz))



n = random.random()
print('{:.2f}'.format(n))



print(emoji.emojize('Vamos codar!! :fire::smile::sunglasses:', language='alias'))
