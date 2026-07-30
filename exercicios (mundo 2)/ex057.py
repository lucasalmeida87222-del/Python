#Faça um programa que leia o sexo de uma pessoa, mas só aceita os valores 'M' ou 'F'.
#Caso esteja errado, peça a digitação novamente até ter um valor correto.
sexo = str(input('Digite M para o gênero masculino e F para o feminimo: ')).upper()
while sexo != 'M' and sexo != 'F':
 print('Valor inválido!')
 sexo = str(input('Digite novamente: ')).upper() 
if sexo == 'M':
  print('Seu gênero é Masculino!')
if sexo == 'F':
 print('Seu gênero é feminino!')
  