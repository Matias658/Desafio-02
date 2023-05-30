import os
from data_stark import *
#**************************************************DESAFÍO 02***************************************************************************
#*************************************************EJERCICIO 1***************************************************************************
#Normalizar datos
def stark_normalizar_datos(lista:list, key:str, tipo):
    lista_normalizada = []
    contador = 0
    if lista:
        try:
            for item in lista:
                if item:
                    if type(item[key]) != tipo:
                        item[key] = tipo(item[key])
                        lista_normalizada.append(item)
                        contador += 1
                    else:
                        print(f"El dato ya es de tipo {tipo}")
                        break
            if contador > 0:
                print("Datos normalizados")
            return lista_normalizada
        except ValueError:
            print("No se puede normalizar ese dato.")
    else:
        print("Error: Lista de héroes vacía")
#--------------------------------------------------------------------------------------------------------------------------------------
# 1.1. Crear la función 'obtener_nombre' la cual recibirá por parámetro un diccionario el cual representara a un héroe y devolverá un string el cual
# contenga su nombre formateado de la siguiente manera:
# Nombre: Howard the Duck
def obtener_nomber(heroe:dict):
    nombre = f"Nombre: {heroe['nombre']}"
    return nombre
#--------------------------------------------------------------------------------------------------------------------------------------
# 1.2. Crear la función 'imprimir_dato' la cual recibirá por parámetro un string y deberá imprimirlo en la consola. La función no tendrá retorno.
def imprimir_dato(dato:str):
    if type(dato) == str:
        print(dato)
#--------------------------------------------------------------------------------------------------------------------------------------
# 1.3. Crear la función 'stark_imprimir_nombres_heroes' la cual recibirá por parámetro la lista de héroes y deberá imprimirla en la consola. Reutilizar las
# funciones hechas en los puntos 1.1 y 1.2. Validar que la lista no esté vacía para realizar sus acciones, caso contrario no hará nada y retornara -1.

def stark_imprimir_nombre_heroes(lista:list):
    if lista:
        for heroe in lista:
            nombre = obtener_nomber(heroe)
            imprimir_dato(nombre)
    else:
        return -1
#--------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------
#*************************************************EJERCICIO 2**************************************************************************
# 2. Crear la función 'obtener_nombre_y_dato' la misma recibirá por parámetro un diccionario el cual representara a un héroe y una key (string) la cual
# representará el dato que se desea obtener.
# ● La función deberá devolver un string el cual contenga el nombre y dato (key) del héroe a imprimir. El dato puede ser 'altura', 'fuerza', 'peso' O CUALQUIER OTRO DATO.


def obtener_nombre_y_dato(heroe:dict, key:str):
    nombre = f"Nombre: {heroe['nombre']}  |  {key}: {heroe[key]}"
    return nombre
#--------------------------------------------------------------------------------------------------------------------------------------
# Crear la función 'stark_imprimir_nombres_alturas' la cual recibirá por
# parámetro la lista de héroes, la cual deberá iterar e imprimir sus nombres y
# alturas USANDO la función creada en el punto 2. Validar que la lista de héroes
# no esté vacía para realizar sus acciones, caso contrario no hará nada y
# retornara -1.

def stark_imprimir_nombres_alturas(lista:list):
    if lista:
        for heroe in lista:
            print(obtener_nombre_y_dato(heroe, "altura"))
    else:
        return -1
#--------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------
#*************************************************EJERCICIO 3, 4, 6, 7*****************************************************************
# 4.1. Crear la función 'calcular_max' la cual recibirá por parámetro la lista de héroes y una key (string) la cual representará el dato que deberá ser evaluado
# a efectos de determinar cuál es el máximo de la lista. Por ejemplo la función deberá poder calcular: el peso, la altura o fuerza máximas y retornar el héroe
# que tenga el dato más alto.

def calcular_max(lista:list, key:str):
    flag_valor_maxima = True
    valor_maxima = None
    for valor in lista:
        if flag_valor_maxima or float(valor[key]) > float(valor_maxima):
            valor_maxima = valor[key]
            heroe_alto = valor
            flag_valor_maxima = False
    return heroe_alto
#--------------------------------------------------------------------------------------------------------------------------------------
# 4.2. Crear la función 'calcular_min' la cual recibirá por parámetro la lista de héroes y una key (string) la cual representará el dato que deberá ser evaluado
# a efectos de determinar cuál es el mínimo de la lista. Por ejemplo la función deberá poder calcular: el peso, la altura o fuerza máximas y retornar el héroe
# que tenga el dato más bajo.

def calcular_min(lista:list, key:str):
    flag_valor_minima = True
    valor_minima = None
    for bajo in lista:
        if flag_valor_minima or float(valor_minima) > float(bajo[key]):
            valor_minima = bajo[key]
            heroe_bajo = bajo
            flag_valor_minima = False
    return heroe_bajo
#--------------------------------------------------------------------------------------------------------------------------------------
# 4.3. Crear la funcion 'calcular_max_min_dato' la cual recibira tres parámetros:
# ● La lista de héroes
# ● El tipo de cálculo a realizar: es un valor string que puede tomar los
# valores ‘maximo’ o ‘minimo’
# ● Un string que representa la key del dato a calcular, por ejemplo: ‘altura’,
# ‘peso’, ‘edad’, etc.
# La función deberá retornar el héroe que cumpla con la condición pedida.
# Reutilizar las funciones hechas en los puntos 4.1 y 4.2
# Ejemplo de llamada:
# calcular_max_min_dato(lista, "maximo", "edad")

def calcular_max_min_dato(lista:list, calculo:str, key:str):
    if calculo == "maximo":
        heroe = calcular_max(lista, key)
    elif calculo == "minimo":
        heroe = calcular_min(lista, key)
    else:
        print("Condición inválida")

    return heroe
