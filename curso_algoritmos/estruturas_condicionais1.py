# Condicional Simples
from datetime import date
atual = date.today().year
nasc = int(input('Em que ano você nasceu? '))
idade = atual - nasc
if idade >= 21:
    print(f'Em {atual} você terá {idade}, logo você é maior de idade!')
    
# Condicional Composta
dinheiro = float(input('Quanto de dinheiro você possui? '))
if dinheiro >= 1000:
    print('Partiu Disney')
else:
    print('#chateado')

print('-' * 20)
print('DEPARTAMENTO DE TRANSITO')
print('- * 20')
atual = date.today().year
nasc = int(input('Em que ano você nasceu? '))
idade = atual - nasc
if idade >= 18:
    print(f'Você tem {idade} anos e já pode dirigir.')
else:
    print(f'Você tem {idade} anos e ainda não pode dirigir.')

n1 = float(input('Nota1:'))
n2 = float(input('Nota2:'))
media = (n1 + n2) / 2
if media >= 6:
    print(f'Sua média é {media} e você esta APROVADO!')
else:
    print(f'Sua média é {media} e você esta REPROVADO!')