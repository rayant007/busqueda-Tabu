import random

def generar_vecinos(solucion_actual, rango=(-10, 10), num_vecinos=5):
    """Genera vecinos de una solución actual.
    
    Args:
    solucion_actual (int): La solución actual.
    rango (tuple): El rango en el que los vecinos se generan.
    num_vecinos (int): Número de vecinos a generar.

    Returns:
    list: Una lista de vecinos generados.
    """
    vecinos = []
    for _ in range(num_vecinos):
        vecino = solucion_actual + random.randint(rango[0], rango[1])
        vecinos.append(vecino)
    return vecinos

def funcion_objetivo(x):
    """Función objetivo para minimizar.
    
    Args:
    x (int): La variable de entrada.

    Returns:
    int: El valor de la función objetivo.
    """
    return x ** 2  # Por ejemplo, minimizamos la función cuadrática x^2

def busqueda_tabu(max_iteraciones=100, lista_tabu_tamano=5, num_vecinos=5):
    """Algoritmo de búsqueda tabú para minimizar una función objetivo.

    Args:
    max_iteraciones (int): Número máximo de iteraciones.
    lista_tabu_tamano (int): Tamaño de la lista tabú.
    num_vecinos (int): Número de vecinos a generar por iteración.

    Returns:
    tuple: Mejor solución encontrada y su valor de función objetivo.
    """
    # Inicializar solución
    solucion_actual = random.randint(-100, 100)
    mejor_solucion = solucion_actual
    mejor_valor = funcion_objetivo(solucion_actual)

    # Inicializar lista tabú
    lista_tabu = []

    for iteracion in range(max_iteraciones):
        # Generar vecinos de la solución actual
        vecinos = generar_vecinos(solucion_actual, num_vecinos=num_vecinos)
        
        # Seleccionar el mejor vecino no tabú
        mejor_vecino = None
        mejor_valor_vecino = float('inf')
        for vecino in vecinos:
            if vecino not in lista_tabu and funcion_objetivo(vecino) < mejor_valor_vecino:
                mejor_vecino = vecino
                mejor_valor_vecino = funcion_objetivo(vecino)
        
        # Actualizar la solución actual
        if mejor_vecino is not None:
            solucion_actual = mejor_vecino
            if mejor_valor_vecino < mejor_valor:
                mejor_solucion = mejor_vecino
                mejor_valor = mejor_valor_vecino

        # Actualizar lista tabú
        lista_tabu.append(solucion_actual)
        if len(lista_tabu) > lista_tabu_tamano:
            lista_tabu.pop(0)

        # Imprimir el estado de la búsqueda
        print(f"Iteración {iteracion}: Mejor solución = {mejor_solucion}, Valor de la función objetivo = {mejor_valor}")

    return mejor_solucion, mejor_valor

# Ejecutar el algoritmo de búsqueda tabú
mejor_solucion, mejor_valor = busqueda_tabu()
print(f"\nMejor solución encontrada: {mejor_solucion} con valor de función objetivo: {mejor_valor}")
