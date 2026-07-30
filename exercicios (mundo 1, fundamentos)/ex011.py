#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
#necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².
a = float(input('Altura da parede: '))
l = float(input('Largura da parede: '))
m2 = a * l #como calcular a area em metros quadrados.
r = m2 / 2

print(f'A parede possui {a} m² de altura, possui {l} m² de largura, sua area é de {m2} m², resultando em {r} l de tinta para pinta-la')

#Outra forma de fazer
a = float(input('Altura da parede: '))
l = float(input('Largura da parede: '))
m2 = a * l #como calcular a area em metros quadrados.
r = m2 / 2

print(f'Sua parede tem a dimensão de {l}x{a} e sua área é de {m2}m².')
print(f'Para pintar essa parede, você precisará de {r}l de tinta.')      