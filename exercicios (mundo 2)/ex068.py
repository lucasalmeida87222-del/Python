#Faça um programa que jogue par ou impar com o computador. O jogo só será interrompido quando o jogador perder,
#mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
cont = 0
while True:
    escolha = str(input('Você quer impar ou par? ')).lower().strip()
    while escolha != 'par' and escolha!= 'impar':
        escolha = str(input('Você quer impar ou par? ')).lower().strip()
    jogador = int(input('Digite um valor: '))
    computador = randint(1,101)
    print(f'computador: {computador}')
    soma = jogador + computador
    print(f'Total: {soma}')
    if escolha == 'par' and soma % 2 == 0:
        print('Jogador Venceu!')
        cont += 1
    elif escolha == 'impar' and soma % 2 != 0:
        print('Jogador venceu!')
        cont += 1
    else:
        print('Você perdeu!')
        break
    print(f'Contador: {cont}')
print(f'Numero de vitórias do jogador = {cont}')