print('1 para binario\n2 para octal\n3 para hexadecimal')
numero = int(input('Digite um numero: '))
conversor = int(input('escolha entre os numeros 1, 2 e 3 e aperte enter para converter: '))
bina = bin (numero)
octa = oct (numero)
hexa = hex(numero)
if conversor == 1:
    print(f'A conversão do numero {numero} para binario ficou {bina [2:]}')
elif conversor == 2:
    print(f'A conversão do numero {numero} para octal ficou {octa[2:]}')
elif conversor == 3:
    print(f'A conversão do numero {numero} para hexadecimal ficou {hexa[2:]}')

#Um método melhor para resolver esse exercicio

num = int(input('Digite um numero inteiro: '))
print('''Escolha uma das basses para conversão:
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''') #coloquei ''' ''' de cada lado para poder escrever embaixo.
opção = int(input('Sua opção: '))
if opção == 1:
    print(f'{num} convertido para BINÁRIO é igual a {bin(num)[2:]}')
elif opção == 2:
    print(f'{num} convertido para OCTAL é igual a {oct(num)[2:]}')
elif opção == 3:
    print(f'{num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}')
else:
    print('Opção inválida. Tente novamente.')
