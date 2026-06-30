import csv # Modulo para manejo de archivo csv
todos = "lista de todos los países.txt" # Dataset para validar ingreso de paises reales
nombre_archivo = "paises.csv" # Nombre del dataset ubicado en el directorio del proyecto
campos = ["nombre", "poblacion", "superficie", "continente"] # Claves del diccionario para el manejo de paises

# Funcion que se encarga del filtrar paises por continente
def filtrar_continente(nombre_archivo):

    encontrado = False
    continente = pedir_texto("\nIngresar continente: ")
    while continente not in ("América", "Europa", "Asia", "África", "Oceanía" ):
        continente = pedir_texto("Ingrese un nombre válido de continente: ")
    print()

    with open(nombre_archivo,"r",encoding="utf-8") as archivo:
        
        lector = csv.DictReader(archivo)
        for fila in lector:
            if fila['continente'] == continente:
                print(f"{fila['nombre']:<15} Poblacion: {fila['poblacion']:<15} Superficie: {fila['superficie']:<15} Continente: {fila['continente']:<15}")
                encontrado = True

        if not encontrado:
            print(f"\nNo se encontro pais en el contienente {continente}")

# Funcion que filta paises por poblacion
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
    
# Funcion que filtra paises por superficie
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

# Funcion que despliega menú para filtrar paises
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

# Funcion que imprime una lista de paises
def mostrar_paises(paises):
    print()
    for fila in paises:
        print(f"{fila['nombre']:<15} Poblacion: {fila['poblacion']:<15} Superficie: {fila['superficie']:<15} Continente: {fila['continente']:<15}")


# Funcion que se encarga de realizar un ordenamiento de selección directa
def ordenar_paises(paises, campo, ascendente=True):

    for i in range(len(paises) - 1):
        posicion = i

        for j in range(i + 1, len(paises)):

            if campo in ["poblacion", "superficie"]:
                valor_j = int(paises[j][campo])
                valor_pos = int(paises[posicion][campo])
            else:
                valor_j = paises[j][campo]
                valor_pos = paises[posicion][campo]

            if ascendente:
                if valor_j < valor_pos:
                    posicion = j
            else:
                if valor_j > valor_pos:
                    posicion = j

        paises[i], paises[posicion] = paises[posicion], paises[i]

    return paises

# Funcion que se encarga de seleccionar el formato ascendente o descendente para el ordenamiento de países por superficie
def sub_menu_5_1(paises):

    op = -1
    while op != 0:
        print("\n        1. Ascendente")
        print("        2. Descendente")
        print("        0. Salir")

        op = pedir_entero("Seleccione una opción (0-2): ", minimo=0)

        if op == 1:
            print("\nOrdenamiento por superficie - ascendente")
            ordenar_paises(paises,'superficie')
            mostrar_paises(paises)
            input("\nPresione una tecla para continuar.")
            break
            
        elif op == 2:
            print("\nOrdenamiento por superficie - descendente")
            ordenar_paises(paises,'superficie',ascendente=False)
            mostrar_paises(paises)
            input("\nPresione una tecla para continuar.")
            break

# Funcion que despliega menú para seleccionar tipo de ordenamiento deseado
def sub_menu_5(nombre_archivo):

    
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        paises = list(lector)

    op = -1
    while op != 0:
        print("\n     1. Nombre")
        print("     2. Poblacion")
        print("     3. Superficie (ascendente o descendente)")
        print("     0. Salir")

        op = pedir_entero("Seleccione el ordenamiento que desea realizar (0-3): ", minimo=0)

        if op == 1:
            print("\nOrdenamiento por nombre")
            ordenar_paises(paises,'nombre')
            mostrar_paises(paises)
            input("\nPresione una tecla para continuar.")
            break
        elif op == 2:
            print("\nOrdenamiento por poblacion")
            ordenar_paises(paises,'poblacion')
            mostrar_paises(paises)
            input("\nPresione una tecla para continuar.")
            break
        elif op == 3:
            sub_menu_5_1(paises)
            break

# Funcion que muestra paises con mayor y menor poblacion
def mayor_menor_poblacion(paises):

    mayor = paises[0]
    menor = paises[0]

    for pais in paises:
        if int(pais["poblacion"]) > int(mayor["poblacion"]):
            mayor = pais

        if int(pais["poblacion"]) < int(menor["poblacion"]):
            menor = pais

    print(f"\nPaís con mayor población: {mayor['nombre']} ({mayor['poblacion']})")
    print(f"País con menor población: {menor['nombre']} ({menor['poblacion']})")
    input("\nPresione una tecla para continuar.")

