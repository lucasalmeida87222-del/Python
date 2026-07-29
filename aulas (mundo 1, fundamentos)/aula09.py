#Referente a fatiamento
frase = str('curso em video python')
print(frase[0:6])
print(frase[7:8]) 
print(frase[9:17]) 
print(frase[9:17:2]) #no caso ele vai do nove até 16 pulando de 1 em 1, resultando nas letras ‘vdop’
print(frase[:5]) # como não foi falado de onde ele começa, ele vai automaticamente começar do 0.
print(frase[15:]) #como não informei o final ele automaticamente vai até o final pulando de 2 em 2.
print(frase[9::3])

#Referente a analise
frase = str('curso em video python')
tamanho = len(frase) # len vem de 'length' comprimento.
a = frase.count('o') #count 'quantidade', ele me diz quantas letras 'o' tem.
b = frase.count('o', 0, 13) #nesse caso ele vai contar quantas letras 'o' tem de 0 a 12.
c = frase.find('deo') #find 'encontrar' ele vai me dizer em qual posição começou a palavra 'deo'.
d = frase.find('android') #quando a palavra não existe ele retorna -1.
e = 'curso' in frase #inside 'dentro' no caso pergunta se dentro da frase tem a palavra 'curso'.
print(f'{tamanho}, {a}, {b}, {c}, {e}')

#Referente a transformação
frase = str('  Curso em Video Python  ')
a = frase.replace('python', 'android') #onde tiver a palavra python ele vai substituir por 'android'.
b = frase.upper() #ele 'transforma' as letras minusculas em maiusculas. 
c = frase.lower() #ele 'transforma' as letras maiusculas em minusculas.
d = frase.capitalize() #ele vai deixar tudo em minusculos exeto a primeira letra que vai ficar em maiusculo.
e = frase.title() #analise quantas palavras tem e a primeira letra de cada palavra fica em maiuscula.
f = frase.strip() #remove caracteres em branco (ou caracteres específicos) do início e do final da string.
g = frase.rstrip() #remove caracteres em branco (ou caracteres específicos) do lado direito da string.
h = frase.lstrip() #remove caracteres em branco (ou caracteres específicos) do lado esquerdo da string.
print(f'{a}\n{b}\n{c}\n{d}\n{e}\n{f}\n{g}\n{h}')

#Referente a divisão
frase = str('Curso em Video python')
a = frase.split() #através dos espaços ele divide a string em palavras soltas dentro de uma lista.
b = frase.split(',') #Separando por vírgula, pois foi o que especifiquei dentro dos ().
c = frase.split('/') #Separando uma data.
d = frase.split('-', maxsplit=2) #Divide apenas nas duas primeiras ocorrências
print(f'{a}\n{b}\n{c}\n{d}')
#Nos casos acima ele corta através do que eu coloquei entre os (), como não tem nada ele não tem diferença visual.

#Referente a junção
frase = str('Curso em Video python')
a = '-'.join(frase) #Junta letra por letra com hífen.
print(f'{a}')