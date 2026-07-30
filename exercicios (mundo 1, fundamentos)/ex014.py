#Desenvolva um conversor de temperatura.
num = float(input('Digite um valor: '))
graus = 5/9*(num-32)
print(f'O valor {num},  de fahrenheit para celsius fica {graus:.0f}\u00B0C') #\u00B0C é para colocar o simbolo.

num = float(input('Digite um valor: '))
graus = num-273
print(f'O valor {num}, de kelvin para celsius fica {graus:.0f}\u00B0C') 

num = float(input('Digite um valor: '))
graus = 5/9*(num-491.67)
print(f'O valor {num}, de rankine para celsius fica {graus:.0f}\u00B0C')
