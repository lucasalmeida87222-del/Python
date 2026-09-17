#Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:  
#A) Quantas pessoas foram cadastradas. B) Uma listagem com as pessoas mais pesadas. C) Uma listagem com as pessoas mais leves.
temporario = []
principal = []
maior = menor = 0
while True:
    temporario.append(str(input('Nome: ')))
    temporario.append(float(input('Peso: ')))
    if len (principal) == 0: #Se não tem nada cadastrado ainda
        maior = menor = temporario [1] # no caso ai o primeiro peso cadastrado vai ser tanto o menor quanto maior.
    else:
        if temporario[1] > maior:
            maior = temporario[1]
        if temporario[1] < menor:
            menor = temporario[1]
    principal.append(temporario.copy()) #Criar uma copia da lista temporaria para a lista principal.
    temporario.clear() #limpar para cada loop depois que já é salvo na principal
    resposta = str(input('Quer continuar? [S/N] '))
    if resposta in 'Nn':
        break
print('-=-' * 20)
print(f'Ao todo, você cadastrou {len(principal)} pessoas.') #o len ali serviu para contar quantas sublistas tinham na lista.
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for p in principal:
    if p [1] == maior: #No caso a cada indice 1 em sublistas sendo o maior peso ele mostra o indice 0 de cada um que no caso é o nome.
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso cadastrado foi de {menor}Kg. Peso de ', end='')
for p in principal:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')
print()