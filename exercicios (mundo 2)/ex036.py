casa = float(input('Qual o valor da casa que você deseja comprar? R$')) 
salario = float(input('Qual o valor do seu salario mensal? R$'))
anos = int(input('Em quantos anos pretende pagar a casa? '))
prestacao = casa / (anos * 12) 
minimo = salario * 30 / 100

print(f'Para pagar uma casa de R${casa:.2f} em {anos} anos', end='')
print(f'a prestação será de R${prestacao:.2f}')
if prestacao <= minimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')


    

