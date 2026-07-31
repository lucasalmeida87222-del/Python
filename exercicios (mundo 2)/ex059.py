#Crie um programa que leia dois valores e mostre o menu na tela: [1] somar, [2] multiplicar, [3] maior
#[4] novos numeros, [5] sair do programa. Seu programa deverá realizar a operação solicitada em cada caso.
from time import sleep
n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
opcao = 0
while opcao != 5:
    print('-=-' * 20)
    print('\033[1;32;40m MENU DE OPÇÕES\33[m')
    print('-=-' * 20)
    print('\033[1;32m[ 1 ] Somar\33[m')
    print('\033[1;32m[ 2 ] Multiplicar\33[m')
    print('\033[1;32m[ 3 ] Maior\33[m')
    print('\033[1;32m[ 4 ] Novos numeros\33[m')
    print('\033[1;32m[ 5 ] Sair do programa\33[m')
    print('-=-' * 20)
    opcao = int(input('Qual é a sua opção desejada: '))
    if opcao == 1:
        print(f'\033[1;36m{n1} + {n2} =\033[m \033[1;32m{n1+n2}\33[m')
    elif opcao == 2:
        print(f'\033[1;36m{n1} x {n2} =\033[m \033[1;32m{n1*n2}\33[m')
    elif opcao == 3 and n1 > n2:
        print(f'\033[1;36m Entre os valores {n1} e {n2} o maior valor é\33[m \033[1;32m{n1}\33[m')
    elif opcao == 3 and n2 > n1:
        print(f'\033[1;36m Entre os valores {n1} e {n2} o maior valor é\33[m \033[1;32m{n2}\33[m')
    elif opcao == 3 and n1 == n2:
        print(f'\033[1;36mOs dois valores são iguais ({n1})!\33[m')
    elif opcao == 4:
        print('Informe os numeros novamente: ')
        n1 = float(input('Primeiro valor: '))
        n2 = float(input('Segundo valor: '))
    elif opcao == 5:
        sleep(1)
        print('\033[1;31m Finalizando...\33[m')
        sleep(1)
print(f'\033[1;42m Fim do programa! Volte sempre!\33[m')