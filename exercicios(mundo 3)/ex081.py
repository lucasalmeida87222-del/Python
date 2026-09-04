#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre: A) Quantos números foram digitados.
#B) A lista de valores ordenada de forma decrescente. C) Se o valor 5 foi digitado e está ou não na lista.
numero = []

for c in range(1,6):
    n = int(input('Digite um valor: '))
    numero.append(n)
numero.sort(reverse = True)
print(f'Foram digitados {len(numero)} numeros')
print(f'Os numeros digitados em forma decrescente fica: {numero}')
if 5 in numero:
    print(f' o numero 5 foi digitado e esta na lista {numero}!')
else:
    print(f'O numero 5 ainda não esta na lista {numero}!')