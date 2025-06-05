import json
import matplotlib.pyplot as plt
import timeit

# Uso de la funcion json.load para asignar datos del archivo json a una lista
with open('productos.json', 'r', encoding='utf-8') as file:
    productos = json.load(file) 

def busqueda_lineal_por_nombre(lista_productos, nombre_buscado):
    for producto in lista_productos:
        if producto["name"].lower() == nombre_buscado.lower(): # Se agrega la funcion .lower() para evitar el case sensitive
            return producto
    return None # Si el se termina el recorrido sin encontrar
        
# Tiempo de ejecución busqueda_lineal por nombre
comienzo = timeit.default_timer()        
resultado_busqueda = busqueda_lineal_por_nombre(productos, "Johnnie Walker Red Label")
fin = timeit.default_timer()
tiempo_busqueda_lineal_por_nombre = fin - comienzo
### print(resultado_busqueda)

"""Para efectuar una busqueda binaria por categoria, es decir, traer todos los vinos, 
debemos tener una lista ordenada primero. Procedemos a hacer un algoritmo de ordenamiento por categoria. """

# Se utiliza un algoritmo MergeSort 
def merge_sort(productos_a_ordenar):
    if len(productos_a_ordenar) <= 1:
        return productos_a_ordenar
    
    centro = len(productos_a_ordenar) // 2
    izquierda = merge_sort(productos_a_ordenar[:centro])
    derecha = merge_sort(productos_a_ordenar[centro:])

    return merge(izquierda, derecha)

def merge(izquierda, derecha):
    resultado_ordenado = []
    i = j = 0

    while i < len(izquierda) and j < len(derecha):
        # Se realiza el orden por categoria
        if izquierda[i]["category"].lower() <= derecha[j]["category"].lower():
            resultado_ordenado.append(izquierda[i])
            i += 1
        else:
            resultado_ordenado.append(derecha[j])
            j += 1
    resultado_ordenado.extend(izquierda[i:])
    resultado_ordenado.extend(derecha[j:])
    return resultado_ordenado

""" Finaliza MergeSort: Se ordenaron los productos por categoria, comenzando con gin; luego ron, etc."""


productos_ordenados_por_categoria = merge_sort(productos)
### print(productos_ordenados_por_categoria)

# Se realiza la busqueda binaria; se pasa una lista ordenada -> MergeSort
def busqueda_binaria_por_categoria(lista_ordenada, categoria): # Recibe lista y categoria a buscar
    # Se inicializan los extremos, izquierda, derecha y el centro (extremos // 2 )
    izquierda = 0
    derecha = len(lista_ordenada) -1
    resultado_busqueda_binaria = []

    while izquierda <= derecha:
        centro = (izquierda + derecha) // 2
        if lista_ordenada[centro]["category"].lower() == categoria.lower(): # En caso de que la categoria centro sea la buscada, comienza busqueda lineal hacia ambos lados, hasta encontrar algo diferente 
            resultado_busqueda_binaria.append(lista_ordenada[centro])
            izquierda = centro - 1
            while izquierda >= 0 and lista_ordenada[izquierda]["category"].lower() == categoria.lower():
                resultado_busqueda_binaria.append(lista_ordenada[izquierda])
                izquierda -= 1
            derecha = centro + 1
            while derecha < len(lista_ordenada) and lista_ordenada[derecha]["category"].lower() == categoria.lower():
                resultado_busqueda_binaria.append(lista_ordenada[derecha])
                derecha += 1
            return resultado_busqueda_binaria
        elif lista_ordenada[centro]["category"].lower() < categoria.lower(): # Si la categoria del centro es menor alfabeticamente que la buscada se descarta la mitad izquierda, ya que no podria estar ahi
            izquierda = centro + 1
        else: # Idem paso anterior, pero se realiza el descarte si es mayor que la buscada
            derecha = centro - 1
    return resultado_busqueda_binaria

todos_los_whiskies = busqueda_binaria_por_categoria(productos_ordenados_por_categoria, "whisky")
### print(todos_los_whiskies)


# Se realiza MergeSort por "nombre" previo a realizar la busqueda binaria en la lista

def merge_sort_nombre(productos_a_ordenar):
    if len(productos_a_ordenar) <= 1:
        return productos_a_ordenar
    
    centro = len(productos_a_ordenar) // 2
    izquierda = merge_sort_nombre(productos_a_ordenar[:centro])
    derecha = merge_sort_nombre(productos_a_ordenar[centro:])

    return merge_por_nombre(izquierda, derecha)

def merge_por_nombre(izquierda, derecha):
    resultado_ordenado_por_nombre = []
    i = j = 0

    while i < len(izquierda) and j < len(derecha):
        # Se realiza el ordenamiento por nombre
        if izquierda[i]["name"].lower() <= derecha[j]["name"].lower():
            resultado_ordenado_por_nombre.append(izquierda[i])
            i += 1
        else:
            resultado_ordenado_por_nombre.append(derecha[j])
            j += 1
    resultado_ordenado_por_nombre.extend(izquierda[i:])
    resultado_ordenado_por_nombre.extend(derecha[j:])
    return resultado_ordenado_por_nombre

productos_ordenados_por_nombre = merge_sort_nombre(productos)
### print(productos_ordenados_por_nombre)

# Se realiza busqueda binaria por el nombre

def busqueda_binaria_por_nombre(lista_ordenada, nombre_buscado):
    izquierda = 0
    derecha = len(lista_ordenada) - 1

    while izquierda <= derecha:
        centro = (izquierda + derecha) // 2
        nombre_centro = lista_ordenada[centro]["name"].lower()
        if nombre_centro == nombre_buscado.lower():
            return lista_ordenada[centro] # Indice del elemento que buscamos, en caso de que sea justo el del centro
        elif nombre_centro < nombre_buscado.lower():
            izquierda = centro + 1
        else:
            derecha = centro - 1
    return None # Si no existe el elemento que buscamos en toda la lista


# Tiempo de ejecución busqueda_binaria por nombre
comienzo = timeit.default_timer()   
resultado_busqueda_binaria_nombre = busqueda_binaria_por_nombre(productos_ordenados_por_nombre, "Johnnie Walker Red Label")
fin = timeit.default_timer()
tiempo_busqueda_binaria_por_nombre = fin - comienzo
### print(resultado_busqueda_binaria_nombre['name'])


tipos_busqueda_por_nombre = ['Busqueda Lineal', 'Busqueda Binaria'] #Nombre columna 
tiempos_por_nombre = [tiempo_busqueda_lineal_por_nombre, tiempo_busqueda_binaria_por_nombre] # Valor a considerar

plt.bar(tipos_busqueda_por_nombre, tiempos_por_nombre, color=['violet', 'green']) # Se asigna color a columna
plt.title('Comparativa de tiempo de busqueda por nombre') # Titulo
plt.ylabel('Tiempo (segundos)') # Etiqueta eje Y
plt.show() # Se muestra el grafico