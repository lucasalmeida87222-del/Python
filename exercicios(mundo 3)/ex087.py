#Aprimore o desafio anterior, mostrando no final: A) A soma de todos os valores pares digitados. B) A soma dos valores da terceira coluna. C) O maior valor da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = maior = scoluna = 0
#Os dois for abaixo são para colocar os valores dentro da matriz.
for linha in range(0,3):
    for coluna in range (0,3):
        matriz [linha] [coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
print('-=-' * 20)
#Os for abaixo são para mostrar os valores gerados acima na tela.
for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[{matriz [linha] [coluna]:^5}]', end='')
        if matriz[linha] [coluna] % 2 == 0:
            par += matriz[linha] [coluna]
    print() #Desse modo toda vez que ele terminar as coluna ele quebra uma linha.
print('-=-' * 20)
print(f'A soma dos valores pares é {par}.')
for linha in range (0,3): #Estou fazendo um for só para linha pq ela é variavel e a coluna é fixa no caso [2].
    scoluna += matriz [linha] [2] # o [2] como falei acima é a coluna fixa.
print(f'A soma dos valores da terceira coluna é {scoluna}.')
for coluna in range(0, 3): #Estou fazendo um for só para coluna pq ela é variavel e a linha é fixa no caso [1].
    if coluna == 0:
        maior = matriz [1] [coluna]
    elif matriz [1] [coluna] > maior:
        maior = matriz [1] [coluna]
print(f'O maior valor da segunda linha é {maior}.')