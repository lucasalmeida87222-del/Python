#Faça um programa que leia o sexo de uma pessoa, mas só aceita os valores 'M' ou 'F'.
#Caso esteja errado, peça a digitação novamente até ter um valor correto.
sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0] #aqui coloquei o 0 para pegar a primeira letra.
while sexo not in 'MF':
 sexo = str(input('\033[1;31m Dados invalidos\33[m. Por favor informe seu sexo: ')).strip().upper()[0]
print(f'\033[1;32m Sexo {sexo} registrado com sucesso\33[m.')

  