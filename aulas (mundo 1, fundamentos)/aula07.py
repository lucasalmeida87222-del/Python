n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2 #di significa 'divisão inteira'
e = n1 ** n2
print(f'A soma é {s}, o produto é {m}, e a divisão é {d:.3f}',end='') 
# Ali na divisão eu coloquei dentro do {} :.3f para dizer que quero com três casas decimais depois do 
#ponto. E o f que esta junto porque é um numero flutuante 'float'. 
# eu coloquei ,end=' ' para que não tivesse a quebra de linha e ficasse tudo em uma linha só.

print(f'Divisão inteira {di} e potência {e}')

print(f'A soma é {s}, \n o produto é {m}, \n e a divisão é {d:.3f} \n', end=' ') 
# Em ambos coloquei \n para que fizesse a quebra de linha aonde foi colocado \n

print(f'Divisão inteira {di} \n e potência {e} \n')

print(f'A soma é {s}, o produto é {m}, e a divisão é {d:.3f}', end=' >>> ') 
# Dentro do '' que fica no end=' ' eu posso colocar caracteres.

print(f'Divisão inteira {di} \n e potência {e} \n')