a = (2,5,4)
b = (5,8,1,2)
c = a + b
print(c)
# Ela só junta tudo
print(c.count(5))
# Mostra quantas vezes o número 5 aparece
print(c.index(8))
# Mostra em qual posição aparece o número 8 (ele pega a primeira ocorrência)

# No Python, as tuplas aceitam strings, inteiros e etc tudo misturado
pessoa = ('Leandro', 39, 'M', 66.6)

# Dá pra apagar uma tupla inteira:
del(pessoa)