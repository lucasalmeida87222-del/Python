D = float(input('Qual foi a distancia percorrida: '))
if D <= 200:
   print(f'O valor da sua passagem ficou em R${0.50*D}')
else:
   print(f'O valor da sua passagem ficou em R${0.45*D}')
   
#outro modo
d = float(input('Qual foi a distancia percorrida: '))
print(f'Você esta prestes a começar uma viagem de {d}km')
if d <= 200:
   preço = d*0.50
   print(f'O valor da sua passagem ficou em R${preço}')
else:
   preço = d * 0.45
   print(f'O valor da sua passagem ficou em R${preço}')

#modo simplificado
a = float(input('Qual foi a distancia percorrida: '))
print(f'Você esta prestes a começar uma viagem de {a}km')
valor = a * 0.50 if a <=200 else a * 0.45
print(f'O valor da sua passagem ficou em R${valor}')