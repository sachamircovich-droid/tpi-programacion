import csv
nombre_archivo = "paises.csv"
campos = ["nombre", "poblacion", "superficie", "continente"]


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
            

def filtrar_continente(nombre_archivo):

    encontrado = False
    continente = pedir_texto("\nIngresar continente: ")
    print()

    with open(nombre_archivo,"r",encoding="utf-8") as archivo:
        
        lector = csv.DictReader(archivo)
        for fila in lector:
            if fila['continente'] == continente:
                print(f"{fila['nombre']:<15} Poblacion: {fila['poblacion']:<15} Superficie: {fila['superficie']:<15} Continente: {fila['continente']:<15}")
                encontrado = True

        if not encontrado:
            print(f"\nNo se encontro pais en el contienente {continente}")





def filtrar_poblacion(nombre_archivo):
    poblacion_min = pedir_entero("\nPoblación mínima: ")
    poblacion_max = pedir_entero("Población máxima: ", minimo=poblacion_min)
    print()

    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)

        encontrado = False

        for fila in lector:
            poblacion = int(fila["poblacion"])

            if poblacion_min <= poblacion <= poblacion_max:
                print(f"{fila['nombre']:<15} Poblacion: {fila['poblacion']:<15} Superficie: {fila['superficie']:<15} Continente: {fila['continente']:<15}")
                encontrado = True

        if not encontrado:
            print("No hay países en ese rango.")
    

def filtrar_superficie(nombre_archivo):
    superficie_min = pedir_entero("\nSuperficie mínima: ")
    superficie_max = pedir_entero("Superficie máxima: ", minimo=superficie_min)
    print()

    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)

        encontrado = False

        for fila in lector:
            superficie = int(fila["superficie"])

            if superficie_min <= superficie <= superficie_max:
                print(f"{fila['nombre']:<15} Poblacion: {fila['poblacion']:<15} Superficie: {fila['superficie']:<15} Continente: {fila['continente']:<15}")
                encontrado = True

        if not encontrado:
            print("No hay países en ese rango.")

def sub_menu_4(nombre_archivo):

    op = -1
    while op != 0:
        print("\nFiltrar por:")
        print("     1. Contienete")
        print("     2. Rango de Poblacion")
        print("     3. Rango de Superficie")
        print("     0. Salir")

        op = pedir_entero("\nSeleccione una opción (0-3): ", minimo=0)

        if op == 1:
            filtrar_continente(nombre_archivo)
        elif op == 2:
            filtrar_poblacion(nombre_archivo)
        elif op == 3:
            filtrar_superficie(nombre_archivo)


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

    nombre = pedir_texto("\nNombre: ")
    poblacion = pedir_entero("Poblacion: ")
    superficie = pedir_entero("Superficie: ")
    continente = pedir_texto("Continente: ")

    return {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }


def agregar_pais(nombre_archivo,campos):

    with open(nombre_archivo, "a", encoding="utf-8", newline="") as archivo:

        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writerow(nuevo_pais())

    print("\nPaís guardado correctamente en el archivo CSV.")


def buscar_pais(nombre_archivo):

    pais = pedir_texto("Ingresar el nombre del país a buscar: ")
    encontrado = False
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)

        for fila in lector:
            if fila["nombre"] == pais:
                print(f"\nNombre: {fila['nombre']}")
                print(f"Población: {fila['poblacion']}")
                print(f"Superficie: {fila['superficie']}")
                print(f"Continente: {fila['continente']}")
                encontrado = True
                input("\nPresione una tecla para continuar.")

        if not encontrado:
            print("\nNo se encontro un pais con ese nombre")

def actualizar_pais(nombre_archivo,campos):

    paises = []

    pais = pedir_texto("Ingresar el nombre del país a buscar: ")

    encontrado = False
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:

        lector = csv.DictReader(archivo)
        for fila in lector:
            if fila["nombre"] == pais:
                print(f"\nNombre: {fila['nombre']}")
                print(f"Población: {fila['poblacion']}")
                print(f"Superficie: {fila['superficie']}")
                print(f"Continente: {fila['continente']}")
                encontrado = True

                print("\nActualizar datos")

                fila["poblacion"] = str(pedir_entero("\nNueva población: "))
                fila["superficie"] = str(pedir_entero("Nueva superficie: "))

            paises.append(fila)
        
        if not encontrado:
            print("\nNo se ecnontro el pais.")
            return
        

        with open(nombre_archivo, "w", encoding="utf-8",newline="") as archivo:
            escritor = csv.DictWriter(archivo,fieldnames=campos)
            escritor.writeheader()
            escritor.writerows(paises)
        
        print("\nPaís actualizado correctamente.")



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
        agregar_pais(nombre_archivo, campos)
    elif op ==2:
        actualizar_pais(nombre_archivo,campos)
    elif op == 3:
        buscar_pais(nombre_archivo)
    elif op == 4:
        sub_menu_4(nombre_archivo)
    elif op == 5:
        sub_menu_5()
    elif op == 6:
        sub_menu_6()
    elif op == 0:
        print("\nFin del preoceso.")
    


