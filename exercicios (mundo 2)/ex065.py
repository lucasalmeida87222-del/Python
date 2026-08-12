#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a
#média entre todos os valores e o menor valor lido. O programa deve perguntar ao usuário se ele 
#quer ou não continuar a digitar valores.
n = 's'.upper().strip()
soma = 1
cont = 0
num = int(input('Digite um valor: '))
menor = num
while n != 'N':
    num = int(input('Digite um valor: '))
    soma += num
    cont += 1
    n = str(input('Quer continuar? [S/N] ')).upper()
    if menor < num:
        menor = menor
    else:
        menor = num
    if n == 'N':
        break
media = soma / cont
print(f'O valor total foi de {soma:.2f} e a média desse valor é {media:.2f} e o menor valor digitado foi {menor}')

#Resolução do professor
resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um numero: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma / quant
print(f'Você digitou {quant} numeros e a média foi {media}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
