#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999,
#que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (exceto o flag).
cont = soma = 0
while True:
    numero = int(input('Digite um numero [para parar digite 999]: '))
    if numero == 999:
        break
    cont += 1
    soma += numero
print(f'Foram digitados {cont} numeros e a soma entre eles foi {soma}')