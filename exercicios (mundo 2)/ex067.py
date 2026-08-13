#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
#O programa será interrompido quando o número solicitado for negativo.
cont = 10
while True:
    numero = int(input('Digite um numero para ver a sua tabuada: '))
    if cont <= 10: 
        cont -= 1
        print(cont)