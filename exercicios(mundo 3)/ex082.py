#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
a = []
b = []
c = []

for v in range(0,5):
    n = int(input('Digite um valor: '))
    a.append(n)
    if n % 2 == 0:
        b.append(n)
    elif n % 2 !=0:
        c.append(n)
print(a)
print(b)
print(c)