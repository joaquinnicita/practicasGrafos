from src.practica1 import *
from src.practica2 import *
from src.practica3 import *

def main():
    grafo = lee_entrada_1()
    grafo_lista = lee_grafo_archivo("/home/joaquin/Documents/Escuela/Grafos/grafo.txt")
    print("Grafo: ")
    print(grafo_lista)
    print(imprime_grafo_lista(grafo_lista))
    print(f"Grado de cada vertice: \n{cuenta_grado(grafo_lista)}")
    print(f"Vertices aislados:  {vertice_aislado(grafo_lista)}")
    print(f"Componentes conexas: {componentes_conexas(grafo_lista)}")
    print(f"Es conexo: {es_conexo(grafo_lista)}")
    print(f"Esta el nodo 'D' en el grafo: {valida_nodo_en_grafo(grafo_lista, 'D')}")
    print(f"Camino desde A hasta C: {encuentra_camino(grafo_lista,'A', 'C')}")
    print(f"Encuentra Camino Cerrado: {encuentra_camino_cerrado(grafo_lista, 'A')}")
    print(f"Recorrido desde A hasta C: {encuentra_recorrido(grafo_lista, 'A', 'C')}")
    print(f"Encuentra Circuito: {encuentra_circuito(grafo_lista, 'A')}")
    print(f"Encuentra Camino simple desde A hasta C: {encuentra_camino_simple(grafo_lista, 'A', 'C')}")
    print(f"Encuentra Ciclo de A: {encuentra_ciclo(grafo_lista, 'A')}")

    camino_lista = ['A','B','C','B','A','B','C']
    print(f"Determina camino: {determina_caminos(camino_lista)}")





          
          


    
if __name__ == '__main__':
    main()
