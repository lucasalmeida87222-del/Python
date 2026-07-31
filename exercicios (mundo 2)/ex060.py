#Faça um programa que leia um numero qualquer e mostre o seu fatorial.
#Ex: 5! = 5x4x3x2x1 = 120
numero = int(input('Digite um valor inteiro: '))
c = numero
fatorial = 1
print(f'Calculando {numero}! = ',end=' ')
while c > 0:
    print(f'{c}',end=' ')
    print('x' if c > 1 else '=',end=' ')
    fatorial *= c
    c -= 1
    print(f'{fatorial}')