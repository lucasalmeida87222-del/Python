#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
#Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint
valores = [] 
for c in range(0,5):
    valores.append(randint(0,100))
n = tuple(valores)
menor = min(n)
maior = max(n)
print(f'Os numeros gerados foram {n}, o maior numeros entre ele é {maior} e o menor é {menor}!')
