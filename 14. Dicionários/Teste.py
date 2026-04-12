pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
pessoas['nome'] = 'Leandro'
pessoas['idade'] = 19
print(pessoas)
print(pessoas['idade'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos') # Repare que foi necessário o uso de aspas duplas
print(pessoas.items())
for k,v in pessoas.items():
    print(f'{k} = {v}')