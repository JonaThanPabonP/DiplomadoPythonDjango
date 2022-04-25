'''
1. Hacer 3 saludos personalizados(usando variables con .format) que sean uno para cada instante del dia, buenos dias, buenas tardes, buenas noches.
2. Contar cuantas veces se repite una palabra en una cancion.
3. Escribir el nombre completo y separar por espacios, sacar el segundo nombre y el ultimo apellido.
4. Para entradas de estilo snake_case convertir la palabra en cammelCase.
'''

# Ejercicio 1
name = input('Ingrese su nombre: ')
print("Buenos dias {}".format(name))
print("Buenas tardes {}".format(name))
print("Buenas noches {}".format(name))


# Ejercicio 2
word = input('Ingrese la palabra a contar: ')
song = input('Ingrese la cancion: ')
song = song.lower()
print(song.count(word.lower()))

# Ejercicio 3
full_name = input('Ingrese su nombre completo: ')
name_splited = full_name.split(" ")
print(f'Segundo nombre {name_splited[1]}')
print(f'Segundo apellido {name_splited[-1]}')

# Ejercicio 4
snake = input('Ingrese una palabra en snake_case: ')
snake_splited = snake.split("_")
# ["mi","variable"]
cammel = snake_splited[0]+"".join(w.capitalize() for w in snake_splited[1:])
# "mi"+"Variable"
print(cammel)
# miVariable

