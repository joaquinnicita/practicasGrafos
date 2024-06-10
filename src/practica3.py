def valida_nodo_en_grafo(grafo_lista, nodo):
    '''
    Dado un grafo en representacion de lista, y un nodo, me devuelve True si el nodo está en el Grafo
    Ejemplo Entrada: 
        (['A','B','C','D','E'],[('A','B'),('B','C'),('C','B'),('D','E')])
	'F'
    Ejemplo formato salida: 
        False '''
    vertices, _ = grafo_lista
    return nodo in vertices

def encuentra_camino(grafo_lista, nodo_ini, nodo_fin):
    '''
    Dado un grafo en representacion de lista, el nodo inicial y final de un camino
    Me devuelve una lista con los vértices del camino, o vacio si no existe
    Ejemplo Entrada: 
        (['a','b','c','d','e','f'],[('a','b'),('a','d'),('b','d'),('b','c'),('c','d'),('c','e'),('d','e'),('c','f')])
	a
	b
    Ejemplo retorno: 
        ['a','b','d','c','e','d','b']
    '''
    vertices, aristas = grafo_lista
    grafo = {vertice: [] for vertice in vertices}
    for v1, v2 in aristas:
        grafo[v1].append(v2)
        grafo[v2].append(v1)

    cola = [(nodo_ini, [nodo_ini])]
    while cola:
        (vertice, camino) = cola.pop(0)
        for siguiente in set(grafo[vertice]) - set(camino):
            if siguiente == nodo_fin:
                return camino + [siguiente]
            else:
                cola.append((siguiente, camino + [siguiente]))
    return []

def encuentra_camino_cerrado(grafo_lista, nodo):
    '''
    Ejemplo Entrada: 
        (['a','b','c','d','e','f'],[('a','b'),('a','d'),('b','d'),('b','c'),('c','d'),('c','e'),('d','e'),('c','f')])
	a
    Ejemplo retorno: 
        ['a','b','c','d','a']
    '''
    vertices, aristas = grafo_lista
    grafo = {vertice: [] for vertice in vertices}
    for v1, v2 in aristas:
        grafo[v1].append(v2)
        grafo[v2].append(v1)

    camino = []
    visitados = {vertice: False for vertice in vertices}

    def dfs(nodo_actual, nodo_padre):
        visitados[nodo_actual] = True
        camino.append(nodo_actual)
        for vecino in grafo[nodo_actual]:
            if not visitados[vecino]:
                if dfs(vecino, nodo_actual):
                    return True
            elif vecino != nodo_padre or nodo_actual == nodo:
                return True
        camino.pop()
        return False

    if dfs(nodo, None):
        camino.append(nodo)  # Para cerrar el ciclo
        return camino
    else:
        return []

def encuentra_recorrido(grafo_lista, nodo_ini, nodo_fin):
    '''
    Ejemplo Entrada: 
        (['a','b','c','d','e','f'],[('a','b'),('a','d'),('b','d'),('b','c'),('c','d'),('c','e'),('d','e'),('c','f')])
	b
	f
    Ejemplo retorno: 
        ['b','c','d','e','c','f']
    '''

    grafo = {nodo: [] for nodo in grafo_lista}
    for origen, destino in aristas:
        grafo[origen].append(destino)
    
    # Función auxiliar para realizar la búsqueda en profundidad (DFS)
    def dfs(nodo_actual, nodo_fin, camino, visitados):
        if nodo_actual == nodo_fin:  # Caso base: llegamos al nodo final
            return camino
        visitados.add(nodo_actual)
        for vecino in grafo[nodo_actual]:
            if vecino not in visitados:  # Evitar ciclos revisando si ya visitamos el nodo
                resultado_camino = dfs(vecino, nodo_fin, camino + [vecino], visitados)
                if resultado_camino:  # Si encontramos un camino, retornarlo
                    return resultado_camino
        return []  # Si no hay camino, retornar lista vacía

