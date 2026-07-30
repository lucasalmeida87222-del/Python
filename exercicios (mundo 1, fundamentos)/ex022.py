#Crie um programa que leia o nome completo de uma pessoa e mostre:
nome = str(input('Qual o seu nome completo? ')).strip() #serve para resolver o problema dos espaços do começo e do fim da frase.
a = nome.upper()
b = nome.lower()
c = len(nome.replace(' ','')) #no caso replace substituiu o espaço por nenhum espaço.
d = nome.find(' ') #pede para encontrar o primeiro espaço. 

print(f'Analisando seu nome...')
print(f'Seu nome em maiúscula é {a}')
print(f'Seu nome em minúscula é {b}')
print(f'Seu nome tem ao todo {c} letras')
print(f'Seu primeiro nome tem {d} letras')

#outro modo 
nome = str(input('Qual o seu nome completo? ')).strip() #serve para resolver o problema dos espaços do começo e do fim da frase.

print(f'Analisando seu nome...')
print(f'Seu nome em maiúscula é {nome.upper()}')
print(f'Seu nome em minúscula é {nome.lower()}')
print(f'Seu nome tem ao todo {len(nome.replace(' ',''))} letras')
#print(f'Seu primeiro nome tem {nome.find(' ')} letras')
#outro modo de fazer o ultimo print
separa = nome.split()
print(f'Seu primeiro nome é {separa[0]} e ele tem {len(separa[0])} letras')