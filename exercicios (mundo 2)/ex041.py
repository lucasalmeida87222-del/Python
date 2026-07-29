from datetime import date
atual = date.today().year
print('Confederação Nacional de Natação!')
print('''Categorias:
Até 9 anos: MIRIM
Até 14 anos: INFANTIL
Até 19 anos: JUNIOR
Até 25 anos: SÊNIOR
Acima de 25 anos: MASTER ''')
nasc = int(input('Em que ano você nasceu? '))
idade = atual - nasc
print(f'Você tem {idade} anos.')
if idade <= 9:
    print('Sua categoria de nadador é MIRIM!')
elif idade <= 14:
    print('Sua categoria de nadador é INFANTIL!')
elif idade <= 19:
    print('Sua categoria de nadador é JUNIOR!')
elif idade <= 25:
    print('Sua categoria de nadador é SÊNIOR!')
else:
    print('Sua categoria de nadador é MASTER!')