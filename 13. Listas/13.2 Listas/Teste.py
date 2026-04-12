teste = []
teste.append('Leandro')
teste.append(40)
galera = []
# galera.append(teste)   # Assim fica uma ligação, então qualquer coisa que muda em um, muda em outro
galera.append(teste[:]) # Agpra não fica ligação, pois apenas copiamos o conteúdo
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)