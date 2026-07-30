#Refaça o Desafio 009, mostrando a tabuada de um numero que o usuário escolher, só que agora utilizando um laço for.
n = int(input('Digite um numero para ver a sua tabuada: '))
if n >=0:
    for c in range(1, 10+1):
        print(f'{n} x {c} = {n*c} ')