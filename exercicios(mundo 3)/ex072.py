#Crie um programa que tenha tupla totalmente preenchida com uma contagem por extenso de zero até vinte.
#Seu programa deverá ler um numero pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
n = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    numero = int(input('Digite um numero entre 0 e 20: '))
    if 0 <= numero <= 20:
        break
    print('Tente novamente. ', end= '')

print(f'Você digitou o numero {n[numero]}')
