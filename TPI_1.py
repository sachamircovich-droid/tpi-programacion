def pedir_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("\n[Error] Tipo de dato inválido. Debe ingresar un número entero.")

def sub_menu_1():

    op = -1
    while op != 0:
        print("\n     1. Contienete")
        print("     2. Rango de Poblacion")
        print("     3. Rango de Superficie")
        print("     0. Salir")

        op = pedir_entero("\nIngresar una opcion: ")

        if op == 1:
            pass
        elif op == 2:
            pass
        elif op == 3:
            pass


def sub_menu_2_1():

    op = -1
    while op != 0:
        print("\n        1. Ascendente")
        print("        2. Descendente")
        print("        0. Salir")

        op = pedir_entero("\nIngresar una opcion: ")

        if op == 1:
            pass
        elif op == 2:
            pass


def sub_menu_2():

    op = -1
    while op != 0:
        print("\n     1. Nombre")
        print("     2. Poblacion")
        print("     3. Superficie")
        print("     0. Salir")

        op = pedir_entero("\nIngresar una opcion: ")

        if op == 1:
            pass
        elif op == 2:
            pass
        elif op == 3:
            sub_menu_2_1()

def sub_menu_3():

    op = -1
    while op != 0:
        print("\n     1. País con mayor y menor población ")
        print("     2. Promedio de población ")
        print("     3. Promedio de superficie ")
        print("     4. Cantidad de países por continente ")
        print("     0. Salir")

        op = pedir_entero("\nIngresar una opcion: ")

        if op == 1:
            pass
        elif op == 2:
            pass
        elif op == 3:
            pass
        elif op == 4:
            pass


op = -1
while op != 0:
    print("\nMENU DE OPCIONES")
    print("\n1. Agregar pais")
    print("2. Actualizar Población y Superficie de un País.")
    print("3. Buscar pais por nombre")
    print("4. Filtrar paises")
    print("5. Ordenar paises")
    print("6. Mostrar estadisticas")
    print("0. Salir")

    op = pedir_entero("\nIngresar una opcion: ")

    if op == 1:
        pass
    elif op ==2:
        pass
    elif op == 3:
        pass
    elif op == 4:
        sub_menu_1()
    elif op == 5:
        sub_menu_2()
    elif op == 6:
        sub_menu_3()
    elif op == 0:
        print("\nFin del preoceso.")


