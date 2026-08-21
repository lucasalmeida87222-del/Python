#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
#No final, mostre uma listagem de preços, organizando os dados em forma tabular.
produtos = ('Lápis',1.75,'Borracha',2.00,'Caderno',15.90,'Estojo',25.00,'Mochila',120.00,'Caneta',2.50,'Régua',4.50)

print('-' * 30)
print('Listagem de preços')
print('-' * 30)

for c in range(0, len(produtos), 2):
    produto = produtos [c]
    preco = produtos[c + 1]
    print(f'{produto:.<20} R$ {preco:>7.2f}')

    print('-' * 30)