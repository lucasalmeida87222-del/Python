jogos = ['Mario', 'Sonic', 'GTA', 'Pacman']
jogos[1] = 'Zelda'
jogos.append('God of war')
jogos.insert(0,'Tetris')
jogos.remove ('Pacman')
print(jogos)
if 'GTA' in jogos:
    print('Jogo encontrado!')
else:
    print('Jogo não encontrado')

#Outro exemplo usando while
jogos = ['Mario', 'Zelda', 'GTA']
i = 0  # Precisa criar o contador

while i < len(jogos):  # Precisa checar o tamanho
    print(jogos[i], end = ' ')
    i += 1

# outro exemplo usando for
jogos = ['Tetris', 'Mario', 'Zelda', 'GTA', 'God of war']

for jogo in jogos:
    print(f'Eu gosto do jogo: {jogos}')
print('Fim da minha lista de jogos')

#outro exemplo usando for e enumerate
jogos = ['Tetris', 'Mario', 'Zelda', 'GTA', 'God of war']

for indice, jogo in enumerate(jogos):
    if jogo == 'GTA':  # Usa a variável 'jogo' que está mudando a cada volta
        print(f'Posição {indice}: GTA é meu favorito!')
    else:
        print(f'Posição {indice}: {jogo}')