#Faça um programa que leia o nome composto de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente.
nome = str(input('Digite seu nome completo: ')).strip()
a = nome.split()[0]
b = nome.split()[-1]
print(f'Primeiro nome = {a}\n Sobrenome = {b}')

#outro modo
n = str(input('Digite seu nome completo: ')).strip()
a = n.split()
print(f'Primeiro nome = {a[0]}\n Sobrenome = {a[len(a)-1]}')
#usei o len() pois ele vê o tamanho da frase, porém estavando dentro de uma lista,
#(fatiamento) e colocando -1 que vai pegar a ultima palavra.

