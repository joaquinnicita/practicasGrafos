#! /usr/bin/python

# 1ra Practica Laboratorio 
# Teoria de Grafos
# Consigna: Implementar los siguientes metodos

import sys

def lee_grafo_stdin(grafo):
    """
    Recibe como argumento un grafo representado como una lista de tipo:
    Ejemplo Entrada: 
       ['3', 'A', 'B', 'C', 'A B', 'B C', 'C B']
    
    donde el 1er elemento se corresponde a la cantidad de vertices,
    y por ultimo las aristas existentes.

    Ejemplo retorno: 
        (['A','B','C'],[('A','B'),('B','C'),('C','B')])"""
    
    num_vertices = int(grafo[0]) # El primer valor de la lista es la cantidad de vertices del grafo
    vertices = grafo[1:num_vertices+1] # Toma una lista de vertices desde el indice 1 inclusive hasta el indice numvertices+1
    aristas = [tuple(arista.split()) for arista in grafo[num_vertices+1:]] # Hace una tupla de aristas para cada par de vertices que estan en la lista original
    return (vertices, aristas)

def lee_grafo_archivo(file_path):
    '''
    Lee un grafo desde un archivo y devuelve su representacion como lista.
    Ejemplo Entrada: 
        3
        A
        B
        C
        A B
        B C
        C B
    Ejemplo retorno: 
        (['A','B','C'],[('A','B'),('B','C'),('C','B')])
    '''
    with open(file_path, 'r') as file: # hace lo mismo que leer grafo stdin
        grafo = [line.strip() for line in file] #lee el archivo
    num_vertices = int(grafo[0])
    vertices = grafo[1:num_vertices+1]
    aristas = [tuple(arista.split()) for arista in grafo[num_vertices+1:]]
    return (vertices, aristas)

def imprime_grafo_lista(grafo):
    '''
    Muestra por pantalla un grafo. El argumento esta en formato de lista.
    '''
    vertices, aristas = grafo # divide el grafo en vertices y aristas
    print("Vertices:") #Imprime vertices
    for vertice in vertices:
        print(vertice)
    print("Aristas:") #Imprime aristas
    for arista in aristas:
        print(" ".join(arista)) #Concatena los dos vertices de la arista 

#################### FIN EJERCICIO PRACTICA ####################
def lee_entrada_1():
    '''
    Lee un grafo desde entrada estandar y devuelve su representacion como lista.
    Ejemplo Entrada: 
        3
        A
        B
        C
        A B
        B C
        C B
    Ejemplo retorno: 
        ['3', 'A', 'B', 'C', 'A B', 'B C', 'C B']
    '''
    data_input = []
    
    for line in sys.stdin:
        if line == '\n':
            break
        else:
            # Con strip() eliminamos los '\n' del final de c/line
            data_input.append(line.strip())
            
    return data_input # Dado el input, le saca los saltos de linea y mete las lineas en una lista

    
def lee_entrada_2():
    count = 0
    try:
        while True:
            line = input()
            count = count + 1
            print ('Linea: [{0}]').format(line)
    except EOFError:
        pass
    
    print ('leidas {0} lineas').format(count)
