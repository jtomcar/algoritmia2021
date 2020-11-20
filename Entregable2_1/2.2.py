import math
import sys
from typing import *
from sys import *
from algoritmia.datastructures.digraphs import UndirectedGraph
from algoritmia.datastructures.mergefindsets import MergeFindSet
from random import shuffle, seed

from graph2dviewer import Graph2dViewer
from labyrinthviewer import LabyrinthViewer

Vertex = Tuple[float, float]
Edge = Tuple[Vertex, Vertex]

def crearGrafo(fichEntrada) -> UndirectedGraph:
    num_puntos = int(fichEntrada[0][0])
    vertices = fichEntrada[1:len(fichEntrada)]
    edges: List[Edge] = []
    aristas: List[Edge] = []
    mfs: MergeFindSet[Vertex] = MergeFindSet()

    dicPuntos = {} #Diccionario de posiciones vertices
    for i in range(len(vertices)):
        dicPuntos[i]=vertices[i]
        mfs.add(dicPuntos[i])

    for i in range(len(vertices)):
        for j in range(len(vertices)):
            if (i!=j and (i,j) not in aristas and (j,i) not in aristas ):
                edges.append((vertices[i],vertices[j]))
                #aristas.append((i,j))

    corridors: List[Edge] = []
    distanciaVertices=[]
    x=0;
    for elem in edges:
        distanciaVertices.append((distancia(elem[0],elem[1]),elem))
        x=x+1;

    distanciaVertices.sort()
    for elem in distanciaVertices:
        aristas.append(elem[1])


    print(aristas)
    conj=set()
    for u, v in aristas:
        print(conj)
        if (mfs.find(u)!=mfs.find(v)):
            if u not in conj and v not in conj:
                #conj.add(v)
                mfs.merge(u,v)
                corridors.append((u,v))

    print(distanciaVertices)
    print(aristas)

    #return UndirectedGraph(V=vertices, E=edges)
    return UndirectedGraph(E=corridors)

# HANGANU -------------------------------------------------------------------------------

# def kruskal(fichEntrada) -> UndirectedGraph:
#     num_puntos = int(fichEntrada[0][0])
#     print(num_puntos)
#     vertices = fichEntrada[1:len(fichEntrada)]
#     print((vertices))
#     conjuntoPuntos = set(fichEntrada[1:len(fichEntrada)])
#     print(conjuntoPuntos)
#     mfs: MergeFindSet[Vertex] = MergeFindSet()
#     vertices: List[Vertex] = []
#     edges: List[Edge] = []
#     distanciaTotal=0
#
#
# #Que ascooooooooooooooooooooooooooooooooooo
#
#     for punto1 in conjuntoPuntos:
#         puntoAux=punto1
#         for punto2 in conjuntoPuntos:
#             distanciaAuxiliar=999999999999
#             if punto1!=punto2:
#                 distancia1=distancia(punto1,punto2)
#                 if(distancia1<distanciaAuxiliar and ((punto1,punto2)) not in(edges) and ((punto2,punto1)) not in(edges)):
#                     distanciaAuxiliar=distancia1
#                     puntoAux=punto2
#         edges.append((punto1,puntoAux))
#
#     for elem in edges:
#         print(elem)
#
#
#     # for r in range(num_puntos):
#     #     for c in range(num_puntos):
#     #         vertices.append((r, c))
#     #         mfs.add((r, c))
#     #         print(r)
#     #         print(c)
#     #         # distancia=math.sqrt((r[0]-r[1])*(r[0]-r[1])+(c[0]-c[1])*(c[0]-c[1]))
#
#
#
#
def distancia(punto1,punto2):
    return math.sqrt((float(punto1[0]) - float(punto1[1])) **2 + ((float(punto2[0]) - float(punto2[1])) **2))
#
#
# #Kruskal del libro
# # class KruskalsMinimumSpanningForestFinder(IMinimumSpanningForestFinder):
# #     def init (self , createMergeFindSet: "Iterable<T> -> IMFSet<T>"
# #             =lambda V: MergeFindSet((v,) for v in V)):
# #         self.createMergeFindSet = createMergeFindSet
# # def minimum spanning forest(self , G: "undirected Digraph<T>",
# #         d: "T, T -> R") -> "Iterable<(T, T)> ":
# #     forest = self.createMergeFindSet(G.V)
# #     n = 0
# #     for ( , (u,v)) in sorted(((d(u,v), (u,v)) for (u,v) in G.E)):
# #         if forest.find(u) != forest.find(v):
# #             forest.merge(u, v)
# #             yield (u, v)
# #             n += 1
# #             if n == len(G.V)-1: break





#********* Metodos para entrada y salida del programa *********************************************
def leerFichero(fichEntrada):
    fich = open(fichEntrada, "r", encoding="utf-8")
    lista = []
    i=0
    for linea in fich:
        i += 1
        elem=linea.rstrip("\n").split(" ")
        elem=tuple(elem)
        if (i>1): #Formato arista
            u = (float(elem[0]), float(elem[1]))
            lista.append(u)
        else:
            lista.append(elem)
    return lista  # Devolvemos lista de tuplas, cada elemento una linea del fichero


if __name__ == '__main__':

    fichEntrada = leerFichero(argv[1])
    # print(int(fichEntrada[0][0]))
    # for elem in fichEntrada[1:int(fichEntrada[0][0])+1]:
    #     print(elem)
    # for i in range(len(fichEntrada)):
    #     print(i)

    grafo = crearGrafo(fichEntrada)
    viewer = Graph2dViewer(grafo, window_size=(800, 800))
    viewer.run()