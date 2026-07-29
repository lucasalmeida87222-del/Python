from random import randint
#random 'aleatório' envolve sorteios e futilidades. randint 'int aleatorio'
computador = randint(0,5) #faz o computador 'PENSAR'
print('-=-' * 20) #vai colocar 20x aquele simbolo 
print('Vou pensar em um numero entre 0 e 5. tente adivinhar...')
print('-=-'*20)
jogador = int(input('Em que numero eu pensei? ')) #jogador tenta adivinhar
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print(f'GANHEI!Eu pensei no numero {computador} e não no {jogador}!')