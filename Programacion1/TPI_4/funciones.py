"""
Biblioteca de funciones del TP Lista de Diccionarios, Archivos y
Paradigma Funcional.

Estructura de datos:
    estudiantes (list): lista donde cada elemento es un diccionario
                        que representa a un estudiante, con las claves:
        "legajo" (int): entero de cinco cifras.
        "nombre" (str): apellido y nombre.
        "genero" (str): "F", "M" o "X".
        "notas" (list): lista de cinco calificaciones enteras (1 a 10).
        "promedio" (float): promedio de las notas. Vale 0 mientras no
                            se calcula (ítem 5): un 0 significa "sin
                            calcular" y nunca se usa como promedio.

Los datos pueden cargarse desde un archivo CSV (ítem 1) o manualmente
(ítem 2), y se pueden guardar en un archivo JSON (ítem 11).
"""

import json

LONGITUD_LEGAJO = 5
CANTIDAD_MATERIAS = 5
CANTIDAD_ESTUDIANTES = 1000
NOTA_MINIMA = 1
NOTA_MAXIMA = 10
PROMEDIO_APROBACION = 4


# ---------------------------------------------------------------------------
# CREACIÓN DE LA ESTRUCTURA DE DATOS
# ---------------------------------------------------------------------------
def crear_estudiante() -> dict:
    """
    Crea un diccionario de estudiante con valores iniciales vacíos.

    Retorno:
        dict: estudiante con las claves legajo, nombre, genero, notas
              (lista de cinco ceros) y promedio (0, sin calcular).
    """
    estudiante = {
        "legajo": 0,
        "nombre": "",
        "genero": "",
        "notas": [0] * CANTIDAD_MATERIAS,
        "promedio": 0
    }

    return estudiante


def crear_lista_estudiantes(cantidad: int) -> list:
    """
    Crea la lista de estudiantes: cada elemento es un diccionario
    distinto con valores iniciales vacíos.

    Argumentos:
        cantidad (int): cantidad de estudiantes.

    Retorno:
        list: lista de diccionarios.
    """
    estudiantes = [0] * cantidad

    for i in range(cantidad):
        estudiantes[i] = crear_estudiante()

    return estudiantes


def nombre_materia(indice: int) -> str:
    """
    Arma el nombre de una materia a partir del índice de su posición en
    la lista de notas. El índice 0 es MAT_1, el 1 es MAT_2, etc.

    Argumentos:
        indice (int): índice de la materia en la lista de notas.

    Retorno:
        str: nombre de la materia (por ejemplo "MAT_1").
    """
    return f"MAT_{indice + 1}"


# ---------------------------------------------------------------------------
# VALIDACIONES
# ---------------------------------------------------------------------------
def es_numero(caracter: str) -> bool:
    """
    Indica si un carácter es un dígito del 0 al 9.

    Argumentos:
        caracter (str): carácter a evaluar.

    Retorno:
        bool: True si es un dígito, False en caso contrario.
    """
    retorno = False
    codigo = ord(caracter)

    if codigo >= 48 and codigo <= 57:
        retorno = True

    return retorno


def es_numerico(cadena: str) -> bool:
    """
    Indica si un texto no vacío está formado solo por dígitos.

    Argumentos:
        cadena (str): texto a evaluar.

    Retorno:
        bool: True si todos los caracteres son dígitos, False en caso
              contrario o si el texto está vacío.
    """
    retorno = cadena != ""

    for caracter in cadena:
        if es_numero(caracter) == False:
            retorno = False
            break

    return retorno


def es_letra(caracter: str) -> bool:
    """
    Indica si un carácter es una letra (mayúscula o minúscula, con o sin
    tilde, incluyendo la ñ y la ü).

    Argumentos:
        caracter (str): carácter a evaluar.

    Retorno:
        bool: True si es una letra, False en caso contrario.
    """
    retorno = False
    codigo = ord(caracter)

    if (codigo >= 65 and codigo <= 90) or \
        (codigo >= 97 and codigo <= 122) or \
        codigo == 193 or codigo == 201 or codigo == 205 or \
        codigo == 211 or codigo == 218 or codigo == 220 or \
        codigo == 225 or codigo == 233 or codigo == 237 or \
        codigo == 243 or codigo == 250 or codigo == 252 or \
        codigo == 209 or codigo == 241:
        retorno = True

    return retorno


def es_alfabetico(cadena: str) -> bool:
    """
    Indica si un texto está formado solo por letras y espacios, y tiene
    al menos una letra.

    Argumentos:
        cadena (str): texto a evaluar.

    Retorno:
        bool: True si es válido, False en caso contrario.
    """
    retorno = True
    hay_letra = False

    for caracter in cadena:
        if es_letra(caracter):
            hay_letra = True
        elif ord(caracter) != 32:
            retorno = False
            break

    if hay_letra == False:
        retorno = False

    return retorno


def es_genero(genero: str) -> bool:
    """
    Indica si un texto es un género válido: F, M o X (mayúscula o
    minúscula).

    Argumentos:
        genero (str): texto a evaluar.

    Retorno:
        bool: True si es válido, False en caso contrario.
    """
    retorno = False

    if genero == "F" or genero == "M" or genero == "X" or \
        genero == "f" or genero == "m" or genero == "x":
        retorno = True

    return retorno


