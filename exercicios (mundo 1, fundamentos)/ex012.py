#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
p = float(input('Qual o preço do produto? R$'))
r = p - (p * 5/100) #calcular porcentagem de desconto.

print(f'O produto esta no valor de R${p} , aplicando 5% de desconto ela vai ficar por R${r:.2f}')

