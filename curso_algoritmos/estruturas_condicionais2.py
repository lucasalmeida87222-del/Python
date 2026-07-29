# Condição aninhada
dinheiro = float(input('Quanto de dinheiro você possui? '))
if dinheiro >= 10000:
    print('Partiu Disney.')
elif dinheiro >= 5000 and dinheiro < 10000:
    print('Visitar Familia.')
else:
    print('#Chateado')
#--------------------------------------------------------------------------------------------------------------
n1 = float(input('Nota1: '))
n2 = float(input('Nota2: '))
media = (n1 + n2) / 2
print(f'A média do aluno foi {media}')
if media >= 6:
    print('Aluno APROVADO')
elif media >= 5 and media <= 5.9:
    print('Aluno em RECUPERAÇÃO')
else:
    print('Aluno REPROVADO')
#--------------------------------------------------------------------------------------------------------------
print('-=-' * 20)
print('CALCULO IMC')
print('-=-' * 20)
peso = float(input('Qual seu peso? '))
altura = float(input('Qual sua altura? '))
imc = peso / (altura**2)
print(f'Seu IMC é de {imc:.2f}')
if imc < 17:
    print('Você esta muito abaixo do peso.')
elif imc > 17 and imc < 18.5:
    print('Você esta abaixo do peso.')
elif imc >= 18.5 and imc <= 25:
    print('Você esta no peso Ideal.')
elif imc >= 25 and imc <= 30:
    print('Você esta sobrepeso.')
elif imc >= 30 and imc <= 35:
    print('Você esta obeso.')
elif imc >= 35 and imc <= 40:
    print('Você tem obesidade severa.')
else:
    print('Você tem obesidade morbida')
#-----------------------------------------------------------------------------------------------------------------
# Escolha caso
print('-=-' * 20)
print('CRIANÇA ESPERANÇA')
print('-=-' * 20)
print('Muito obrigado por ajudar')
print('''[1] para doar R$10
[2] para doar R$25
[3] para doar R$50
[4] para doar outros valores
[5] para cancelar''')

doação = int(input('Digite o número correspondente à doação desejada: '))

# Substituindo a estrutura if/elif pelo match/case
match doação:
    case 1:
        print('Você doou R$10')
    case 2:
        print('Você doou R$25')
    case 3:
        print('Você doou R$50')
    case 4:
        valor = int(input('Qual valor você deseja doar? '))
        print(f'Você doou R${valor}')
    case 5:
        print('Doação cancelada.')
    case _:
        # O "_" substitui o "else", tratando qualquer valor que não seja de 1 a 5
        print('Opção inválida')

print('MUITO OBRIGADO!')