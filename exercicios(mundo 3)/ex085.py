#Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

lista = []
par = []
impar = []
final = []

for c in range(0,7):
    lista.append(int(input('Digite um valor: ')))
for c in lista:
    if c % 2 == 0:
        par.append(c)
        par.sort()
    else:
        impar.append(c)
        impar.sort()
final.append(par)
final.append(impar)
print(final)
#----------------------------------------------------------------------------------------------------------------------------------------
#VERSÃO OTIMIZADA!
# Lista única com duas sublistas internas: [0] para pares, [1] para ímpares
num = [[], []]

for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor: '))
    
    if valor % 2 == 0:
        num[0].append(valor)  # Adiciona na sublista de pares
    else:
        num[1].append(valor)  # Adiciona na sublista de ímpares

# Ordena cada sublista individualmente
num[0].sort()
num[1].sort()

print('-=' * 30)
print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valores ímpares digitados foram: {num[1]}')
