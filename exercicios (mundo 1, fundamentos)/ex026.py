a = str(input('Digite uma frase: ')).strip().upper() #coloquei o .upper() para não ter problema com letra minuscula.
b = a.count('A')
c = a.find('A')+1 # o +1 é para contar a partir de 1
d = a.rfind('A')+1
input(f'Quantas vezes apareceu a letra A? {b}')
input(f'A primeira letra A apareceu na posição? {c}')
input(f'Em que posição ela aparece a ultima vez? {d}')

