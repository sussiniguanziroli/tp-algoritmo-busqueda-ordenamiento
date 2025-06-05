import json #importo la herramienta para leer formato
import matplotlib.pyplot as plt #importo la libreria de matplotlib para graficar la diferencia de tiempos
import timeit #importo la libreria de timeit para calcular los tiempos de ejecucion``````````````````````````````````````````````````````````````````````````````````````````````````

#uso la funcion json.load para asignar la data del json a una lista de python
with open('productos.json', 'r', encoding='utf-8') as file:
    productos = json.load(file) 

#########procedo a ordenar la larga lista de productos con varias tecnicas por nombre:

#insertion sort, algortimo de ordenamiento por incersion en la lista de productos, devuelve el "objeto" entero

def insertion_sort_por_nombre(lista):
    for i in range(1, len(lista)):
        elemento = lista[i]
        j = i - 1
        # mueve elementos mayores que el actual hacia la derecha, con su indice
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

#QuickSort por nombre para la lista productos

def quicksort_por_nombre(lista):
    if len(lista) <= 1:
        return lista
    pivote = lista[-1]["name"].lower() #empieza por el ultimo elemento
    menores = [x for x in lista[:-1] if x["name"].lower() <= pivote]
    mayores = [x for x in lista[:-1] if x["name"].lower() > pivote]
    return quicksort_por_nombre(menores) + [lista[-1]] + quicksort_por_nombre(mayores) #se divide recursivamente para generar la lista resultante hasta que se procede a repasar cada elemento

# Tiempo de ejecución ordenamiento quicksort por nombre
comienzo = timeit.default_timer()
productos_ordenados_por_nombre_quicksort = quicksort_por_nombre(productos)
fin = timeit.default_timer()
tiempo_quicksort_por_nombre = fin - comienzo
#print(productos_ordenados_por_nombre_quicksort)

#BubbleSort por nombre

def bubble_sort_por_nombre(lista): #recontramil lento util para comparativa
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

########### ordeno por precio con varias tecnicas:

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





tipos_ordenamiento_por_nombre = ['Insertion Sort', 'QuickSort', 'Bubble Sort']
tiempos_por_nombre = [tiempo_insertion_sort_por_nombre, tiempo_quicksort_por_nombre, tiempo_bubble_sort_por_nombre]

plt.bar(tipos_ordenamiento_por_nombre, tiempos_por_nombre, color=['blue', 'green', 'red'])
plt.title('Comparativa de tiempo de ordenamiento por nombre')
plt.ylabel('Tiempo (segundos)')
plt.show()


tipos_ordenamiento_por_precio = ['QuickSort', 'Bubble Sort']
tiempos_por_precio = [tiempo_quicksort_por_precio, tiempo_bubble_sort_por_precio]

plt.bar(tipos_ordenamiento_por_precio, tiempos_por_precio, color=['violet', 'yellow'])
plt.title('Comparativa de tiempo de ordenamiento por precio')
plt.ylabel('Tiempo (segundos)')
plt.show()