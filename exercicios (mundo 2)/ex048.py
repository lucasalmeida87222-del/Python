soma = 0
cont = 0
for c in range(1,501):
    if c % 2 != 0 and c % 3 == 0:
        cont = cont + 1
        soma = soma + c 
print(f'\nA soma de todos os {cont} valores solicitados é {soma}', end = '')