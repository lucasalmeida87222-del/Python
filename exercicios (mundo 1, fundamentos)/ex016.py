#Crie um programa que leia um numero real qualquer pelo teclado e mostre na tela a sua porção inteira.
from math import floor, trunc 
n = float(input('Digite um valor: '))
print(f'O valor digitado foi {n}, e a sua porção inteira é {floor(n)}')

#outra forma
n = float(input('Digite um valor: '))
print(f'O valor digitado foi {n} e a sua porção inteira é {trunc(n)}')