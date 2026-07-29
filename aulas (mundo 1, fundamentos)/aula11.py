print('\033[31m Olá, Mundo!')
print('\033[31;43m Olá, Mundo!')
print('\033[1;31;43m Olá, Mundo!')
print('\033[1;31;43m Olá, Mundo!\33[m') # coloquei \33[m no final para limitar a distancia da cor de fundo.
print('\033[4;30;45m Olá, Mundo!\33[m')
print('\033[;7;30;45m Olá, Mundo!\33[m')

#outro modo
nome = 'Lucas'
print(f'Olá, Muito prazer em te conhecer, {'\033[4;34m'} {nome} {'\033[m'}')

#modo mais avançado
n = 'Lucas'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}
print(f'Olá, Muito prazer em te conhecer, {cores['pretoebranco']} {nome} {cores['limpa']}')
# no caso de 'core = {}' eu acabei criando uma lista de cores.