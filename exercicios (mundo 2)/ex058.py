#Melhore o jogo onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar
#até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint
jogador = int(input('Digite um numero inteiro entre 0 e 10: '))
computador = randint(0,10)
contador = 1
while jogador != computador:
    jogador = int(input('Digite novamente um numero inteiro entre 0 e 10: '))
    contador += 1
print(f'O jogador levou {contador} tentativas para acertar!')