def es_legajo(legajo: str) -> bool:
    """
    Indica si un texto es un legajo válido: un entero de cinco cifras
    (entre 10000 y 99999, sin cero a la izquierda).

    Argumentos:
        legajo (str): texto a evaluar.

    Retorno:
        bool: True si es válido, False en caso contrario.
    """
    retorno = False

    if es_numerico(legajo) and len(legajo) == LONGITUD_LEGAJO \
        and legajo[0] != "0":
        retorno = True

    return retorno


def es_nota(nota: str) -> bool:
    """
    Indica si un texto es una calificación válida: un entero entre 1 y 10.

    Argumentos:
        nota (str): texto a evaluar.

    Retorno:
        bool: True si es válida, False en caso contrario.
    """
    retorno = False

    if es_numerico(nota):
        valor = int(nota)
        if valor >= NOTA_MINIMA and valor <= NOTA_MAXIMA:
            retorno = True

    return retorno


def es_materia(materia: str, cantidad_materias: int) -> bool:
    """
    Indica si un texto es un número de materia válido: un entero entre
    1 y la cantidad de materias (índice de la materia más uno).

    Argumentos:
        materia (str): texto a evaluar.
        cantidad_materias (int): cantidad de materias.

    Retorno:
        bool: True si es válido, False en caso contrario.
    """
    retorno = False

    if es_numerico(materia):
        valor = int(materia)
        if valor >= 1 and valor <= cantidad_materias:
            retorno = True

    return retorno


def es_cantidad(cantidad: str, maximo: int) -> bool:
    """
    Indica si un texto es una cantidad de estudiantes válida: un entero
    entre 1 y el máximo.

    Argumentos:
        cantidad (str): texto a evaluar.
        maximo (int): cantidad máxima permitida.

    Retorno:
        bool: True si es válida, False en caso contrario.
    """
    retorno = False

    if es_numerico(cantidad):
        valor = int(cantidad)
        if valor >= 1 and valor <= maximo:
            retorno = True

    return retorno


def es_promedio(promedio: str) -> bool:
    """
    Indica si un texto es un promedio válido para un archivo: un número
    (con o sin parte decimal) igual a 0 (sin calcular) o entre 1 y 10.

    Argumentos:
        promedio (str): texto a evaluar.

    Retorno:
        bool: True si es válido, False en caso contrario.
    """
    retorno = False
    partes = promedio.split(".")

    if len(partes) <= 2 and es_numerico(partes[0]) and \
        (len(partes) == 1 or es_numerico(partes[1])):
        valor = float(promedio)
        if valor == 0 or (valor >= NOTA_MINIMA and valor <= NOTA_MAXIMA):
            retorno = True

    return retorno


def es_nombre_archivo(nombre: str) -> bool:
    """
    Indica si un texto sirve como nombre de archivo: no está vacío y no
    contiene caracteres prohibidos en nombres de archivo.

    Argumentos:
        nombre (str): nombre a evaluar.

    Retorno:
        bool: True si es válido, False en caso contrario.
    """
    retorno = nombre != ""

    for caracter in nombre:
        if caracter in '\\/:*?"<>|':
            retorno = False
            break

    return retorno


# ---------------------------------------------------------------------------
# CARGA MANUAL DE DATOS (ítem 2)
# ---------------------------------------------------------------------------
def cargar_legajo() -> int:
    """
    Pide un legajo por consola y lo valida hasta que sea un entero de
    cinco cifras.

    Retorno:
        int: legajo ingresado.
    """
    legajo = input("Ingrese el legajo (5 cifras): ")

    while es_legajo(legajo) == False:
        print("Error. El legajo debe ser un número entero de 5 cifras.")
        legajo = input("Ingrese el legajo (5 cifras): ")

    return int(legajo)


def cargar_nombre() -> str:
    """
    Pide el nombre por consola y lo valida hasta que contenga solo
    letras y espacios.

    Retorno:
        str: nombre ingresado.
    """
    nombre = input("Ingrese el nombre: ")

    while es_alfabetico(nombre) == False:
        print("Error. Ingrese solamente letras y espacios.")
        nombre = input("Ingrese el nombre: ")

    return nombre


def cargar_genero() -> str:
    """
    Pide el género por consola y lo valida hasta que sea F, M o X
    (se acepta también en minúscula; el ítem 3 lo pasa a mayúscula).

    Retorno:
        str: género ("F", "M" o "X").
    """
    genero = input("Ingrese el género (F/M/X): ")

    while es_genero(genero) == False:
        print("Error. Ingrese F, M o X.")
        genero = input("Ingrese el género (F/M/X): ")

    return genero


def cargar_nota(indice_materia: int) -> int:
    """
    Pide la calificación de una materia por consola y la valida hasta
    que sea un entero entre 1 y 10.

    Argumentos:
        indice_materia (int): índice de la materia en la lista de notas.
                              Se usa solo para armar el mensaje.

    Retorno:
        int: calificación ingresada.
    """
    mensaje = f"Ingrese la nota de {nombre_materia(indice_materia)} (1-10): "
    nota = input(mensaje)

    while es_nota(nota) == False:
        print("Error. Ingrese un entero entre 1 y 10.")
        nota = input(mensaje)

    return int(nota)


