import sys
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
    listaProhibidas = []
    for elem in fichEntrada[2:len(fichEntrada)]:
        u = (elem[0], elem[1])
        v = (elem[2], elem[3])
        arista = (u,v)
        listaProhibidas.append(arista)
    #***********************************************
    vertices: List[Vertex] = [(r,c) for r in range(num_filas) for c in range(num_cols)]

    mfs: MergeFindSet[Vertex] = MergeFindSet()
    for v in vertices:
        mfs.add(v)

    edges: List[Edge] = []
    # Creamos la arista de arriba e izquierda de cada vertice
    for r, c in vertices:  # r,c = (r,c) = v Desglolsas la tupla
        if r > 0:
            edges.append(((r, c), (r - 1, c)))
        if c > 0:
            edges.append(((r, c), (r, c - 1)))

    shuffle(edges)  # baraja las aristas

    corridors: List[Edge] = []  # pasillos de nuestro grafo
    for elem2 in edges:
        u2=elem2[0]
        v2=elem2[1]
        if (mfs.find(u2) != mfs.find(v2)):
            if ((u2, v2) not in listaProhibidas and (v2, u2) not in listaProhibidas):
                mfs.merge(u2, v2)
                corridors.append((u2, v2))

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
        if (len(resultado)>1): #Si no es conexo, salir
            es_conexo=False
            break
    return es_conexo

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
    lv = LabyrinthViewer(graph, canvas_width=900, canvas_height=900, margin=10)
    lv.run()

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
    es_valido=sol[4]
    es_conexo = componentes_conexos(graph)

    if(es_conexo and es_valido):
        muestraSolucion(sol)
        if len(argv) == 3 and argv[2] == "-g":
            visualizaLaberinto(graph)
    else:
        print("NO ES POSIBLE CONSTRUIR EL LABERINTO")



