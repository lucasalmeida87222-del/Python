#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastra-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
numero = []
for c in range(0,5):
    n = int(input('Digite um valor: '))
    if n not in numero:
        numero.append(n)
print(numero)