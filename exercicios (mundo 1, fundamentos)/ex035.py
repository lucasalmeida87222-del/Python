print('-='*20)
print('Analisador de triangulo')
n1 = float(input('Digite um comprimento: '))
n2 = float(input('Digite outro comprimento: '))
n3 = float(input('Digite outro comprimento: '))
if (n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2):
    print('Com o valor das retas informadas elas geram um triangulo')
else:
    print('Com o valor das retas informadas elas não geram um triangulo')

#outro modo
n1 = float(input('Digite um comprimento: '))
n2 = float(input('Digite outro comprimento: '))
n3 = float(input('Digite outro comprimento: '))
if n2 + n3 > n1:
    print('Com o valor das retas informadas elas geram um triangulo')
else:
    print('Com o valor das retas informadas elas não geram um triangulo')