def cargar_cantidad(maximo: int) -> int:
    """
    Pide por consola la cantidad de estudiantes a cargar y la valida
    hasta que sea un entero entre 1 y el máximo.

    Argumentos:
        maximo (int): cantidad máxima permitida.

    Retorno:
        int: cantidad ingresada.
    """
    mensaje = f"Ingrese la cantidad de estudiantes a cargar (1-{maximo}): "
    cantidad = input(mensaje)

    while es_cantidad(cantidad, maximo) == False:
        print(f"Error. Ingrese un número entre 1 y {maximo}.")
        cantidad = input(mensaje)

    return int(cantidad)


def cargar_estudiantes(estudiantes: list) -> None:
    """
    Carga los datos de todos los estudiantes en la lista de
    diccionarios. La cantidad de estudiantes es el tamaño de la lista.
    El promedio queda en 0 (sin calcular) hasta el ítem 5.

    Argumentos:
        estudiantes (list): lista de diccionarios de estudiantes.

    Retorno:
        None: modifica los diccionarios de la lista original.
    """
    for i in range(len(estudiantes)):
        print(f"\nEstudiante {i + 1}")

        estudiantes[i]["legajo"] = cargar_legajo()
        estudiantes[i]["nombre"] = cargar_nombre()
        estudiantes[i]["genero"] = cargar_genero()

        for j in range(len(estudiantes[i]["notas"])):
            estudiantes[i]["notas"][j] = cargar_nota(j)

        estudiantes[i]["promedio"] = 0

    print("\nDatos cargados correctamente.")


# ---------------------------------------------------------------------------
# NORMALIZAR A MAYÚSCULAS - PARADIGMA FUNCIONAL (ítem 3)
# ---------------------------------------------------------------------------
# Función lambda: recibe un texto y devuelve el texto en mayúsculas.
a_mayuscula = lambda texto: texto.upper()


def normalizar_texto(texto: str) -> str:
    """
    Normaliza un texto: le quita los espacios del principio y del final
    y lo convierte a mayúsculas. No modifica el texto original.

    Argumentos:
        texto (str): texto a normalizar.

    Retorno:
        str: texto normalizado.
    """
    return a_mayuscula(texto.strip())


def normalizar_estudiante(estudiante: dict) -> dict:
    """
    Devuelve un NUEVO diccionario igual al estudiante recibido, pero con
    los datos de tipo str (nombre y género) normalizados. No modifica el
    diccionario original.

    Argumentos:
        estudiante (dict): diccionario de un estudiante.

    Retorno:
        dict: estudiante con nombre y género en mayúsculas.
    """
    return {
        "legajo": estudiante["legajo"],
        "nombre": normalizar_texto(estudiante["nombre"]),
        "genero": normalizar_texto(estudiante["genero"]),
        "notas": estudiante["notas"],
        "promedio": estudiante["promedio"]
    }


def normalizar_estudiantes(estudiantes: list) -> list:
    """
    Aplica normalizar_estudiante a todos los estudiantes usando map.

    Argumentos:
        estudiantes (list): lista de diccionarios de estudiantes.

    Retorno:
        list: NUEVA lista de diccionarios con los str en mayúsculas.
    """
    return list(map(normalizar_estudiante, estudiantes))


# ---------------------------------------------------------------------------
# MOSTRAR ESTUDIANTES (ítems 4, 6, 7 y 9)
# ---------------------------------------------------------------------------
def mostrar_estudiante(estudiante: dict) -> None:
    """
    Muestra en una fila los datos de UN estudiante: legajo, nombre,
    género, cada nota y promedio, con un separador entre valores. Si
    el promedio todavía no se calculó, muestra un guion.

    Argumentos:
        estudiante (dict): diccionario del estudiante a mostrar.

    Retorno:
        None.
    """
    fila = f"{estudiante['legajo']:<6} | {estudiante['nombre']:<26} "
    fila += f"| {estudiante['genero']:<6}"

    for j in range(len(estudiante["notas"])):
        fila += f" | {estudiante['notas'][j]:<2}"

    if estudiante["promedio"] == 0:
        fila += f" | {'-':<5}"
    else:
        fila += f" | {estudiante['promedio']:<5.2f}"

    print(fila)


def mostrar_estudiantes(estudiantes: list,
                        criterio: str = "TODOS",
                        valor: int = None,
                        titulo: str = "INFORME DE ESTUDIANTES") -> None:
    """
    Recorre la lista de estudiantes y muestra, llamando a
    mostrar_estudiante, los que cumplan el criterio. Antes muestra un
    encabezado con las claves: LEGAJO | NOMBRE | GENERO | N1 | N2 | N3 |
    N4 | N5 | PROM.

    Argumentos:
        estudiantes (list): lista de diccionarios de estudiantes.
        criterio (str): "TODOS" muestra a todos; "LEGAJO" muestra solo
                        al estudiante cuyo legajo es igual a valor.
        valor (int): legajo buscado cuando el criterio es "LEGAJO".
        titulo (str): título que se muestra sobre la tabla.

    Retorno:
        None.
    """
    if criterio == "LEGAJO":
        titulo = "ESTUDIANTE ENCONTRADO"

    print(f"\n--- {titulo} ---")

    titulos = f"{'LEGAJO':<6} | {'NOMBRE':<26} | {'GENERO':<6}"

    for j in range(len(estudiantes[0]["notas"])):
        titulos += f" | N{j + 1}"

    titulos += f" | {'PROM':<5}"

    print(titulos)
    print("-" * len(titulos))

    for i in range(len(estudiantes)):
        if criterio == "TODOS" or \
            (criterio == "LEGAJO" and estudiantes[i]["legajo"] == valor):
            mostrar_estudiante(estudiantes[i])


