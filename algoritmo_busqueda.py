import json #importo la herramienta para leer formato
import matplotlib.pyplot as plt #importo la libreria de matplotlib para graficar la diferencia de tiempos
import timeit #importo la libreria de timeit para calcular los tiempos de ejecucion```

#uso la funcion json.load para asignar la data del json a una lista de python
with open('productos.json', 'r', encoding='utf-8') as file:
    productos = json.load(file) 

def busqueda_lineal_por_nombre(lista_productos, nombre_buscado):
    for producto in lista_productos:
        if producto["name"].lower() == nombre_buscado.lower(): #agregamos la funcion .lower() para evitar el case sensitive
            return producto
    return None #si termina el recorrido sin encontrar
        
# Tiempo de ejecución busqueda_lineal por nombre
comienzo = timeit.default_timer()        
resultado_busqueda = busqueda_lineal_por_nombre(productos, "Johnnie Walker Red Label")
fin = timeit.default_timer()
tiempo_busqueda_lineal_por_nombre = fin - comienzo
####print(resultado_busqueda)

#para efectuar una busqueda binaria por categoria, es decir, traer todos los vinos, debemos tener
#una lista ordenada primero, asi que procedemos a hacer un algoritmo de ordenamiento por categoria

#usamos un algoritmo MergeSort 

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
        #realizamos orden por categoria
        if izquierda[i]["category"].lower() <= derecha[j]["category"].lower():
            resultado_ordenado.append(izquierda[i])
            i += 1
        else:
            resultado_ordenado.append(derecha[j])
            j += 1
    resultado_ordenado.extend(izquierda[i:])
    resultado_ordenado.extend(derecha[j:])
    return resultado_ordenado

############ Fin MergeSort - ordena los productos por categoria, empezando todos los gin
#luego los ron, etc


productos_ordenados_por_categoria = merge_sort(productos)
#print(productos_ordenados_por_categoria)

## empieza la busqueda binaria, la cual se le pasa la lista ordenada MergeSort

def busqueda_binaria_por_categoria(lista_ordenada, categoria): #recibe la lista y la categoria que se quiere buscar
    #inicializamos los extremos, izquierda, derecha y el centro, que va a ser los extremos // 2
    izquierda = 0
    derecha = len(lista_ordenada) -1
    resultado_busqueda_binaria = []

    while izquierda <= derecha:
        centro = (izquierda + derecha) // 2
        if lista_ordenada[centro]["category"].lower() == categoria.lower(): #si el centro es de la categoria buscada, empieza la busqueda lineal hasta encontrarse con algo diferente hacia ambos lados
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
        elif lista_ordenada[centro]["category"].lower() < categoria.lower(): #si la categoria del centro es menor alfabeticamente que la buscada se descarta la mitad izquierda, ya que no podria estar ahi
            izquierda = centro + 1
        else: #mismo descarte pero si es mayor que la buscada
            derecha = centro - 1
    return resultado_busqueda_binaria

todos_los_whiskies = busqueda_binaria_por_categoria(productos_ordenados_por_categoria, "whisky")
#print(todos_los_whiskies)


########### mismo MergeSort por "nombre" para hacer la busqueda 100% binaria en la lista

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
        #realizamos orden por nombre
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
###print(productos_ordenados_por_nombre)

#ahora si la busqueda binaria por el nombre exacto

def busqueda_binaria_por_nombre(lista_ordenada, nombre_buscado):
    izquierda = 0
    derecha = len(lista_ordenada) - 1

    while izquierda <= derecha:
        centro = (izquierda + derecha) // 2
        nombre_centro = lista_ordenada[centro]["name"].lower()
        if nombre_centro == nombre_buscado.lower():
            return lista_ordenada[centro] #indice del elemento que buscamos si es justo el del centro
        elif nombre_centro < nombre_buscado.lower():
            izquierda = centro + 1
        else:
            derecha = centro - 1
    return None #si no existe el elemento que buscamos en toda la lista


# Tiempo de ejecución busqueda_binaria por nombre
comienzo = timeit.default_timer()   
resultado_busqueda_binaria_nombre = busqueda_binaria_por_nombre(productos_ordenados_por_nombre, "Johnnie Walker Red Label")
fin = timeit.default_timer()
tiempo_busqueda_binaria_por_nombre = fin - comienzo
##print(resultado_busqueda_binaria_nombre['name'])


tipos_busqueda_por_nombre = ['Busqueda Lineal', 'Busqueda Binaria']
tiempos_por_nombre = [tiempo_busqueda_lineal_por_nombre, tiempo_busqueda_binaria_por_nombre]

plt.bar(tipos_busqueda_por_nombre, tiempos_por_nombre, color=['violet', 'green'])
plt.title('Comparativa de tiempo de busqueda por nombre')
plt.ylabel('Tiempo (segundos)')
plt.show()
