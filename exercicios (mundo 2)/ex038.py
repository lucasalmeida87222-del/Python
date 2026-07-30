#Escreva um programa que leia dois numeros inteiros e compare-os, mostrando na tela uma mensagem:
n1 = int(input('Digite o primeiro valor: '))
n2 = int (input('Digite o segundo valor: '))
if n1 > n2:
    print(f' O primeiro valor {n1} é maior')
elif n1 < n2:
    print(f'O segundo valor {n2} é maior')
else:
    print('Não existe valor maior, os dois são iguais')