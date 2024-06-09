def cuenta_grado(grafo_lista):
    '''
    Muestra por pantalla los grados de los vertices de un grafo. 
    El argumento esta en formato de lista.
    
    Ejemplo Entrada: 
        (['A','B','C'],[('A','B'),('B','C'),('C','B')])
    Ejemplo retorno: 
        {'A': 1, 'B': 3, 'C': 2}
    '''
    vertices, aristas = grafo_lista 
    grados = {vertice: 0 for vertice in vertices}
    for arista in aristas:
        for vertice in arista:
            grados[vertice] += 1
    return grados
    

def vertice_aislado(grafo_lista):
    '''
    Dado un grafo en representacion de lista, obtiene una lista de los vértices aislado.
    Ejemplo Entrada: 
        (['A','B','C','D','E'],[('A','B'),('B','C'),('C','B')])
    Ejemplo formato salida: 
        ['D','E']
    '''
    vertices, aristas = grafo_lista
    vertices_aislados = vertices.copy()
    for arista in aristas:
        for vertice in arista:
            if vertice in vertices_aislados:
                vertices_aislados.remove(vertice)
    return vertices_aislados


def componentes_conexas(grafo_lista):
    '''
    Dado un grafo en representacion de lista, obtiene sus componentes conexas.
    Ejemplo Entrada: 
        (['A','B','C','D','E'],[('A','B'),('B','C'),('C','B'),('D','E')])
    Ejemplo formato salida: 
        [['A, 'B','C'], ['D','E']]
    '''
    vertices, aristas = grafo_lista
    visitados = {vertice: False for vertice in vertices}
    grafo = {vertice: [] for vertice in vertices}
    for v1, v2 in aristas:
        grafo[v1].append(v2)
        grafo[v2].append(v1)
    componentes = []

    def dfs(vertice, componente):
        visitados[vertice] = True
        componente.append(vertice)
        for vecino in grafo[vertice]:
            if not visitados[vecino]:
                dfs(vecino, componente)

    for vertice in vertices:
        if not visitados[vertice]:
            componente = []
            dfs(vertice, componente)
            componentes.append(componente)

    return componentes

def es_conexo(grafo_lista):
    '''
    Dado un grafo en representacion de lista, y utilizando la función "componentes_conexas"
    devuelve True/False si el grafo es o no conexo.
    '''
    componentes = componentes_conexas(grafo_lista)
    return len(componentes) == 1
