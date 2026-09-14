#1 cadastra duas pessoas diferentes em uma mesma lista, reaproveitando a variável teste sem perder os dados anteriores.
teste = []
teste.append('Gustavo') #Adiciona o texto 'Gustavo' na posição 0 da lista teste.
teste.append(40) #Adiciona o número 40 na posição 1 da lista teste.

galera = []
galera.append(teste.copy()) #Cria uma cópia independente do conteúdo de teste naquele exato momento (['Gustavo', 40]) e insere esse bloco dentro da lista galera.

teste[0] = 'Maria' #Vai até a lista teste e substitui o valor da posição 0 ('Gustavo') por 'Maria'.
teste[1] = 22 #Vai até a lista teste e substitui o valor da posição 1 (40) por 22. (Estado atual de teste: ['Maria', 22])
galera.append(teste.copy()) #Tira uma nova "foto" de como a lista teste está agora (['Maria', 22]) e adiciona essa nova lista como o segundo item de galera. (Estado final de galera: [['Gustavo', 40], ['Maria', 22]]).
print(galera)
print('FIM')
print('-=-'*20)
#----------------------------------------------------------------------------------------------------------------------------------------
#2
galera = [['joão',19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera[0]) #Retorna [joão, 19].
print(galera[2] [1]) #Retorna [13] que se refere ao Joaquim.
print('FIM')
print('-=-'*20)
#----------------------------------------------------------------------------------------------------------------------------------------
#3
galera = [['joão',19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
for pessoa in galera:
    print(pessoa) # a cada lista dentro da lista vai aparecer uma embaixo da outra. Pois a cada loop ele mostra uma lista por vez.
print('FIM')
print('-=-'*20)
#----------------------------------------------------------------------------------------------------------------------------------------
#4
galera = [['joão',19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
for pessoa in galera:
    print(pessoa[1]) # a cada lista dentro da lista vai aparecer uma embaixo da outra porém agora indice [1]. Pois a cada loop ele mostra uma lista por vez.
print('FIM')
print('-=-'*20)
#----------------------------------------------------------------------------------------------------------------------------------------
#5 Modo  3 e 4 só que formatado.
galera = [['joão',19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
for pessoa in galera:
    print(f'{pessoa[0]} tem {pessoa [1]} anos de idade.')
print('FIM')
print('-=-'*20)
#----------------------------------------------------------------------------------------------------------------------------------------
#6
galera = []
dado = [] # Uma lista temporaria.
for c in range (0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado.copy()) #Eu coloco o resultado da lista dado dentro da lista galera.
    dado.clear() #Aqui eu excluo a lista dado pois os dados que eu queria pegar já estão na lista galera.
print(galera)
print('FIM')
print('-=-'*20)
#----------------------------------------------------------------------------------------------------------------------------------------
#7 Mostrar pessoas que tem mais de 20 anos.
galera = []
dado = [] # Uma lista temporaria.
totmai = totmen = 0
for c in range (0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado.copy()) #Eu coloco o resultado da lista dado dentro da lista galera.
    dado.clear() #Aqui eu excluo a lista dado pois os dados que eu queria pegar já estão na lista galera.
for p in galera:
    if p [1] >= 21:
       print(f'{p[0]} é maior de idade.') 
       totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade.')
print('FIM')
print('-=-'*20)