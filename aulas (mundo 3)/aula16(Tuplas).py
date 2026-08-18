#1
lanche = ('Hambúrguer', 'Suco', 'pizza', 'pudim')
print(lanche)
print (lanche[0])
print(lanche[0:3])
print(lanche[:4])
print(lanche[-1:])
print(lanche[::])
print('FIM!')
#---------------------------------------------------------------------------------------------------------------------
#2
lanche = ('Hambúrguer', 'Suco', 'pizza', 'pudim')
for comida in lanche:
    print(f'Eu vou comer {comida}')
print("Comi pra caramba!")
print('FIM!')
#----------------------------------------------------------------------------------------------------------------------
#3
lanche = ('Hambúrguer', 'Suco', 'pizza', 'pudim', 'Batata frita')
print(len(lanche))
print('FIM!')
#----------------------------------------------------------------------------------------------------------------------
#4
lanche = ('Hambúrguer', 'Suco', 'pizza', 'pudim', 'Batata frita')
for cont in range(0, len(lanche)): # tanto esse quanto o for comida in lanche dão o mesmo resultado, porém tera ocasiões que somente uma das duas ira funcionar. 
    print(f'{cont}')
    print(f'{lanche[cont]}') #Aqui ele faz todos pois o cont começa em 0 e vai até 5.
print('FIM!')
#------------------------------------------------------------------------------------------------------------------------
#5
lanche = ('Hambúrguer', 'Suco', 'pizza', 'pudim', 'Batata frita')
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
print('FIM!')
#-------------------------------------------------------------------------------------------------------------------------
#6
#Esse funciona igual o exemplo #5
lanche = ('Hambúrguer', 'Suco', 'pizza', 'pudim', 'Batata frita')
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('FIM!')
#-------------------------------------------------------------------------------------------------------------------------
#7
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata frita')
print(sorted(lanche)) #'sorted' organiza em ordem alfabética.
print('FIM!')
#OBS: No Python, a ordenação de texto segue a tabela de caracteres (ASCII/Unicode). Nela, todas as letras maiúsculas vêm antes de qualquer letra minúscula.
#---------------------------------------------------------------------------------------------------------------------------
#8
a = (2,5,4)
b = (5,8,1,2)
c = a + b
print(c) #nesse caso ele vai mostrar a sequencia de 'a' e a de 'b' todas juntas.
print(len(c)) #vai mostrar quantos numeros eu tenho, no caso 7 pois nesse caso não começa com 0.
print(c.count(5))#Ele vai me dizer quantas vezes o numero 5 aparece, no caso 2x.
print(c.index(8)) #ele vai me mostrar em que posição esta o 8, como a contagem começa com 0 nesse caso o 8 esta no posição 4.
print(c.index(5,2))#Aqui ele pede pra mostrar em que posição esta o 5 começando da posição 2, como tem dois 5 o segundo 5 esta na posição 3.
#---------------------------------------------------------------------------------------------------------------------------------
#9
pessoa = ('Lucas',39, 'M', 98)#Eu posso ter tipos de dados diferentes dentro das minhas tuplas.
print(pessoa)
#---------------------------------------------------------------------------------------------------------------------------------
#10
pessoa = ('Lucas',39, 'M', 98)
del(pessoa) #como logo em seguida da tupla pessoa eu usei del(pessoa) ele apagou a tupla e vai aparecer um erro na execução.
print(pessoa)