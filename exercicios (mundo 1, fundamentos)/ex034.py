#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$1.250,00, calcule um aumento de 10%.
#Para os inferiores ou iguais, o aumento é de 15%.
num = float(input('Qual o valor do seu salario? R$'))
n1 = num + (num * 10 / 100) #como calcular o aumento em porcentagem.
n2 = num + (num * 15 / 100)
if num <= 1.250:
    print(f'Com o aumento de 10% o seu salario foi para R${n1}')
else:
    print(f'Com o aumento de 15% o seu salario foi para R${n2}')

#outro modo
n = float(input('Qual o valor do seu salario? R$'))
if n >= 1250:
    novo = n + (n * 10/100)
    print(f'Com o aumento de 10% o seu salario foi para R${n1}')
else:
    novo = n + (n * 15/100)
    print(f'Com o aumento de 15% o seu salario foi para R${n2}')