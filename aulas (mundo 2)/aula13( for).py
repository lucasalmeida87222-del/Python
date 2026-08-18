for c in range (5, 0, -1): #aqui ele vai contar de trás pra frente, diminuindo -1 a cada vez.
    print(c)
for c in range(1,5): #Aqui ele ira contar 4x
    print('oi')
for c in range(0,5): #Aqui ele ira contar 5x
    print(c)
for c in range (0, 7, 2): #Aqui ele vai de 0 a 7 pulando de 2 em 2
    print(c)
# for c in range() no lugar do 'c' pode ser qualquer letra.

n = int(input('Digite um número: '))
for c in range (0, n+1): # Coloquei o +1 pq começando com 0 ele vai até um numero antes do que eu colocar.
    print(c)

i = int(input('Inicio: ' ))
f = int(input('Fim: '))
p = int(input('passo: '))
for c in range(i, f+1, p):
    print(c)
print('FIM')

for c in range(0,4):
    n = int(input('Digite um valor: '))
print('FIM')

s = 0
for c in range (0, 4):
    n = int(input('Digite um valor: '))
    s += n
print(f'O somatório de todos os valores foi {s}')