#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo
#que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
vel = float(input('A qual velocidade o carro estava? '))
if vel > 80:
    x = (vel - 80)*7
    print(f'você foi multado!, o valor da sua multa é de R${x}')

else:
    print('Você esta dentro do limite de velocidade!')

#outro modo
velocidade = float(input('Qual a velocidade atual do carro? '))
if velocidade > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h')
    multa = (velocidade-80)*7
    print(f'Você deve pagar uma multa de R${multa:.2f}! ')
print('Tenha um bom dia! Dirija com segurança!')

#tudo do lado 'esquerdo' sempre se repete.
# usando só a condição 'if' usamos a condição simples.