#--------------------------------------------------------------------------------------------------------------------------------------
# 4.4. Crear la función 'stark_calcular_imprimir_heroe'
# La función deberá obtener el héroe que cumpla dichas condiciones, imprimir su nombre y el valor calculado. Reutilizar las funciones de los puntos:
# punto 1.2, punto: 2 y punto 4.3
# Validar que la lista de héroes no esté vacía para realizar sus acciones, caso contrario no hará nada y retornara -1.

def stark_calcular_imprimir_heroes(lista:list, calculo:str, key:str):
    if lista:
        heroe = calcular_max_min_dato(lista, calculo, key)
        return obtener_nombre_y_dato(heroe, key)
    else:
        return -1
#--------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------
#****************************************************EJERCICIO 5***********************************************************************
# 5.1. Crear la función 'sumar_dato_heroe' la cual recibirá como parámetro una
# lista de héroes y un string que representara el dato/key de los héroes que se
# requiere sumar. Validar que cada héroe sea tipo diccionario y que no sea un
# diccionario vacío antes de hacer la suma. La función deberá retorna la suma
# de todos los datos según la key pasada por parámetro
 
def sumar_dato_heroe(lista:list, key:str):
    suma_total = 0 
    for heroe in lista:
        if heroe:
            if type(heroe) == dict:
                suma_total += heroe[key]
    return suma_total
#--------------------------------------------------------------------------------------------------------------------------------------
# Crear la función ‘dividir’ la cual recibirá como parámetro dos números
# (dividendo y divisor). Se debe verificar si el divisor es 0, en caso de serlo,
# retornar 0, caso contrario realizar la división entre los parámetros y retornar el
# resultado

def dividir(num1:float, num2:float):
    if num2 == 0:
        return 0
    else:
        resultado = num1 / num2
        return resultado
#--------------------------------------------------------------------------------------------------------------------------------------    
# 5.3. Crear la función ‘calcular_promedio’ la cual recibirá como parámetro una
# lista de héroes y un string que representa el dato del héroe que se requiere
# calcular el promedio. La función debe retornar el promedio del dato pasado
# por parámetro

def calcular_promedio(lista:list, key:str):
    suma_total = sumar_dato_heroe(lista, key)
    promedio = dividir(suma_total, len(lista))
    return promedio
#--------------------------------------------------------------------------------------------------------------------------------------    
# Crear la función 'stark_calcular_imprimir_promedio_altura' la cual recibirá
# una lista de héroes y utilizando la función del punto 5.3 calcula y mostrará la
# altura promedio. Validar que la lista de héroes no esté vacía para realizar sus
# acciones, caso contrario no hará nada y retornara -1.
# IMPORTANTE: hacer uso de las las funciones creadas en los puntos 1.2, 5.1 y 5.3

def stark_calcular_imprimir_promedio_altura(lista:list, key:str):
    if lista:
        promedio = calcular_promedio(lista, key)
        return promedio
    else:
        return -1
#--------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------
#MENÚS :D
def imprimir_menu():
    os.system("cls")
    imprimir_dato("""***Bienvenidos a las Industrias Stark***
************Menu de Opciones************
1-Nombre de cada SuperHeroe
2-Nombre y alturas de cada SuperHeroe
3-Altura del SuperHeroe más alto
4-Altura del SuperHeroe más bajo
5-Altura promedio
6-SuperHeroe más pesado
7-SuperHeroe menos pesado
8-Siguiente menú
9-Salir""")
#--------------------------------------------------------------------------------------------------------------------------------------      
def validar_entero(num):
    try:
        int(num)
        entero = True
    except ValueError:
        entero = False
    
    return entero
#--------------------------------------------------------------------------------------------------------------------------------------
def stark_menu_principal():
    imprimir_menu()
    
    opcion =(input("Ingrese una opcion: "))

    if validar_entero(opcion):
        return int(opcion)
    else:
        return -1
#--------------------------------------------------------------------------------------------------------------------------------------
#Elegir opción 00
def stark_marvel_app(lista:list):
    opcion = stark_menu_principal()
    match opcion:
        case 1:
            stark_imprimir_nombre_heroes(lista)
        case 2:
            stark_normalizar_datos(lista, "altura", float)
            stark_imprimir_nombres_alturas(lista)
        case 3:
            stark_normalizar_datos(lista, "altura", float)
            heroe_alto = stark_calcular_imprimir_heroes(lista, "maximo", "altura")
            print(f"El heroe más alto es: {heroe_alto}")
        case 4:
            stark_normalizar_datos(lista, "altura", float)
            heroe_bajo = stark_calcular_imprimir_heroes(lista, "minimo", "altura")
            print(f"El heroe más bajo es: {heroe_bajo}")
        case 5:
            stark_normalizar_datos(lista, "altura", float)
            promedio = stark_calcular_imprimir_promedio_altura(lista, "altura")
            imprimir_dato(str(promedio))
        case 6:
            stark_normalizar_datos(lista, "peso", float)
            heroe_pesado = stark_calcular_imprimir_heroes(lista, "maximo", "peso")
            print(f"El heroe más pesado es: {heroe_pesado}")
        case 7:
            stark_normalizar_datos(lista, "peso", float)
            heroe_menos_pesado = stark_calcular_imprimir_heroes(lista, "minimo", "peso")
            print(f"El heroe menos pesado es: {heroe_menos_pesado}")
        case 8:
            print("*******Trabajando*******")
        case 9:
            y = input("Seguro que desea salir? s/n: ")
            return y
        case _:
            print("ERROR. Opción inválida. Reintente")
#--------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------
