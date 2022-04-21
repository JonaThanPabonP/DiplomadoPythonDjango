'''
3) sabes de geometria? seguro recuerdas algunas formulas del colegio/universidad 
y como aplicarlas. 
crea un programa para:
3.1) hallar el area de un circulo donde el radio sea un valor que ingresamos por input
3.2) hallar el area de un cuadrado donde uno de sus lados se un valor que ingresamos por input
3.3) hallar el volumen de una esfera, y un cubo con  los valore por cosola.
'''
import math

# 3.1
# Area circulo
r_c = int(input('Ingrese el valor del radio del circulo: '))
area_circulo = math.pi*(pow(r_c,2))
print(f'El area del circulo es {area_circulo} unidades cuadradas.')

# 3.2
# Area cuadrado
l = int(input('Ingrese el valor del lado de un cuadrado: '))
print(f'El area del cuadrado es {l**2} unidades cuadradas.')

# 3.3
# Volumen esfera

r = int(input('Ingrese el valor del radio de la esfera: '))
volumen_esfera = (4/3)*math.pi*(r**3)
print(f'El valor del volumen de la esfera es de {volumen_esfera} unidades cúbicas')

# Volumen del cubo
a = int(input('Ingrese el valor de una de las aristas del cubo: '))
volumen_cubo = a**3
print(f'El volumen del cubo es de {volumen_cubo} unidades cúbicas')