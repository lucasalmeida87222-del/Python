#for c in range (1, 10)
    #print(c)
#print('Fim')

c = 1 #Aqui eu coloco o valor no caso do 'c'
while c < 10: # aqui eu coloco a condição
    print(c ,end=' ') #aqui é para mostrar os valores de 'c'
    c += 1 #aqui é para que a cada volta ela vá somando + 1 
print('Fim')
#OBS: o while pode ser usado tanto quando sabe-se o limite e quando não se sabe o limite.

#Quando se se sabe o limite

n = 1 #aqui eu coloquei um valor inicial, para que ele inicie.
while n != 0:
    n = int(input('Digite um valor: '))
print('fim')

r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).upper()
print('Fim')

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0: # desse modo as condições abaixo não contabilizarão o '0' na resposta.
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Você digitou {par} números pares e {impar} números ímpares')