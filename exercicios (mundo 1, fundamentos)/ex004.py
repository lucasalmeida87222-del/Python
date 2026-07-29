n = input('Diga algo: ')
print('Essa informação é alphanumérica?', n.isalnum()) # verifica se todos são alfanuméricos
print('É uma letra?' , n.isalpha()) #verifica se todos são letras do alfabeto
print('Essa informação esta dentro da tabela?', n.isascii()) # Verifica se todos os caracteres estão
# na tabela ASCII (0-127)
print('É um valor decimal?' , n.isdecimal())
print('É um digito?' , n.isdigit()) #Verifica se todos são dígitos
print('Pode ser usada?' , n.isidentifier()) #verifica se a string pode ser usada como nome de 
# variável/função/classe em Python.
print('A palavra é minuscula?' , n.islower()) #Verifica se todas as letras são minúsculas
print('A informação é numerica?' , n.isnumeric()) #Verifica se todos são numéricos
print('Pode ser impresso' , n.isprintable()) #Verifica se todos os caracteres podem ser impressos
print('Só tem espaços?' , n.isspace())
print('a informação é maiuscula?' , n.isupper()) #verifica se todas as letras são maiúsculas
