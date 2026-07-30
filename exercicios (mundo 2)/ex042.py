#Refaça o Desafio 035 dos triângulos, acrescentando o recurdo de mostrar que tipo de triângulo será formado:
n1 = float(input('Digite um comprimento: '))
n2 = float(input('Digite outro comprimento: '))
n3 = float(input('Digite outro comprimento: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Os segmentos acima PODEM FORMAR um triângulo!', end='')
    if n1 == n2 == n3:
        print('EQUILÁTERO!')
    elif n1 != n2 != n3 != n1:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')