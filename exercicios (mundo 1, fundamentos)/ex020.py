import random
a = str(input('Nome: '))
b = str(input('nome: '))
c = str(input('nome: '))
d = str(input('nome: '))
lista = [a, b, c, d]
ordem = random.shuffle(lista) #embaralha ordem dos elementos dentro da sua lista original.

print(f'Primero aluno {lista[0]}, Segundo aluno {lista[1]}, terceiro aluno {lista[2]}, quarto aluno {lista[3]}')
#foi colocado numeros dentro dos [] pois ele espera receber a posição(índice) do aluno.

#from random import shuffle # aqui só importamos o shuffle  da biblioteca random