# ---------------------------------------------------------------------------
# PROMEDIOS DE LOS ESTUDIANTES - LAMBDA Y MAP (ítem 5)
# ---------------------------------------------------------------------------
# Función lambda: recibe la lista de calificaciones de un estudiante (cinco
# materias) y devuelve el promedio.
calcular_promedio = lambda notas: (
    notas[0] + notas[1] + notas[2] + notas[3] + notas[4]) / len(notas)


def asignar_promedio(estudiante: dict) -> dict:
    """
    Devuelve un NUEVO diccionario igual al estudiante recibido, pero con
    la clave "promedio" calculada con la lambda calcular_promedio. No
    modifica el diccionario original.

    Argumentos:
        estudiante (dict): diccionario de un estudiante.

    Retorno:
        dict: estudiante con su promedio.
    """
    return {
        "legajo": estudiante["legajo"],
        "nombre": estudiante["nombre"],
        "genero": estudiante["genero"],
        "notas": estudiante["notas"],
        "promedio": calcular_promedio(estudiante["notas"])
    }


def calcular_promedios(estudiantes: list) -> list:
    """
    Calcula el promedio de cada estudiante usando map: mapea la clave
    "promedio" de cada diccionario.

    Argumentos:
        estudiantes (list): lista de diccionarios de estudiantes.

    Retorno:
        list: NUEVA lista de diccionarios con el promedio calculado.
    """
    return list(map(asignar_promedio, estudiantes))


def mostrar_promedios(estudiantes: list) -> None:
    """
    Muestra una tabla con el nombre de cada estudiante y su promedio.

    Argumentos:
        estudiantes (list): lista de diccionarios de estudiantes.

    Retorno:
        None.
    """
    titulos = f"{'NOMBRE':<26} | {'PROM':<5}"
    print(titulos)
    print("-" * len(titulos))

    for i in range(len(estudiantes)):
        print(f"{estudiantes[i]['nombre']:<26} | {estudiantes[i]['promedio']:<5.2f}")


# ---------------------------------------------------------------------------
# ORDENAMIENTO (ítem 6)
# ---------------------------------------------------------------------------
def intercambiar(lista: list, i: int, j: int) -> None:
    """
    Intercambia los elementos de las posiciones i y j de una lista.

    Argumentos:
        lista (list): lista a modificar (puede contener diccionarios).
        i (int): primera posición.
        j (int): segunda posición.

    Retorno:
        None: modifica la lista original.
    """
    aux = lista[i]
    lista[i] = lista[j]
    lista[j] = aux


def ordenar_por_promedio(estudiantes: list, orden: str) -> None:
    """
    Ordena la lista de estudiantes por la clave "promedio". Como cada
    elemento es un diccionario completo, un solo intercambio mueve
    todos los datos del estudiante juntos.

    Argumentos:
        estudiantes (list): lista de diccionarios de estudiantes (con
                            el promedio ya calculado).
        orden (str): "ASC" (menor a mayor) o "DESC" (mayor a menor).

    Retorno:
        None: modifica la lista original.
    """
    if orden != "ASC" and orden != "DESC":
        print('Error. El orden debe ser "ASC" o "DESC".')
    else:
        n = len(estudiantes)

        for i in range(n - 1):
            for j in range(i + 1, n):
                if (orden == "DESC" and
                    estudiantes[j]["promedio"] > estudiantes[i]["promedio"]) or \
                    (orden == "ASC" and
                     estudiantes[j]["promedio"] < estudiantes[i]["promedio"]):
                    intercambiar(estudiantes, i, j)


# ---------------------------------------------------------------------------
# ESTUDIANTES CON PROMEDIO MENOR A 4 - FILTER (ítem 7)
# ---------------------------------------------------------------------------
def filtrar_desaprobados(estudiantes: list) -> list:
    """
    Filtra, usando filter, los estudiantes cuyo promedio es menor a
    PROMEDIO_APROBACION (4).

    Argumentos:
        estudiantes (list): lista de diccionarios de estudiantes (con el
                            promedio ya calculado).

    Retorno:
        list: NUEVA lista con los estudiantes de promedio menor a cuatro.
    """
    return list(filter(lambda estudiante: estudiante["promedio"] < PROMEDIO_APROBACION,
                       estudiantes))


# ---------------------------------------------------------------------------
# MATERIAS CON MAYOR PROMEDIO GENERAL (ítem 8)
# ---------------------------------------------------------------------------
def calcular_promedio_materia(estudiantes: list, indice: int) -> float:
    """
    Calcula el promedio general de una materia (la nota de esa posición
    en todos los estudiantes), con dos decimales.

    Argumentos:
        estudiantes (list): lista de diccionarios de estudiantes.
        indice (int): índice de la materia en la lista de notas.

    Retorno:
        float: promedio de la materia redondeado a 2 decimales.
    """
    suma = 0

    for i in range(len(estudiantes)):
        suma += estudiantes[i]["notas"][indice]

    return round(suma / len(estudiantes), 2)


