# 
# ## Sumar los recibos de mi hogar
'''
Escribir un codigo en python para sumar los gastos de consumo de mi casa
al final imprima cuanto es el valor total de dichos gastos
ejemplo:
agua = 135000
luz = 200000
gas = 40000
telefono_internet = 100000
administracion = 150000
...
total = agua + luz + .... 

si en mi casa viven n personas, 
cuanto es el gasto por cada uno?
(usar input para ingresar los valores)
'''

agua = int(input('Ingrese el valor del recibo del agua: '))
luz = int(input('Ingrese el valor del recibo de la luz: '))
gas = int(input('Ingrese el valor del recibo del gas: '))
telefono_internet = int(input('Ingrese el valor del recibo del telefono y el internet: '))
administracion = int(input('Ingrese el valor de la administracion: '))

total = agua + luz + gas + telefono_internet + administracion

cantidad_personas = int(input('Cuantas personas viven en casa: '))

gasto_individual = total/cantidad_personas

print(f'El total de gastos de consumo en mi casa es de ${total}, lo que da un promedio por persona de ${gasto_individual}')