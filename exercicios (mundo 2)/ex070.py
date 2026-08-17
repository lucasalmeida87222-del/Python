#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:
#A) Qual é o total gasto na compra. B) Quantos produtos custam mais de R$1000. C) Qual é o nome do produto mais barato.
total = 0
maior = 0
menor_preco = 0
produto_barato = ''
cont = 0 #Contador para identificar o 1º produto
while True:
    nome = str(input('Digite o nome de um produto: '))
    preco = float(input('Digite o valor do produto: '))
    total += preco
    cont += 1 #Soma +1 a cada produto lido
    if cont == 1 or preco < menor_preco:
        menor_preco = preco
        produto_barato = nome
    if preco > 1000:
        maior += 1
    continuar = str(input('Você quer continuar [S/N]? ')).upper().strip()
    while continuar != 'S' and continuar != 'N':
        print('Opção invalida!' ,end=' ')
        continuar = str(input('Você quer continuar [S/N]? ')).upper().strip()
    if continuar == 'N':
        break
print(f'O valor total gasto na compra foi de R${total}',end= ' ')
print(f'{maior} produto(s) são maiores que R$1000,00 e o produto mais barato é {produto_barato}')