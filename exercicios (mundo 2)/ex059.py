#Crie um programa que leia dois valores e mostre o menu na tela: [1] somar, [2] multiplicar, [3] maior
#[4] novos numeros, [5] sair do programa. Seu programa deverá realizar a operação solicitada em cada caso.
n1 = float(input('Digite um valor: '))
n2 = float(input('Digite outro valor: '))
print('-=-' * 20)
print('\033[1;32;40m MENU DE OPÇÕES\33[m')
print('-=-' * 20)
print('\033[1;32m[ 1 ] Somar\33[m')
print('\033[1;32m[ 2 ] Multiplicar\33[m')
print('\033[1;32m[ 3 ] Maior\33[m')
print('\033[1;32m[ 4 ] Novos numeros\33[m')
print('\033[1;32m[ 5 ] Sair do programa\33[m')
print('-=-' * 20)
opcao = int(input('Digite a opção desejada: '))