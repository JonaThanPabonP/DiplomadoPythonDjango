menu = [
    ["ID004", "entrada", "ensalada"],
    ["ID008", "entrada", "sopa de tomate"],
    ["ID005", "entrada", "sopa de cebolla"],
    ["ID011", "bebida", "Jugo de Fresa"],
    ["ID012", "bebida", "Limonada Natural"],
    ["ID102", "plato fuerte", "pasta"],
    ["ID106", "plato fuerte", "lassagna"],
]

def opciones():
    print("--- MENU ---")
    print("1. Visualizar la informacion del menú.")
    print("2. Agregar nuevos elementos al menú.")
    print("3. Filtrar por una categoría.")
    print("4. Buscar por un nombre.")
    print("5. Visualizar nombres en categorías.")
    print("0. Salir.")


# Visualizar info menu
def ver_menu(menu):
    for elem in menu:
        print(elem)

# Agregar elementos
def add_menu(menu, elemento):
    menu.append(elemento)

# Filtro por categoria
def filtro_menu(menu, filter):
    for elem in menu:
        if filter == elem[1]:
            print(elem)
        

# Buscar por nombre
def buscar(menu, nombre):
    for elem in menu:
        if nombre == elem[3]:
            print(elem[3])
        

# Visualizar nombres
def visua_nombres_cat(menu):
    listado_plato = {}
    for elem in menu:
        cat = elem[1]
        plato = elem[2]
        if cat not in listado_plato.keys():
            listado_plato.update({cat: [plato]})
        else:
            listado_plato[cat].append(plato)
    
    for categ in listado_plato:
        print(f"{categ}: {listado_plato[categ]}")


# Inicio App
def inicio():
    print("Bienvenido...")
    flag = True
    while flag == True:
        opciones()
        opc = int(input("Ingrese la opcion que desea realizar: "))
        if opc == 0:
            print("Gracias por venir. Vuelva pronto!")
            flag = False
        elif opc == 1:
            ver_menu(menu)
        elif opc == 2:
            id = input("Ingrese el id del producto: ")
            categoria = input("Ingrese la categoria del producto: ")
            nombre = input("Ingrese el nombre del plato: ")
            elemento = [id, categoria, nombre]
            add_menu(menu,elemento)
        elif opc == 3:
            filtro = input("Ingrese la categoria: ")
            filtro_menu(menu, filtro)
        elif opc == 4:
            nombre = input("Ingrese el plato: ")
            buscar(menu, nombre)
        elif opc == 5:
            visua_nombres_cat(menu)
        else:
            print("Opcion no valida.")


# if __name__ == 'main':
inicio()