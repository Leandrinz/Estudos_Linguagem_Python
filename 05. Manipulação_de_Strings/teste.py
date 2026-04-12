frase = ' Vasco da Gama'
print(frase[1::2])
print('Oi')
# Se vc quiser printar um texto muito grande, coloque aspas triplas

print("""aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
      aaaaaaaaaaaaaaaaaaaaaaaaa
      aaaaaaaaaaaaaa
      aaaaaaaaaa""")


print(frase.upper().count('A'))
print(len(frase))
print(len(frase.strip()))

print(frase.replace('Gama', 'Bola'))
# Aqui a frase nn muda, pois isso tem que ser salvo ex: frase = print(frase.replace('Gama', 'Bola'))
print(frase)
print(frase.lower().find('vasco'))
dividido = frase.title().split()
print(dividido)
