import json 
import matplotlib.pyplot as plt 
import timeit 

# Uso de la funcion json.load para asignar datos del archivo json a una lista
with open('productos.json', 'r', encoding='utf-8') as file:
    productos = json.load(file) 

# Se procede a ordenar la lista de productos con distintos metodos de ordenamiento por nombre:

# Insertion-sort, algortimo de ordenamiento por incersion en la lista de productos, devuelve el "objeto" entero.
def insertion_sort_por_nombre(lista):
    for i in range(1, len(lista)):
        elemento = lista[i]
        j = i - 1
        # Mueve los elementos mayores que el actual hacia la derecha, con su indice
        while j >= 0 and lista[j]["name"].lower() > elemento["name"].lower():
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = elemento

# Tiempo de ejecución ordenamiento insertion_sort por nombre
comienzo = timeit.default_timer()
productos_ordenados_por_nombre_insertion = insertion_sort_por_nombre(productos)
fin = timeit.default_timer()
tiempo_insertion_sort_por_nombre = fin - comienzo
##print(productos_ordenados_por_nombre_insertion)

# Se aplica QuickSort por nombre a la lista productos
def quicksort_por_nombre(lista):
    if len(lista) <= 1:
        return lista
    pivote = lista[-1]["name"].lower() #empieza por el ultimo elemento
    menores = [x for x in lista[:-1] if x["name"].lower() <= pivote]
    mayores = [x for x in lista[:-1] if x["name"].lower() > pivote]
    return quicksort_por_nombre(menores) + [lista[-1]] + quicksort_por_nombre(mayores) # Se divide recursivamente para generar la lista resultante hasta que se procede a repasar cada elemento

# Tiempo de ejecución ordenamiento quicksort por nombre
comienzo = timeit.default_timer()
productos_ordenados_por_nombre_quicksort = quicksort_por_nombre(productos)
fin = timeit.default_timer()
tiempo_quicksort_por_nombre = fin - comienzo
#print(productos_ordenados_por_nombre_quicksort)


# Se aplica Bubble-Sort por nombre
def bubble_sort_por_nombre(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j]["name"].lower() > lista[j + 1]["name"].lower():
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

# Tiempo de ejecución ordenamiento bubble_sort por nombre
comienzo = timeit.default_timer()
productos_ordenados_por_nombre_bubble_sort = bubble_sort_por_nombre(productos)
fin = timeit.default_timer()
tiempo_bubble_sort_por_nombre = fin - comienzo
#print(productos_ordenados_por_nombre_bubble_sort) 

# Se realiza ordenamiento por precio con distintos tipos de algoritmos:

def quicksort_por_precio(lista): #mismo quicksort pero cambiando el nombre del parametro
    if len(lista) <= 1:
        return lista
    pivote = lista[-1]["price"] 
    menores = [x for x in lista[:-1] if x["price"] <= pivote]
    mayores = [x for x in lista[:-1] if x["price"] > pivote]
    return quicksort_por_precio(menores) + [lista[-1]] + quicksort_por_precio(mayores)

# Tiempo de ejecución ordenamiento quicksort por precio
comienzo = timeit.default_timer()
productos_ordenados_por_precio_quicksort = quicksort_por_precio(productos)
fin = timeit.default_timer()
tiempo_quicksort_por_precio = fin - comienzo
#print(productos_ordenados_por_precio_quicksort[:5]) #corto en 5 para checkear mas facil

def bubble_sort_por_precio(lista): #recontra lento jaja
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j]["price"] > lista[j + 1]["price"]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

# Tiempo de ejecución ordenamiento bubble_sort por precio
comienzo = timeit.default_timer()
productos_ordenados_por_precio_bubble_sort = bubble_sort_por_precio(productos)
fin = timeit.default_timer()
tiempo_bubble_sort_por_precio = fin - comienzo
#print(productos_ordenados_por_precio_bubble_sort)


tipos_ordenamiento_por_nombre = ['Insertion Sort', 'QuickSort', 'Bubble Sort'] # Nombre columna 
tiempos_por_nombre = [tiempo_insertion_sort_por_nombre, tiempo_quicksort_por_nombre, tiempo_bubble_sort_por_nombre] # Valor a considerar

plt.bar(tipos_ordenamiento_por_nombre, tiempos_por_nombre, color=['blue', 'green', 'red']) # Se asigna color a columna
plt.title('Comparativa de tiempo de ordenamiento por nombre') # Titulo
plt.ylabel('Tiempo (segundos)') # Etiqueta eje Y
plt.show() # Se muestra el grafico


tipos_ordenamiento_por_precio = ['QuickSort', 'Bubble Sort'] # Nombre columna 
tiempos_por_precio = [tiempo_quicksort_por_precio, tiempo_bubble_sort_por_precio] # Valor a considerar

plt.bar(tipos_ordenamiento_por_precio, tiempos_por_precio, color=['violet', 'yellow']) # Se asigna color a columna
plt.title('Comparativa de tiempo de ordenamiento por precio') # Titulo
plt.ylabel('Tiempo (segundos)') # Etiqueta eje Y
plt.show() # Se muestra el grafico