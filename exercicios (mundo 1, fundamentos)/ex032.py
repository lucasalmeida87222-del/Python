ano = int(input('Digite um ano: '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: 
   print(f'O ano de {ano} é bissexto')
else:
   print(f'O ano de {ano} não é bissexto')

#outro modo só que pegando o ano atual
from datetime import date # da biblioteca 'datetime' estou importando só o date
a = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if a == 0:
   a = date.today().year
if a % 4 == 0 and a % 100 != 0 or ano % 400 == 0:
   print(f'O ano {a} é Bissexto')
else:
   print(f'O ano {a} não é Bissexto') 