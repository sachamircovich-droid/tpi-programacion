import csv


def pedir_entero(mensaje, minimo=0):
    
    while True:
        try:
            valor = int(input(mensaje))
            if valor < minimo:
                print(f"Error: El valor debe ser mayor o igual a {minimo}.")
                continue  
            return valor          
        except ValueError:
            print("Error: Ingresar un número entero válido.")

def pedir_texto(mensaje):
    while True:
        valor = input(mensaje).strip().title()
        if valor == "" or not valor.isalpha():
            print("Error: No debe ingresar numero ni ingresar un espacio vacio")
            continue
        else:
            return valor
            
def sub_menu_4():

    op = -1
    while op != 0:
        print("\n     1. Contienete")
        print("     2. Rango de Poblacion")
        print("     3. Rango de Superficie")
        print("     0. Salir")

        op = pedir_entero("Seleccione una opción (0-3): ", minimo=0)

        if op == 1:
            pass
        elif op == 2:
            pass
        elif op == 3:
            pass


def sub_menu_5_1():

    op = -1
    while op != 0:
        print("\n        1. Ascendente")
        print("        2. Descendente")
        print("        0. Salir")

        op = pedir_entero("Seleccione una opción (0-2): ", minimo=0)

        if op == 1:
            pass
        elif op == 2:
            pass


def sub_menu_5():

    op = -1
    while op != 0:
        print("\n     1. Nombre")
        print("     2. Poblacion")
        print("     3. Superficie")
        print("     0. Salir")

        op = pedir_entero("Seleccione una opción (0-3): ", minimo=0)

        if op == 1:
            pass
        elif op == 2:
            pass
        elif op == 3:
            sub_menu_5_1()

def sub_menu_6():

    op = -1
    while op != 0:
        print("\n     1. País con mayor y menor población ")
        print("     2. Promedio de población ")
        print("     3. Promedio de superficie ")
        print("     4. Cantidad de países por continente ")
        print("     0. Salir")

        op = pedir_entero("Seleccione una opción (0-4): ", minimo=0)

        if op == 1:
            pass
        elif op == 2:
            pass
        elif op == 3:
            pass
        elif op == 4:
            pass

def nuevo_pais():
    print("\nREGISRO DE NUEVO PAIS")

    nombre = pedir_texto("Nombre: ")
    poblacion = pedir_entero("Poblacion: ")
    superficie = pedir_entero("Superficie: ")
    continente = pedir_texto("Continente: ")

    return ([nombre,poblacion,superficie,continente])


def agregar_pais():

    with open("paises.csv","a",encoding="utf-8",newline="") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(nuevo_pais())
    print(f"\nPais guardado correctamente en el archivo CSV. ")
        

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

    op = pedir_entero("\nSeleccione una opción (0-6): ", minimo=0)

    if op == 1:
        agregar_pais()
    elif op ==2:
        pass
    elif op == 3:
        pass
    elif op == 4:
        sub_menu_4()
    elif op == 5:
        sub_menu_5()
    elif op == 6:
        sub_menu_6()
    elif op == 0:
        print("\nFin del preoceso.")
    


