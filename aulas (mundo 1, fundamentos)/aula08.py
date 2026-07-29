import math #importa tudo da biblioteca 'math'
num = int(input('Digite um numero: '))
raiz = math.sqrt(num) #aqui importei somente da biblioteca 'math' referente a 'raiz'.
print(f'A raiz de {num} é igual a {math.ceil(raiz)}') # aqui com o 'ceil' fiz o arredondamento.
print(f'A raiz de {num} é igual a {raiz:.2f}') #aqui eu solicitei só com 3 casas decimais.

#Outro modo
from math import sqrt, floor #aqui com o comando 'from' eu solicitei só a importação de 'sqrt e floor'
num = int(input('Digite um numero: '))
raiz = sqrt(num) #como eu usei o 'from' aqui não preciso usar '.math'
print(f'A raiz de {num} é igual a {raiz:.2f}')

#outra biblioteca
import random #com esse comando ele fornece um numero aleatório, porém ele gera um numero de 0 até 1.
num = random.random()
print(num)

#outro modo
import random #se eu aperto 'import + espaço' eu posso escolher qual biblioteca importar.
num = random.randint(1, 10) #com o comando 'randint' eu posso escolhe de quanto até quando ele vai pegar.
print(num)

#exemplo de uma nova biblioteca
import emoji
print(emoji.emojize('Olá, Mundo :sunglasses:', language='alias')) 
#language='alias' serve para usar nomes alternativos/abreviados dos emojis


