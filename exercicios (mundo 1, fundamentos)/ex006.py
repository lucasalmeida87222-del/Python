#Crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada.
numero = int(input('Digite um numero '))
d = numero*2
t = numero*3
ra = numero**(1/2)

print(f'{numero}, o dobro é {d}, o triplo é {t}, e a raiz quadrada é {ra:.3f}')

#colocando cada resultado em uma linha

numero = int(input('Digite um numero '))
d = numero*2
t = numero*3
ra = numero**(1/2)

print(f'O dobro de {numero} vale {d} \nO triplo de {numero} vale {t} \nE a raiz quadrada de {numero} vale {ra:.3f}')