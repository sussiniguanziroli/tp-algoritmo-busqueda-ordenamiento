import json #importo la herramienta para leer formato

#uso la funcion json.load para asignar la data del json a una lista de python
with open('productos.json', 'r', encoding='utf-8') as file:
    productos = json.load(file) 

def busqueda_lineal_por_nombre(lista_productos, nombre_buscado):
    for producto in lista_productos:
        if producto["name"].lower() == nombre_buscado.lower(): #agregamos la funcion .lower() para evitar el case sensitive
            return producto
    return None #si termina el recorrido sin encontrar
        
resultado_busqueda = busqueda_lineal_por_nombre(productos, "Johnnie Walker Red Label")
####print(resultado_busqueda)

#para efectuar una busqueda binaria por categoria, es decir, traer todos los vinos, debemos tener
#una lista ordenada primero, asi que procedemos a hacer un algoritmo de ordenamiento por categoria

productos_ordenados_por_categoria = sorted(productos, key=lambda x: x["category"])

def busqueda_binaria_por_categoria(lista_ordenada, categoria):
    izquierda = 0
    derecha = len(lista_ordenada) -1
    resultado_busqueda_binaria = []

    while izquierda <= derecha:
        centro = (izquierda + derecha) // 2
        if lista_ordenada[centro]["category"].lower() == categoria.lower():
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
        elif lista_ordenada[centro]["category"].lower() < categoria.lower():
            izquierda = centro + 1
        else:
            derecha = centro - 1
    return resultado_busqueda_binaria

todos_los_whiskies = busqueda_binaria_por_categoria(productos_ordenados_por_categoria, "whisky")
print(todos_los_whiskies)
