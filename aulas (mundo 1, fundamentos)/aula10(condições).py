media = float(input('Qual foi a sua média? '))
if media >= 7:
    print('Aprovado')
else:
    print('Reprovado')
# de forma simplificada
print('Aprovado'if media>=7 else'Reprovado')

# outro exemplo
nome = str(input('Qual é o seu nome? ')).strip()
if nome == 'Lucas':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
print(f'Bom dia, {nome}!')

#outro exemplo
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print(f'A sua média foi {m}')
if m>= 6.0:
    print('Sua média foi boa! PARABÉNS!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')
# do modo simplificado
print('PARABÉNS' if m >=6 else 'Estude mais!')