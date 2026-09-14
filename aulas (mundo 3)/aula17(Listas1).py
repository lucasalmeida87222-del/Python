#1 Troca o elemento da lista.
num = [2,5,9,1]
num[2] = 3
print(num)
#----------------------------------------------------------------------------------------------------------------------------------------
#2 Adiciona um elemento a lista.
num = [2,5,9,1]
num.append(7)
print(num)
#----------------------------------------------------------------------------------------------------------------------------------------
#3 Coloca a lista ordenada do menor para o maior.
num = [2,5,9,1]
num.sort()
print(num)
#----------------------------------------------------------------------------------------------------------------------------------------
#4 Coloca a lista ordenada do maior para o menor.
num = [2,5,9,1]
num.sort(reverse=True)
print(num)
#----------------------------------------------------------------------------------------------------------------------------------------
#5 Conta quantos elementos tem na lista.
num = [2,5,9,1]
print(f'Essa lista tem {len(num)} elementos.')
#----------------------------------------------------------------------------------------------------------------------------------------
#6 Insere o numero 0 na posição 2.
num = [2,5,9,1]
num.insert(2,0)
print(num)
#----------------------------------------------------------------------------------------------------------------------------------------
#7 Elimina o ultimo elemento devido a não ter colocado um parametro entre ().
num = [2,5,9,1,2]
num.pop()
print(num)
#----------------------------------------------------------------------------------------------------------------------------------------
#8 Elimina o numero que vc pediu para remover. porém se existir dois numeros iguais ele só remove o primeiro que aparece.
num = [2,5,9,1,2]
num.remove(2)
print(num)
#----------------------------------------------------------------------------------------------------------------------------------------
#9 Remover um numero de uma lista, porém se esse numero não existir ele não faz nada, desse modo não dando erro no programa.
num = [2,5,9,1,2]
if 4 in num:
    num.remove(4)
else:
    print('Não achei o numero 4.')
#----------------------------------------------------------------------------------------------------------------------------------------
#10 Criar uma lista mais bonita.
valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for v in valores:
    print(f'{v}...')
#----------------------------------------------------------------------------------------------------------------------------------------
#11 Caso eu queira além do valor o indice(chaves).
valores = []
valores.append(8)
valores.append(10)
valores.append(20)

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')
#----------------------------------------------------------------------------------------------------------------------------------------
#12 Ler valores no teclado e incluir na lista.
valores = []
for cont in range(0,5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')
#----------------------------------------------------------------------------------------------------------------------------------------
#13 Fazer uma ligação entre as listas.
a = [2, 3, 4, 7]
b = a
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
#----------------------------------------------------------------------------------------------------------------------------------------
#14 Fazer a cópia de uma lista, desse modo se mudar algo na lista do b não ira alterar o da lista a junto.
a = [2, 3, 4, 7]
b = a[:] #recebe todos os elementos de a
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')