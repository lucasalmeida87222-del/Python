#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

lista = []

for c in range (0,5):
    n = int(input('Digite um valor: '))
    lista.append(n)
a = min(lista)
b = max(lista)
pos_maior = lista.index(b)
pos_menor = lista.index(a)
print(f'Os numeros digitados foram{lista}!',end=' ')
print(f'O menor valor é {a} posição {pos_menor} e o maior valor é {b} posição {pos_maior}!')
