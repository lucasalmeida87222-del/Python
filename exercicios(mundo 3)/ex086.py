#Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
#Os dois for abaixo são para colocar os valores dentro da matriz.
for linha in range(0,3):
    for coluna in range (0,3):
        matriz [linha] [coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
print('-=-' * 20)
#Os for abaixo são para mostrar os valores gerados acima na tela.
for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[{matriz [linha] [coluna]:^5}]', end='')
    print() #Desse modo toda vez que ele terminar as coluna ele quebra uma linha.