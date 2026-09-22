#1 usando dentro de um laço de repetição.
pessoas = {'nome': 'Lucas', 'sexo': 'M', 'idade': 29}
for k, v in pessoas.items(): # k = keys e v = values.
    print(f'{k} = {v}')
print('FIM')
print('-' * 40)
#----------------------------------------------------------------------------------------------------------------------------------------
#2 apagando informações.
pessoas = {'nome': 'Lucas', 'sexo': 'M', 'idade': 29}
del pessoas['sexo']
for k, v in pessoas.items():
    print(f'{k} = {v}')
    print('FIM')
print('-' * 40)
#----------------------------------------------------------------------------------------------------------------------------------------
#3 Alterando valores.
pessoas = {'nome': 'Lucas', 'sexo': 'M', 'idade': 29}
pessoas ['nome'] = 'Goku'
for k, v in pessoas.items():
    print(f'{k} = {v}')
print('FIM')
print('-' * 40)
#----------------------------------------------------------------------------------------------------------------------------------------
#4 Adicionando elementos.
pessoas = {'nome': 'Lucas', 'sexo': 'M', 'idade': 29}
pessoas ['peso'] = '98'
for k, v in pessoas.items():
    print(f'{k} = {v}')
print('FIM')
print('-' * 40)
#----------------------------------------------------------------------------------------------------------------------------------------
#5 Criar um Dicionário dentro de uma Lista.
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1) # adicionando dentro da Lista.
brasil.append(estado2) # adicionando dentro da Lista.
print(brasil) 
print(brasil[0])
print(brasil[1])
print(brasil[0] ['uf'])
print('FIM')
print('-' * 40)
#----------------------------------------------------------------------------------------------------------------------------------------
#6 Adicionando elementos ao Dicionário, dentro de uma Lista.
estado = {}
brasil = []
for c in range(0, 2):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil: # e = Estado. Esse for é da Lista.
    for k, v in e.items(): # k = chave e v = valor. Esse for é do Dicionário.
        print(f'O campo {k} tem valor {v}.')
    for v in e.values():
        print(v, end=' ')
    print() # Pular linha.