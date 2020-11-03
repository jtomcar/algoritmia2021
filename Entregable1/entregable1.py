import sys
from typing import *
from sys import *
from algoritmia.datastructures.digraphs import UndirectedGraph
from algoritmia.datastructures.mergefindsets import MergeFindSet
from random import shuffle, seed
# from labyrinthviewer import LabyrinthViewer

Vertex = Tuple[int, int]
Edge = Tuple[Vertex, Vertex]

def laberintoMensaje(fichEntrada) -> UndirectedGraph:

    num_filas=int(fichEntrada[0][0])
    num_cols=int(fichEntrada[0][1])
    conjuntoProhibidas = set(fichEntrada[2:len(fichEntrada)]) #Conjunto es más rapido ls busq O(1)

    mfs: MergeFindSet[Vertex] = MergeFindSet()
    vertices: List[Vertex] = []
    edges: List[Edge] = []
    corridors: List[Edge] = []  # pasillos de nuestro grafo

    #Hacemos msf, y la lista de aristas en el mismo bucle anidado, para quitarnos bucles y ganar rapidez
    for r in range(num_filas):
        for c in range(num_cols):
            vertices.append((r,c))
            mfs.add((r,c))
            # Creamos la arista de arriba e izquierda de cada vertice
            if r > 0:
                edges.append(((r, c), (r - 1, c)))
            if c > 0:
                edges.append(((r, c), (r, c - 1)))

    shuffle(edges)  # baraja las aristas

    for elem in edges:
        u=elem[0]
        v=elem[1]
        if (mfs.find(u) != mfs.find(v)):
            if ((u, v) not in conjuntoProhibidas and (v,u) not in conjuntoProhibidas): # Comprabamos que no es una pared prohibida
                mfs.merge(u, v)
                corridors.append((u, v))

    # Comprabación de que entra en todas las habitaciones
    valido=True
    if ((len(vertices)-len(corridors))!=1):
        valido=False

    return UndirectedGraph(E=corridors), (num_filas,num_cols), len(corridors), corridors, valido

#**************Comprobación si es conexo o no + cliclos*******************************************
def recorredor_vertices_profundidad(grafo: UndirectedGraph, v_inicial: Vertex) -> List[Edge]:
    def recorrido_desde(v):
        seen.add(v)
        vertices.append(v)
        for suc in grafo.succs(v):
            if suc not in seen:
                recorrido_desde(suc)
    vertices = []
    seen = set()
    recorrido_desde(v_inicial)
    return vertices

def componentes_conexos(g: UndirectedGraph) -> "List[List[Vertex]]":
    vertices_no_visitados = set(g.V)
    resultado = []
    es_conexo=True
    while len(vertices_no_visitados) > 0:
        u = vertices_no_visitados.pop()
        vertices_visitados = recorredor_vertices_profundidad(g, u)
        vertices_no_visitados -= set(vertices_visitados)
        resultado.append(vertices_visitados)
        if (len(resultado)>1): #Si ya tiene más de un grafo, salimos.
            es_conexo=False
            break
    return es_conexo

#********* Metodos para entrada y salida del programa *********************************************
def leerFichero(fichEntrada):
    fich = open(fichEntrada, "r", encoding="utf-8")
    lista = []
    i=0
    for linea in fich:
        i+=1
        elem=linea.rstrip("\n").split(" ")
        elem=tuple(elem)
        if (i>=3): #Formato arista
            u = (int(elem[0]), int(elem[1]))
            v = (int(elem[2]), int(elem[3]))
            lista.append((u,v))
        else:
            lista.append(elem)
    return lista  # Devolvemos lista de tuplas, cada elemento una linea del fichero

# def visualizaLaberinto(graph):
#     lv = LabyrinthViewer(graph, canvas_width=1500, canvas_height=1500, margin=10)
#     lv.run()

def muestraSolucion(sol):
    print(sol[1][0],sol[1][1])
    print(sol[2])
    for elem1, elem2 in sol[3]:
        print(elem1[0], elem1[1], elem2[0], elem2[1])

#********* main ***************************************************************************************

if __name__ == '__main__':
    seed(42)  # Esto es para que siempre salga el mismo grafico, lo ejecutes donde lo ejecutes

    sys.setrecursionlimit(10000) #Para que no limita la pila por las limitaciones de python

    fichEntrada = leerFichero(argv[1])
    sol = laberintoMensaje(fichEntrada)

    graph = sol[0]
    entra_en_todas=sol[4]
    es_conexo = componentes_conexos(graph)

    if(es_conexo and entra_en_todas):
        muestraSolucion(sol)
        # if len(argv) == 3 and argv[2] == "-g":
        #     visualizaLaberinto(graph)
    else:
        print("NO ES POSIBLE CONSTRUIR EL LABERINTO")



