#Faça um programa que leia um numero inteiro e diga se ele é ou não um numero primo.
num = int(input('Digite um numero inteiro: '))
total = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end = '')
        total += 1
    else:
        print('\033[31m', end = '')
    print(f'{c}', end = '')
print(f'\n\033[mO numero {num} foi divisivel {total} vez(es)')
if total == 2:
    print('E por isso ele É PRIMO')
else:
    print('Por isso ele NÃO É PRIMO')

