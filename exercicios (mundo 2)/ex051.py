termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = termo + (10 - 1) * razao
for c in range(termo , decimo + razao, razao): # aqui no caso foi do primeiro 'termo', até decimo, pulando de razao em razao
    print(f'{c}', end = ' → ')
print('ACABOU')