def calcular_promedios_materias(estudiantes: list) -> list:
    """
    Calcula el promedio general de cada materia. La posición de la
    lista es el índice de la materia.

    Argumentos:
        estudiantes (list): lista de diccionarios de estudiantes.

    Retorno:
        list: promedios generales de las materias.
    """
    cantidad = len(estudiantes[0]["notas"])
    promedios_materias = [0.0] * cantidad

    for j in range(cantidad):
        promedios_materias[j] = calcular_promedio_materia(estudiantes, j)

    return promedios_materias


def buscar_mayor(valores: list) -> float:
    """
    Busca el mayor valor de una lista.

    Argumentos:
        valores (list): lista de números (no vacía).

    Retorno:
        float: el mayor valor de la lista.
    """
    mayor = valores[0]

    for i in range(len(valores)):
        if valores[i] > mayor:
            mayor = valores[i]

    return mayor


def mostrar_materia(indice: int, promedio: float) -> None:
    """
    Muestra en una fila UNA materia con su promedio general.

    Argumentos:
        indice (int): índice de la materia en la lista de notas.
        promedio (float): promedio general de la materia.

    Retorno:
        None.
    """
    print(f"{nombre_materia(indice):<10}{promedio:<10.2f}")


def mostrar_materias(promedios_materias: list,
                     criterio: str = "TODAS",
                     valor: float = None) -> None:
    """
    Recorre todas las materias y muestra, llamando a mostrar_materia,
    las que cumplan el criterio.

    Argumentos:
        promedios_materias (list): promedios generales de las materias.
        criterio (str): "TODAS" muestra todas; "MAYOR" muestra solo las
                        materias cuyo promedio es igual a valor.
        valor (float): promedio buscado cuando el criterio es "MAYOR".

    Retorno:
        None.
    """
    if criterio == "MAYOR":
        print("\n--- MATERIA/S CON MAYOR PROMEDIO GENERAL ---")
    else:
        print("\n--- PROMEDIO GENERAL DE LAS MATERIAS ---")

    titulos = f"{'MATERIA':<10}{'PROMEDIO':<10}"
    print(titulos)
    print("-" * len(titulos))

    for i in range(len(promedios_materias)):
        if criterio == "TODAS" or \
            (criterio == "MAYOR" and promedios_materias[i] == valor):
            mostrar_materia(i, promedios_materias[i])


# ---------------------------------------------------------------------------
# BÚSQUEDA POR LEGAJO (ítem 9)
# ---------------------------------------------------------------------------
def buscar_indice_legajo(estudiantes: list, legajo_buscar: int) -> int:
    """
    Busca un legajo en la lista de estudiantes.

    Argumentos:
        estudiantes (list): lista de diccionarios de estudiantes.
        legajo_buscar (int): legajo a buscar.

    Retorno:
        int: posición del estudiante en la lista, o -1 si no existe.
    """
    indice = -1

    for i in range(len(estudiantes)):
        if estudiantes[i]["legajo"] == legajo_buscar:
            indice = i
            break

    return indice


def buscar_estudiante(estudiantes: list, legajo_buscar: int) -> None:
    """
    Busca un estudiante por legajo y, si existe, muestra todos sus
    datos (incluyendo el promedio).

    Argumentos:
        estudiantes (list): lista de diccionarios de estudiantes.
        legajo_buscar (int): legajo a buscar.

    Retorno:
        None.
    """
    indice = buscar_indice_legajo(estudiantes, legajo_buscar)

    if indice == -1:
        print("No se encontró un estudiante con ese legajo.")
    else:
        mostrar_estudiantes(estudiantes, "LEGAJO", legajo_buscar)


# ---------------------------------------------------------------------------
# REPETICIÓN DE CALIFICACIONES EN UNA MATERIA (ítem 10)
# ---------------------------------------------------------------------------
def cargar_materia(cantidad_materias: int) -> int:
    """
    Pide por consola el número de una materia (índice más uno) y lo
    valida hasta que exista.

    Argumentos:
        cantidad_materias (int): cantidad de materias.

    Retorno:
        int: número de materia ingresado (entre 1 y cantidad_materias).
    """
    mensaje = f"Ingrese el número de materia (1-{cantidad_materias}): "
    materia = input(mensaje)

    while es_materia(materia, cantidad_materias) == False:
        print(f"Error. Ingrese un número entre 1 y {cantidad_materias}.")
        materia = input(mensaje)

    return int(materia)


def contar_calificaciones(estudiantes: list, materia: int) -> list:
    """
    Cuenta cuántas veces se repite cada calificación en una materia.

    Argumentos:
        estudiantes (list): lista de diccionarios de estudiantes.
        materia (int): número de materia (índice más uno).

    Retorno:
        list: lista de 10 elementos. En el índice 0 está la cantidad de
              veces que se repite la nota 1, en el índice 1 la nota 2,
              y así hasta el índice 9, que corresponde a la nota 10.
    """
    cantidades = [0] * NOTA_MAXIMA
    indice = materia - 1

    for i in range(len(estudiantes)):
        nota = estudiantes[i]["notas"][indice]
        cantidades[nota - 1] += 1

    return cantidades


