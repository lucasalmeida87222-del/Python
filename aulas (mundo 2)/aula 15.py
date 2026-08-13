n = s = 0
while True: #Aqui ele vai repitir infinitamente.
    n = int(input('Digite um número: '))
    if n == 999:
        break #Nessa condição que fiz ele vai parar o programa assim que digitar 999 e vai sair do loop.
    s += n #Se não for 999 ele ira somar.
print(f'A soma vale {s}') #Depois de sair do loop ele vai mostrar a soma.
#------------------------------------------------------------------------------------------------------------