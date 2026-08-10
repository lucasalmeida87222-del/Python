#Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais ulguns termos.
#O programa encerra quando ele disser que quer mostrar 0 termos.
print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Digite o primeiro termo de uma PA: '))
razao = int(input('Digite a razao de uma PA: '))
termo = primeiro 
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo} ', end=' ')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'progressão finalizada com {total} termos mostrados.')