#Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

lista = []
par = []
impar = []

for c in range(0,7):
    lista.append(int(input('Digite um valor: ')))
par.append(lista.copy())
print(par)