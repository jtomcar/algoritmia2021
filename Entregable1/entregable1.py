from typing import *
from sys import *
from algoritmia.datastructures.digraphs import UndirectedGraph
from algoritmia.datastructures.mergefindsets import MergeFindSet
from random import shuffle, seed
from labyrinthviewer import LabyrinthViewer

Vertex = Tuple[int, int]
Edge = Tuple[Vertex, Vertex]


def laberintoMensaje(fichEntrada) -> UndirectedGraph:

    num_filas=fichEntrada[0][0]
    num_cols=fichEntrada[0][1]
    num_paredesProhib = fichEntrada[1][0]  #No se para que utilizarlo
    listaProhibidas = fichEntrada[2:len(fichEntrada)]

    vertices: List[Vertex] = [(r,c) for r in range(num_filas) for c in range(num_cols)]

    mfs: MergeFindSet[Vertex] = MergeFindSet()
    for v in vertices:
        mfs.add(v)

    edges: List[Edge] = []
    # Creamos la arista de arriba e izquierda de cada vertice
    for r, c in vertices:  # r,c = (r,c) = v Desglosas la tupla
        if r > 0:
            edges.append(((r, c), (r - 1, c)))
        if c > 0:
            edges.append(((r, c), (r, c - 1)))
    shuffle(edges)  # baraja las aristas
    # Paso 4
    corridors: List[Edge] = []  # pasillos de nuestro grafo
    #***********************************************
    for elem in listaProhibidas:
        u = (elem[0],elem[1])
        v = (elem[2],elem[3])
        # mfs.merge(u, v) #Etiqueto a "u" y a "v"
        # corridors.append((u, v))
        for u2, v2 in edges:
            if (mfs.find(u2) != mfs.find(v2)):
                mfs.merge(u2, v2)
                corridors.append((u2, v2))
    #************************************************
    # Paso 5

    # Paso 6
    return UndirectedGraph(E=corridors), (num_filas,num_cols), len(corridors), corridors

#********* Metodos para entrada y salida del programa *********************************************

def leerFichero(fichEntrada):
    fich = open(fichEntrada, "r", encoding="utf-8")
    lista = []
    for linea in fich:
        elem = [int(x) for x in linea.rstrip("\n").split(" ")]
        elem = tuple(elem)  # Convertimos lista a tupla
        lista.append(elem)
    return lista  # Devolvemos lista de tuplas, cada elemento una linea del fichero

def visualizaLaberinto(graph):
    lv = LabyrinthViewer(graph, canvas_width=800, canvas_height=600, margin=10)
    lv.run()

def muestraSolucion(sol):
    print(sol[1][0],sol[1][1])
    print(sol[2])
    for elem1, elem2 in sol[3]:
        print(elem1[0], elem1[1], elem2[0], elem2[1])

if __name__ == '__main__':
    seed(42)  # Esto es para que siempre salga el mismo grafico, lo ejecutes donde lo ejecutes

    fichEntrada = leerFichero(argv[1])
    sol = laberintoMensaje(fichEntrada)

    graph = sol[0]
    #muestraSolucion(sol)

    if len(argv) == 3 and argv[2] == "-g":
        visualizaLaberinto(graph)