def mostrar_repeticiones(cantidades: list, materia: int) -> None:
    """
    Muestra cuántas veces se repite cada calificación en una materia.

    Argumentos:
        cantidades (list): lista devuelta por contar_calificaciones.
        materia (int): número de materia (índice más uno).

    Retorno:
        None.
    """
    print(f"\n--- REPETICIÓN DE CALIFICACIONES EN {nombre_materia(materia - 1)} ---")

    for i in range(len(cantidades)):
        print(f"Nota {i + 1}: {cantidades[i]}")


# ---------------------------------------------------------------------------
# CARGA DESDE ARCHIVO CSV (ítem 1)
# ---------------------------------------------------------------------------
def pedir_ruta_csv() -> str:
    """
    Pide por consola la ruta de un archivo CSV. Con Enter (texto vacío)
    se cancela. Si el archivo no existe, el error se informa al cargarlo.

    Retorno:
        str: ruta del archivo, o "" si se canceló.
    """
    mensaje = "Ingrese la ruta del archivo CSV (Enter para cancelar): "
    ruta = input(mensaje).strip().strip('"')

    return ruta


def leer_lineas(ruta: str) -> list:
    """
    Lee todas las líneas de un archivo de texto.

    Argumentos:
        ruta (str): ruta del archivo.

    Retorno:
        list: líneas del archivo.
    """
    lineas = []

    with open(ruta, "r") as archivo:
        for linea in archivo:
            lineas.append(linea)

    return lineas


def es_registro_valido(campos: list) -> bool:
    """
    Valida los campos de una línea del CSV con las mismas funciones de
    validación que se usan en la carga manual. El orden de los campos
    es: legajo, nombre, género, una nota por materia y promedio.

    Argumentos:
        campos (list): textos de cada columna de la línea.

    Retorno:
        bool: True si todos los campos son válidos, False en caso
              contrario.
    """
    retorno = False

    if len(campos) == CANTIDAD_MATERIAS + 4:
        retorno = es_legajo(campos[0]) and es_alfabetico(campos[1]) and \
            es_genero(campos[2]) and es_promedio(campos[-1])

        for j in range(3, 3 + CANTIDAD_MATERIAS):
            if es_nota(campos[j]) == False:
                retorno = False
                break

    return retorno


def crear_estudiante_desde_campos(campos: list) -> dict:
    """
    Arma el diccionario de un estudiante a partir de los campos (ya
    validados) de una línea del CSV.

    Argumentos:
        campos (list): textos de cada columna de la línea.

    Retorno:
        dict: estudiante con las claves legajo, nombre, genero, notas y
              promedio.
    """
    notas = [0] * CANTIDAD_MATERIAS

    for j in range(CANTIDAD_MATERIAS):
        notas[j] = int(campos[3 + j])

    promedio = float(campos[-1])

    if promedio == 0:
        promedio = 0
    else:
        promedio = round(promedio, 2)

    estudiante = {
        "legajo": int(campos[0]),
        "nombre": campos[1],
        "genero": campos[2],
        "notas": notas,
        "promedio": promedio
    }

    return estudiante


def cargar_desde_csv(ruta: str) -> list:
    """
    Carga los estudiantes de un archivo CSV en una nueva lista de
    diccionarios. Cada línea tiene el formato:
    legajo,nombre,genero,n1,n2,n3,n4,n5,promedio
    Las líneas vacías se ignoran y las líneas con datos inválidos se
    rechazan, informando su número.

    Argumentos:
        ruta (str): ruta del archivo CSV.

    Retorno:
        list: lista de diccionarios con los estudiantes válidos (vacía
              si no había datos válidos).
    """
    estudiantes = []
    rechazadas = 0

    lineas = leer_lineas(ruta)

    for i in range(len(lineas)):
        linea = lineas[i].strip()

        if linea != "":
            campos = linea.split(",")

            for j in range(len(campos)):
                campos[j] = campos[j].strip()

            if es_registro_valido(campos):
                estudiantes.append(crear_estudiante_desde_campos(campos))
            else:
                rechazadas += 1
                print(f"Línea {i + 1} rechazada (datos inválidos): {linea}")

    if rechazadas > 0:
        print(f"Se rechazaron {rechazadas} línea/s.")

    return estudiantes


# ---------------------------------------------------------------------------
# GUARDADO EN ARCHIVO JSON (ítem 11)
# ---------------------------------------------------------------------------
def pedir_nombre_json() -> str:
    """
    Pide por consola el nombre, sin extensión, del archivo JSON donde
    guardar los datos y lo valida (es obligatorio ingresar uno). Al
    nombre se le agrega siempre la extensión .json.

    Retorno:
        str: nombre del archivo, con la extensión .json.
    """
    mensaje = "Ingrese el nombre del archivo, sin extensión: "
    nombre = input(mensaje).strip().strip('"')

    while es_nombre_archivo(nombre) == False:
        print('Error. Ingrese un nombre válido (no puede estar vacío ni contener \\ / : * ? " < > |).')
        nombre = input(mensaje).strip().strip('"')

    return nombre + ".json"


