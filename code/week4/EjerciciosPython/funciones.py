# Ejercicios
# 1. Hacer una funcion que se llame suma que reciba 2 parametros y retorne la adicion de dichos valores ejemplo
# 4, 5 ==> 9

import math
from random import randint, random


def suma (num1, num2):
    return f"La suma es: {num1+num2}"

print(suma(4,5))
print(suma(3,12.4))

# 2) hacer una funcion con el nombre que prefieran, que haga la division de dos valores, Importante el segundo termino no puede ser 0, en caso de que sea 0 debe mostrar un mensaje
# 15, 3 ==> 5
# 15, 0 ==> message: la div en 0 no esta definida 

def division(num1,num2):
    if num2 != 0:
        return (num1/num2)
    else:
        return "La división en 0 no está definida."

print(division(15,3))
print(division(15,0))


# Reto
# 1) un generador de contraseñas Recomendacion: (revisar lo que hemos visto de clases de string) parametros 1) sea mayor de 8 caracteres 2) debe contener letras y numeros 3) mayusculas y minusculas

carac_min = "abcdefghijklmnopqrstuvwxyz"
carac_may = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
carac_dig = "1234567890"
cant = randint(8,12)
print(cant)

def pass_gen():
    pwd = ""
    while len(pwd)<cant:
        pwd=pwd+
    return pwd

print(pass_gen())

# 2) un validador de contraseñas Recomendacion: (revisar lo que hemos visto de clases de string) parametros 1) sea mayor de 8 caracteres 2) debe contener letras y numeros 3) mayusculas y minusculas