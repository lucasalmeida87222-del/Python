#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.
n = int(input('Digite um numero: '))
u = (n%10)
d = (n//10)%10
c = (n//100)%10
m = (n//1000)%10
print(f'Milhar: {m}\n centena: {c}\n Dezena: {d}\n Unidade: {u}')



