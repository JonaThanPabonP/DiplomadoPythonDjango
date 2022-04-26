lista = [
    {
        "nombre": "juanito",
        "promedio": 3.9
    },
    {
        "nombre": "pepita",
        "promedio": 2.4
    },
    {
        "nombre": "carlitos", 
        "promedio": 2.7
    },
    {
        "nombre": "martha", 
        "promedio": 4.2
    },
]

# Determinar:
# -	Cual tiene el promedio más alto
# -	Quien tiene el nombre más largo 
# -	Cual tiene el promedio más bajo

alto, bajo, nombre, prom_alto, prom_bajo, nombre_largo = 0, 0, 0, "", "", ""

for estudiante in lista:
    if alto==0 and bajo==0:
        alto = bajo = estudiante["promedio"]
    else:
        if estudiante["promedio"]<bajo:
            bajo = estudiante["promedio"]
            prom_bajo = estudiante["nombre"]
        elif estudiante["promedio"]>alto:
            alto = estudiante["promedio"]
            prom_alto = estudiante["nombre"]

        if len(estudiante["nombre"])>nombre:
            nombre = len(estudiante["nombre"])
            nombre_largo = estudiante["nombre"]
    
print("Estudiante con promedio mas alto:", prom_alto)
print("Estudiante con nombre mas largo:", nombre_largo)
print("Estudiante con promedio mas bajo:", prom_bajo)