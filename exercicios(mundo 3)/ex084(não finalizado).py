#Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:  
#A) Quantas pessoas foram cadastradas. B) Uma listagem com as pessoas mais pesadas. C) Uma listagem com as pessoas mais leves.

lista = [] #Excluida
dado = []
quantidade = []
pesado = []
leve = []
m = l = q = 0

while True: # pegar os dados necessarios para a lista.
    lista.append(str(input('Qual seu nome: ')))
    lista.append(int(input('Qual seu peso: ')))
    continua = str(input('Deseja continuar[S/N]? ')).upper()
    dado.append(lista.copy())
    lista.clear()
    if continua != 'S' and continua != 'N':
        print('Opção incorreta.', end = ' ')
        continuar = str(input('Deseja continuar[S/N]? ')).upper()    
    elif continua == 'N': 
        break
for p in dado: 
    if p [1]:
        q +=1
print(f'Temos {q} pessoa(s) cadastradas.')
#até o momento o código só resolve a parte da letra A.




