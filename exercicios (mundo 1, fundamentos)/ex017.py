import math 
cos = float(input('Digite o valor do cateto adjacente: '))
sin = float(input('Digite o valor do cateto oposto: '))
tan = math.hypot(cos, sin)
print(f'O cateto adjacente é {cos}, o cateto oposto é {sin}, a hypotenusa vai ser {tan:.2f}')

import math
sin = float(input('Digite o valor do cateto oposto: '))
tan = float(input('Digite o valor da hipotenusa: '))
cos = sin / math.tan(math.radians(tan)) 
#math.radians() converte o ângulo de graus para radianos antes de passá-lo para a função trigonométrica.
print(f'O cateto oposto é {sin}, o hipotenusa é {tan}, o cateto adjacente vai ser {cos:.2f}')