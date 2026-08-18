n = float(input('Digite um valor: '))
print (n)
n = float(input('Digite um valor: '))
print (type(n))

n1 = bool(input('Digite um valor: '))
print (n1)
n1 = bool(input('Digite um valor: '))
print (type(n1))

n2 = str(input('Digite um valor: '))
print (n2)
n2 = str(input('Digite um valor: '))
print (type(n2))

n = input('Digite algo: ')
print(n.isnumeric()) #é um método das strings que verifica se todos os caracteres são numéricos.

n = input('Digite algo: ')
print(n.isalpha()) #é um método das strings que verifica se todos os caracteres são letras do alfabeto.

n = input('Digite algo: ')
print(n.isalnum()) #é um método das strings que verifica se todos os caracteres são 
#alfanuméricos (letras OU números).

n = input('Digite algo: ')
print(n.isupper()) #é um método das strings que verifica se todos os caracteres que podem ser 
#maiúsculos são maiúsculos.

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1+n2
print(f'A soma entre {n1} e {n2} vale {s}!')
# print(f"{x} + {y} = {r}") cada variável no seu lugar