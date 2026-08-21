#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. no final mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.
from random import randint
valores = []
pares = []
for c in range(0, 4):
    valores.append(randint(0, 100))
    
n = tuple(valores)
a = n.count(9)

for c in n:
    if c % 2 == 0:
        pares.append(c)

print(f'Os valores digitados foram {n}')
print(f'O numero 9 apareceu {a} vezes')

# Verificação de segurança para o número 3
if 3 in n:
    print(f'O primeiro valor 3 foi digitado na posição {n.index(3) + 1}')
else:
    print('O valor 3 não foi digitado em nenhuma posição')

print(f'Os números pares são {pares}')