def guardar_json(estudiantes: list, nombre: str) -> None:
    """
    Guarda la lista de diccionarios en un archivo JSON.

    Argumentos:
        estudiantes (list): lista de diccionarios de estudiantes.
        nombre (str): nombre del archivo a escribir (con extensión).

    Retorno:
        None: crea (o reemplaza) el archivo.
    """
    with open(nombre, "w") as archivo:
        json.dump(estudiantes, archivo, indent=2, ensure_ascii=False)


# ---------------------------------------------------------------------------
# MENÚ
# ---------------------------------------------------------------------------
def mostrar_menu() -> None:
    """
    Muestra por consola las opciones del menú principal.
    """
    print("\n--- MENU DE ESTUDIANTES ---")
    print("1. Cargar datos desde un archivo CSV")
    print("2. Cargar datos manualmente")
    print("3. Normalizar los textos a mayúsculas")
    print("4. Mostrar todos los estudiantes")
    print("5. Calcular promedios")
    print("6. Mostrar estudiantes ordenados por promedio")
    print("7. Mostrar estudiantes con promedio menor a 4")
    print("8. Mostrar materia/s con mayor promedio general")
    print("9. Buscar estudiante por legajo")
    print("10. Repetición de calificaciones en una materia")
    print("11. Guardar los datos en un archivo JSON")
    print("12. Salir")


def opcion_cargar_csv() -> list:
    """
    Ítem 1 del menú: pide por consola el nombre del archivo CSV, lo
    guarda en una variable y carga los estudiantes en una nueva lista de
    diccionarios.

    Retorno:
        list: lista de estudiantes cargados (vacía si se canceló o si
              el archivo no tenía datos válidos).
    """
    ruta = pedir_ruta_csv()
    estudiantes = []

    if ruta == "":
        print("Carga cancelada.")
    else:
        estudiantes = cargar_desde_csv(ruta)

        if len(estudiantes) == 0:
            print("No se cargó ningún estudiante.")
        else:
            print(f"Se cargaron {len(estudiantes)} estudiante/s desde el archivo.")

    return estudiantes


def opcion_cargar_manual(estudiantes: list) -> list:
    """
    Ítem 2 del menú: pide la cantidad de estudiantes y carga y valida
    manualmente los datos de cada uno. Los nuevos estudiantes se
    AGREGAN a los que ya estaban cargados (sin superar el máximo).

    Argumentos:
        estudiantes (list): lista de diccionarios ya cargados (puede
                            estar vacía).

    Retorno:
        list: la misma lista, con los estudiantes nuevos al final.
    """
    disponibles = CANTIDAD_ESTUDIANTES - len(estudiantes)

    if disponibles == 0:
        print(f"Error. Ya se cargó el máximo de {CANTIDAD_ESTUDIANTES} estudiantes.")
    else:
        cantidad = cargar_cantidad(disponibles)
        nuevos = crear_lista_estudiantes(cantidad)

        cargar_estudiantes(nuevos)

        for i in range(len(nuevos)):
            estudiantes.append(nuevos[i])

    return estudiantes


def opcion_normalizar(estudiantes: list) -> list:
    """
    Ítem 3 del menú: pasa a mayúsculas los datos de tipo str (nombre y
    género) de todos los estudiantes, bajo el paradigma funcional.

    Argumentos:
        estudiantes (list): lista de diccionarios de estudiantes.

    Retorno:
        list: NUEVA lista de estudiantes normalizados.
    """
    normalizados = normalizar_estudiantes(estudiantes)

    print("Los nombres y géneros se convirtieron a mayúsculas.")

    return normalizados


def opcion_mostrar_estudiantes(estudiantes: list) -> None:
    """
    Ítem 4 del menú: muestra el informe con todos los estudiantes.

    Argumentos:
        estudiantes (list): lista de diccionarios de estudiantes.

    Retorno:
        None.
    """
    mostrar_estudiantes(estudiantes)


def opcion_calcular_promedios(estudiantes: list) -> list:
    """
    Ítem 5 del menú: calcula el promedio de cada estudiante (lambda y
    map), lo guarda en su diccionario y lo muestra.

    Argumentos:
        estudiantes (list): lista de diccionarios de estudiantes.

    Retorno:
        list: NUEVA lista de estudiantes con el promedio calculado.
    """
    con_promedio = calcular_promedios(estudiantes)

    print("\n--- PROMEDIOS DE LOS ESTUDIANTES ---")
    mostrar_promedios(con_promedio)

    return con_promedio


def opcion_mostrar_ordenados(estudiantes: list) -> None:
    """
    Ítem 6 del menú: pide el sentido del orden (ASC o DESC, en mayúscula
    o minúscula), ordena a
    los estudiantes por promedio y muestra el informe.

    Argumentos:
        estudiantes (list): lista de diccionarios de estudiantes (con
                            el promedio ya calculado).

    Retorno:
        None: modifica la lista original (queda ordenada).
    """
    orden = normalizar_texto(input("Ingrese el orden (ASC o DESC): "))

    while orden != "ASC" and orden != "DESC":
        print('Error. Ingrese "ASC" o "DESC".')
        orden = normalizar_texto(input("Ingrese el orden (ASC o DESC): "))

    ordenar_por_promedio(estudiantes, orden)
    mostrar_estudiantes(estudiantes)


