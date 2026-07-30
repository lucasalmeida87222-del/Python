#Crie um programa que informe qual o valor deve ser pago pelo aluguel do carro.
dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
pago = (dias * 60) + (km * 0.15)
print(f'O total a pagar é de R${pago:.2f}')
