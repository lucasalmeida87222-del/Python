n = int(input('Digite um numero '))
a = n * 1
b = n * 2
c = n * 3
d = n * 4
e = n * 5
f = n * 6
g = n * 7
h = n * 8
i = n * 9
j = n * 10

print(f'O numero {n} e sua tabuada: \n {a} \n {b} \n {c} \n {d} \n {e} \n {f} \n {g} \n {h} \n {i} \n {j}')

#outra forma de fazer
n = int(input('Digite um numero '))

print(f'O numero {n} e sua tabuada: \n {n*1} \n {n*2} \n {n*3} \n {n*4} \n {n*5} \n {n*6} \n {n*7} \n {n*8} \n {n*9} \n {n*10}' ,end=' ')

#uma forma melhor de fazer esse exercicio
n = int(input('Digite um numero para ver sua tabuada '))

print(f' {n} x {1:2} = {n*1}')
print(f' {n} x {2:2} = {n*2}')
print(f' {n} x {3:2} = {n*3}')
print(f' {n} x {4:2} = {n*4}')
print(f' {n} x {5:2} = {n*5}')
print(f' {n} x {6:2} = {n*6}')
print(f' {n} x {7:2} = {n*7}')
print(f' {n} x {8:2} = {n*8}')
print(f' {n} x {9:2} = {n*9}')
print(f' {n} x {10:2} = {n*10}')