# Funcion que muestra el promedio de población de los países
def prom_poblacion(paises):

    suma = 0

    for pais in paises:
        suma += int(pais["poblacion"])

    promedio = suma / len(paises)

    print(f"\nPromedio de población: {promedio:.2f}")
    input("\nPresione una tecla para continuar.")

# Funcion que muestra el promedio de superficie de los países
def prom_superficie(paises):

    suma = 0

    for pais in paises:
        suma += int(pais["superficie"])

    promedio = suma / len(paises)

    print(f"\nPromedio de superficie: {promedio:.2f}")
    input("\nPresione una tecla para continuar.")

# Funcion que muestra cuantos paises hay por continente
def cant_continente(paises):

    continentes = {}

    for pais in paises:
        continente = pais["continente"]

        if continente in continentes:
            continentes[continente] += 1
        else:
            continentes[continente] = 1

    print()

    for continente, cantidad in continentes.items():
        print(f"{continente}: {cantidad} país/es")  
    input("\nPresione una tecla para continuar.")  

# Funcion que despliega menú para seleccionar estadísticas que se desean mostrar
def sub_menu_6(nombre_archivo):
    
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        paises = list(lector)

    op = -1
    while op != 0:
        print("\n     1. País con mayor y menor población ")
        print("     2. Promedio de población ")
        print("     3. Promedio de superficie ")
        print("     4. Cantidad de países por continente ")
        print("     0. Salir")

        op = pedir_entero("\nSeleccione una opción (0-4): ", minimo=0)

        if op == 1:
            mayor_menor_poblacion(paises)

        elif op == 2:
            prom_poblacion(paises)

        elif op == 3:
            prom_superficie(paises)

        elif op == 4:
            cant_continente(paises)

# Funcion que busca un pais por nombre y muestra los datos del mismo 
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

# Funcion que busca un pais por nombre y permite modificar datos de superficie y población.
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

# Funcion que agrega un nuevo pais al dataset
def agregar_pais(nombre_archivo,campos,todos):

    with open(nombre_archivo, "a", encoding="utf-8", newline="") as archivo:

        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writerow(nuevo_pais(nombre_archivo,todos))

    print("\nPaís guardado correctamente en el archivo CSV.")

# Funcion que verifica si el pais que desea agregar existe y genera los datos de poblacion, superficie y continente
def nuevo_pais(nombre_archivo,todos):
    print("\nREGISRO DE NUEVO PAIS")
    lista =[]
    with open(nombre_archivo, "r", encoding = "utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for pais in lector:
            lista.append(pais)
    
    while True:
        encontrado = False

        nombre = pedir_texto("\nNombre: ")
        if pais_valido(nombre,todos) is False:
            print("El país ingresado no existe. Vuelve a ingresar el nombre")
            continue

        for i in lista:
            if i["nombre"] == nombre:
                print("El país ya se encuentra cargado. Vuelve a ingresar el nombre")
                encontrado = True
                break 
        if encontrado == True:
            continue
        else:
            break
    
    poblacion = pedir_entero("Poblacion: ")
    superficie = pedir_entero("Superficie: ")
    continente = pedir_texto("Continente: ")
    while continente not in ("América", "Europa", "Asia", "África", "Oceanía" ):
        continente = pedir_texto("Ingrese un nombre válido de continente: ")

    return {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }

# Funcion que virifica si el pais que desea agregar existe
def pais_valido(nombre,todos):
    with open(todos, "r", encoding = "utf-8") as archivo:
        for i in archivo:
            if i.title().strip() == nombre:
                return True
    return False        

# funcion que valida un ingreso de numero entero
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

# Funcion que valida un ingreso de string
def pedir_texto(mensaje):
    while True:
        valor = input(mensaje).strip().title()
        if valor.replace(" ","").isalpha():
            return valor            
        else:
            print("Error: No debe ingresar numero ni ingresar un espacio vacio")
            continue

# Menu principal de opciones
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
        agregar_pais(nombre_archivo, campos, todos)
    elif op ==2:
        actualizar_pais(nombre_archivo,campos)
    elif op == 3:
        buscar_pais(nombre_archivo)
    elif op == 4:
        sub_menu_4(nombre_archivo)
    elif op == 5:
        sub_menu_5(nombre_archivo)
    elif op == 6:
        sub_menu_6(nombre_archivo)
    elif op == 0:
        print("\nFin del preoceso.")
    else:
        print("\nOpcion incorrecta. Intentelo de nuevo")
