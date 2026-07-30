#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e
#condição de pagamento:
preço = float(input('Qual o valor do produto? R$'))
print('''Métodos de pagamento
[1] Á vista dinheiro/cheque: 10%, de desconto
[2] Á vista no cartão: 5%, de desconto
[3] Em até 2x no cartão: preço normal
[4] 3x ou mais no cartão: 20%, de juros
---------------------------------------------------''')
pagamento = int(input('Escolha o método de pagamento desejado: '))
pix = preço * (1 - 10 / 100)
vista = preço * (1 - 5 / 100)
parcelado = preço * (1 + 20 / 100)

if pagamento == 1:
    print(f'O valor total ficou em R${pix:.2f}')
elif pagamento == 2:
    print(f'O valor total ficou em R${vista:.2f} ')
elif pagamento == 3:
    print(f'O valor total ficou em R${preço:.2f}')
elif pagamento == 4:
    print(f'O valor total ficou em R${parcelado:.2f}')
else:
    print('Escolha um método de pagamento válido!')

#método mais profissional
#pagamento = int(input('Escolha o método de pagamento desejado: '))

#if pagamento == 1:
    #valor = preco * 0.90
    #print(f'O valor total ficou em R${valor:.2f}')
#elif pagamento == 2:
    #valor = preco * 0.95
    #print(f'O valor total ficou em R${valor:.2f}')
#elif pagamento == 3:
    #print(f'O valor total ficou em R${preco:.2f}')
#elif pagamento == 4:
    #valor = preco * 1.20
    #print(f'O valor total ficou em R${valor:.2f}')
#else:
    #print('Escolha um método de pagamento válido!')