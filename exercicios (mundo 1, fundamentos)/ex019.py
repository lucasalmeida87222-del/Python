import random # Aqui avisamos o Python que vamos usar coisas aleatórias
a = str(input('Nome do aluno a: '))
b = str(input('Nome do aluno b: '))
c = str(input('nome do aluno c: '))
d = str(input('nome do aluno d: '))

lista = [a, b, c, d] #colocando os nomes dentro de uma lista []
escolhido = random.choice(lista) #choice significa escolha

print(f'O aluno escolhido foi {escolhido}')


#from random import choice # aqui só importamos o choice da biblioteca random
