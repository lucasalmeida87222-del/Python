from math import floor, trunc 
n = float(input('Digite um valor: '))
print(f'O valor digitado foi {n}, e a sua porção inteira é {floor(n)}')

#outra forma
n = float(input('Digite um valor: '))
print(f'O valor digitado foi {n} e a sua porção inteira é {trunc(n)}')