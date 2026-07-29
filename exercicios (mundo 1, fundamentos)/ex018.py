import math
n = float(input('Informe um ângulo: '))

rad = math.radians(n) #Converta o ângulo para radianos (Passo Obrigatório!)
sin = math.sin(rad) 
cos = math.cos(rad)
tan = math.tan(rad)

print(f'Seno de {n} é igual a {sin:.2f}')
print(f'Cosseno de {n} é igual a {cos:.2f}')
print(f'Tangente de {n} é igual a {tan:.2f}')

#outra maneira

n = float(input('Informe um ângulo: '))

sin = math.sin(math.radians(n)) 
cos = math.cos(math.radians(n))
tan = math.tan(math.radians(n))

print(f'Seno de {n} é igual a {sin:.2f}')
print(f'Cosseno de {n} é igual a {cos:.2f}')
print(f'Tangente de {n} é igual a {tan:.2f}')