def opcion_filtrar_desaprobados(estudiantes: list) -> None:
    """
    Ítem 7 del menú: filtra (filter) y muestra los estudiantes cuyo
    promedio es menor a cuatro.

    Argumentos:
        estudiantes (list): lista de diccionarios de estudiantes (con
                            el promedio ya calculado).

    Retorno:
        None.
    """
    desaprobados = filtrar_desaprobados(estudiantes)

    if len(desaprobados) == 0:
        print(f"No hay estudiantes con promedio menor a {PROMEDIO_APROBACION}.")
    else:
        mostrar_estudiantes(desaprobados, "TODOS", None,
                            f"ESTUDIANTES CON PROMEDIO MENOR A {PROMEDIO_APROBACION}")


def opcion_mayor_promedio_materia(estudiantes: list) -> None:
    """
    Ítem 8 del menú: calcula el promedio general de cada materia y
    muestra la/s materia/s con mayor promedio.

    Argumentos:
        estudiantes (list): lista de diccionarios de estudiantes.

    Retorno:
        None.
    """
    promedios_materias = calcular_promedios_materias(estudiantes)
    mayor = buscar_mayor(promedios_materias)

    mostrar_materias(promedios_materias, "MAYOR", mayor)


def opcion_buscar_estudiante(estudiantes: list) -> None:
    """
    Ítem 9 del menú: pide un legajo y muestra los datos del estudiante
    junto con su promedio.

    Argumentos:
        estudiantes (list): lista de diccionarios de estudiantes (con
                            el promedio ya calculado).

    Retorno:
        None.
    """
    legajo_buscar = cargar_legajo()

    buscar_estudiante(estudiantes, legajo_buscar)


def opcion_contar_calificaciones(estudiantes: list) -> None:
    """
    Ítem 10 del menú: pide el número de una materia y muestra cuántas
    veces se repite cada calificación en ella.

    Argumentos:
        estudiantes (list): lista de diccionarios de estudiantes.

    Retorno:
        None.
    """
    materia = cargar_materia(len(estudiantes[0]["notas"]))
    cantidades = contar_calificaciones(estudiantes, materia)

    mostrar_repeticiones(cantidades, materia)


def opcion_guardar_json(estudiantes: list) -> None:
    """
    Ítem 11 del menú: pide el nombre de un archivo y guarda en él la
    lista de diccionarios en formato JSON.

    Argumentos:
        estudiantes (list): lista de diccionarios de estudiantes.

    Retorno:
        None.
    """
    nombre = pedir_nombre_json()

    guardar_json(estudiantes, nombre)
    print(f"Datos guardados en '{nombre}'.")


def opcion_salir() -> None:
    """
    Ítem 12 del menú: informa que el programa finaliza.
    """
    print("Saliendo del programa...")


def menu(estudiantes: list, datos_cargados: bool = False) -> None:
    """
    Controla el flujo del programa: muestra el menú, valida que se
    hayan cargado los datos (y calculado los promedios cuando
    corresponde) y llama a la función de cada ítem. Las cargas de los
    ítem 1 reemplaza la lista de estudiantes, el ítem 2 agrega estudiantes
    a la lista, y los ítems 3 y 5
    la reemplazan por una nueva lista (programación funcional).

    Argumentos:
        estudiantes (list): lista de diccionarios de estudiantes.
        datos_cargados (bool): True si la lista ya viene con datos (por
                               ejemplo, datos hardcodeados para
                               pruebas). Por defecto es False.

    Retorno:
        None.
    """
    opcion = ""
    promedios_calculados = False

    while opcion != "12":
        mostrar_menu()
        opcion = input("Ingrese una opcion: ")

        if opcion in ["3", "4", "5", "6", "7", "8", "9", "10", "11"] and datos_cargados == False:
            print("Primero debe cargar los datos.")

        elif opcion in ["6", "7", "9"] and promedios_calculados == False:
            print("Primero debe calcular los promedios.")

        else:
            match opcion:

                case "1":
                    cargados = opcion_cargar_csv()

                    if len(cargados) > 0:
                        for i in range(len(cargados)):
                            estudiantes.append(cargados[i])

                        datos_cargados = True
                        # Hay estudiantes sin promedio: hay que volver a calcular
                        promedios_calculados = False

                case "2":
                    estudiantes = opcion_cargar_manual(estudiantes)
                    datos_cargados = len(estudiantes) > 0
                    # Hay estudiantes sin promedio: hay que volver a calcular
                    promedios_calculados = False

                case "3":
                    estudiantes = opcion_normalizar(estudiantes)

                case "4":
                    opcion_mostrar_estudiantes(estudiantes)

                case "5":
                    estudiantes = opcion_calcular_promedios(estudiantes)
                    promedios_calculados = True

                case "6":
                    opcion_mostrar_ordenados(estudiantes)

                case "7":
                    opcion_filtrar_desaprobados(estudiantes)

                case "8":
                    opcion_mayor_promedio_materia(estudiantes)

                case "9":
                    opcion_buscar_estudiante(estudiantes)

                case "10":
                    opcion_contar_calificaciones(estudiantes)

                case "11":
                    opcion_guardar_json(estudiantes)

                case "12":
                    opcion_salir()

                case _:
                    print("Opcion invalida.")
