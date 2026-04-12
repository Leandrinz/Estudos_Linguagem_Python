# Como fazer a copia
estado = {}
Brasil = []
for c in range(0,1):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    Brasil.append(estado.copy()) # Copia tudo
for e in Brasil:
    for v in e.values():
        print(v, end=' ')
    print()
