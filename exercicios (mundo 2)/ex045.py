from random import randint
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
computador = randint(0,2)
jogada = int(input('Qual a sua jogada? '))
print('''JO
KEN
PO!!!''')
print('-=-' * 20)
if jogada == 0 and computador == 1:
    print('Jogador jogou Pedra\nComputador jogou Papel')
    print('-=-' * 20)
    print('Computador VENCE!')
elif jogada == 2 and computador == 0:
    print('Jogador jogou Tesoura\nComputador jogou Pedra')
    print('-=-' * 20)
    print('Computador VENCE!')
elif jogada == 1 and computador == 2:
    print('Jogador jogou Papel\nComputador jogou Tesoura')
    print('-=-' * 20)
    print('Computador VENCE!')

elif jogada == 1 and computador == 0:
    print('Jogador jogou Papel\nComputador jogou Pedra')
    print('-=-' * 20)
    print('Jogador VENCE!')
elif jogada == 2 and computador == 1:
    print('Jogador jogou Tesoura\nComputador jogou Papel')
    print('-=-' * 20)
    print('Jogador VENCE!')
elif jogada == 0 and computador == 2:
    print('Jogador jogou Pedra\nComputador jogou Tesoura')
    print('-=-' * 20)
    print('Jogador VENCE!')

elif jogada == 0 and computador == 0:
    print('Jogador jogou Pedra\nComputador jogou Pedra')
    print('-=-' * 20)
    print('Deu EMPATE!')
elif jogada == 1 and computador == 1:
    print('Jogador jogou Papel\nComputador jogou Papel')
    print('-=-' * 20)
    print('Deu EMPATE!')
elif jogada == 2 and computador == 2:
    print('Jogador jogou Tesoura\nComputador jogou Tesoura')
    print('-=-' * 20)
    print('Deu EMPATE!')
else:
    print('Jogada INVALIDA! Escolha 0, 1 ou 2')
