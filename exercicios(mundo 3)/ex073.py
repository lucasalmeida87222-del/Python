#Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato Brasileiro de futebol, na ordem de colocação. Depois mostre: A) Apenas os 5 primeiros colocados.
#B)Os últimos 4 colocados da tabela.
#C) Uma lista com os times em ordem alfabética.
#D) Em que posição na tabela está o time do grêmio.
tabela = ('Botafogo','Palmeiras','Flamengo','Fortaleza','Internacional','São Paulo','Corinthians','Bahia','Cruzeiro','Vasco','Vitória','Atlético-MG','Fluminense','Grêmio','Juventude','Red Bull Bragantino','Athletico-PR','Criciúma','Atlético-GO','Cuiabá')
print('-=' * 84)
print(f'Lista de times do Brasileirão: {tabela}')
print('-=' * 84)
print(f'Os 5 primeiros são {tabela[0:5]}')
print('-=' * 84)
print(f'Os 4 últimos são {tabela[-4:]}')
print('-=' * 84)
print(f'Times em ordem alfabética: {sorted(tabela)}')
print('-=' * 84)
print(f'O Grêmio está na {tabela.index('Grêmio')+1} posição')