def encuentra_circuito(grafo_lista, nodo):
    '''
    Ejemplo Entrada: 
        (['a','b','c','d','e','f'],[('a','b'),('a','d'),('b','d'),('b','c'),('c','d'),('c','e'),('d','e'),('c','f')])
    d
    Ejemplo retorno: 
        ['d','a','b','d','c','e','d']
    '''
    vertices, aristas = grafo_lista
    grafo = {vertice: [] for vertice in vertices}
    for v1, v2 in aristas:
        grafo[v1].append(v2)
        grafo[v2].append(v1)

    camino = []
    visitados = {vertice: False for vertice in vertices}

    def dfs(nodo_actual):
        visitados[nodo_actual] = True
        camino.append(nodo_actual)
        if nodo_actual == nodo and len(camino) > 1:
            return True
        for vecino in grafo[nodo_actual]:
            if not visitados[vecino] and dfs(vecino):
                return True
        camino.pop()
        return False

    if dfs(nodo):
        return camino
    else:
        return []	 	

def encuentra_camino_simple(grafo_lista, nodo_ini, nodo_fin):
    '''
    Ejemplo Entrada: 
        (['a','b','c','d','e','f'],[('a','b'),('a','d'),('b','d'),('b','c'),('c','d'),('c','e'),('d','e'),('c','f')])
	d
    Ejemplo retorno: 
        ['a','b','c','d']
    '''
    vertices, aristas = grafo_lista
    grafo = {vertice: [] for vertice in vertices}
    for v1, v2 in aristas:
        grafo[v1].append(v2)
        grafo[v2].append(v1)

    camino = []
    visitados = {vertice: False for vertice in vertices}

    def dfs(nodo_actual):
        visitados[nodo_actual] = True
        camino.append(nodo_actual)
        if nodo_actual == nodo_fin:
            return True
        for vecino in grafo[nodo_actual]:
            if not visitados[vecino] and dfs(vecino):
                return True
        camino.pop()
        return False

    if dfs(nodo_ini):
        return camino
    else:
        return []

def encuentra_ciclo(grafo_lista, nodo):
    '''
    Ejemplo Entrada: 
        (['a','b','c','d','e','f'],[('a','b'),('a','d'),('b','d'),('b','c'),('c','d'),('c','e'),('d','e'),('c','f')])
	d
    Ejemplo retorno: 
        ['a','b','c','d','a']
    '''
    vertices, aristas = grafo_lista
    grafo = {vertice: [] for vertice in vertices}
    for v1, v2 in aristas:
        grafo[v1].append(v2)
        grafo[v2].append(v1)

    camino = []
    visitados = {vertice: False for vertice in vertices}

    def dfs(nodo_actual, nodo_padre):
        visitados[nodo_actual] = True
        camino.append(nodo_actual)
        for vecino in grafo[nodo_actual]:
            if not visitados[vecino]:
                if dfs(vecino, nodo_actual):
                    return True
            elif vecino != nodo_padre or nodo_actual == nodo:
                return True
        camino.pop()
        return False

    if dfs(nodo, None):
        camino.append(nodo)  # Para cerrar el ciclo
        return camino
    else:
        return []

def determina_caminos(camino_lista):
    '''
    Dado una lista que representa un camino, camino cerrado, recorrido, circuito, camino simple o ciclo,
    me devuelva de qué se trata
    Ejemplo Entrada: 
        ['d','a','b','d','c','e','d']
    Ejemplo formato salida: 
        Circuito

    '''
    if len(camino_lista) < 2:
        return "Camino inválido"
    if camino_lista[0] != camino_lista[-1]:
        return "Camino simple"
    if len(set(camino_lista)) == len(camino_lista):
        return "Camino cerrado"
    if len(set(camino_lista)) < len(camino_lista):
        return "Recorrido"
    if camino_lista[0] == camino_lista[-1] and len(set(camino_lista)) == len(camino_lista) - 1:
        return "Circuito"
    if camino_lista.count(camino_lista[0]) > 2 or any(camino_lista.count(nodo) > 2 for nodo in camino_lista):
        return "Ciclo"
