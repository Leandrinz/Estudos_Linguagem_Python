#def somar(a=0,b=0,c=0):
  #      s = a + b + c
 #       print(f'A soma vale {s}')


#somar(3,2,5)
#somar(2,2)
#somar(6)
# E se eu quiser mostrar a soma das somas?
# ficaria assim:
def somar(a=0,b=0,c=0):
    s = a + b + c
    return s


r1 = somar(3,2,5)
r2 = somar(1,7)
r3 = somar(4)
print(f'A soma das somas foi igual a {r1 + r2 + r3}')