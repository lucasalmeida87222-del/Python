print('''Classificação de IMC (OMS - ADULTOS):
----------------------------------------------
[1] Abaixo de 18.5: ABAIXO DO PESO
[2] Entre 18.5 e 25: PESO IDEAL
[3] 25 até 30: SOBREPESO
[4] 30 até 40: OBESIDADE
[5] Acima de 40: OBESIDADE MÓRBIDA
---------------------------------------------''')
altura = float(input('Qual a sua altura? (m) '))
peso = float(input('Qual o seu peso? (kg) '))
imc = (peso / altura ** 2)
print(f' Seu IMC é: {imc:.1f}')
if imc < 18.5:
    print('Você esta ABAIXO do peso!')
elif  18.5 <= imc < 25: 
    print('Você esta no peso IDEAL!')
elif 25 <= imc < 30:
    print('Você esta SOBREPESO!')
elif 30 <= imc < 40:
    print('Você está OBESO!')
else:
    print('Você esta com OBESIDADE MÓRBIDA!')