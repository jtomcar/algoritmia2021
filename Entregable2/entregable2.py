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

def crearGrafo(fichEntrada) -> Tuple[UndirectedGraph, Dict[Tuple[int, int], float]]:
    vertices = fichEntrada[1:len(fichEntrada)]
    aristas = dict()

    for u in range(len(vertices)):
        for v in range(len(vertices)):
            if u != v:
                dist = distancia(vertices[u], vertices[v])
                aristas[(u, v)] = dist

    return UndirectedGraph(E=aristas.keys()), aristas


def kruskalMod(grafo,aristas) -> Tuple[List[Edge], int, float]:
    dicAristas=aristas
    aristas= sorted(aristas.items(), key=lambda x: x[1]) #Ordenamos las aristas
    vertices = grafo.V
    mfs = MergeFindSet()
    edges=[]
    distanciaFinal=0
    for vertice in vertices:
        mfs.add(vertice)

    vistos: List[int] = [0] * len(vertices)
    for arista, distancia in aristas:
        u = arista[0]
        v = arista[1]
        if mfs.find(u) != mfs.find(v):
            mfs.merge(u, v)
            edges.append((u, v))
            vistos[u] += 1
            vistos[v] += 1
            distanciaFinal = distanciaFinal+distancia

    #Buscamos los que solo se han visto una vez, y añadimos la ultima arista
    cont=0
    elem1=-1
    elem2=-1
    for elem in vistos:
        if elem==1:
            if elem1 != -1: elem2 = cont
            else: elem1=cont
        cont=cont+1

    edges.append((elem1,elem2))
    distanciaFinal = distanciaFinal + dicAristas[(elem1,elem2)]
    #-----------------------------------------------------------------------
    pos=0
    sol=[]
    for edge in edges:
        if edge in dicAristas.keys():
          sol.append(pos)
        pos=pos+1

    return edges,len(vertices),distanciaFinal

#Metodo calculo de distancias
def distancia(punto1,punto2):
    return math.sqrt((punto2[0] - punto1[0]) **2 + ((punto2[1] - punto1[1]) **2))

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

def muestraSalida(edges, num_v, distanciaFinal):
    # output = [0]
    # grafo = UndirectedGraph(E=edges)
    # s0 = grafo.succs(0)
    # output.append(min(s0))
    # for i in range(num_v - 2):
    #     s0 = grafo.succs(output[len(output) - 1])
    #     s0_0 = s0.pop()
    #     if s0_0 != output[len(output) - 2]:
    #         output.append(s0_0)
    #     else:
    #         if len(s0)==0:
    #             break
    #         s0_1 = s0.pop()
    #         output.append(s0_1)
    # print(distanciaFinal)
    # print(output)
    # return output

    print(edges)
    salida=[]
    salida.append(0)
    i=0
    #Primera arista
    for arista in edges:
        if arista[0] == 0 and i != 0:
            salida.append(arista[1])
        i=i+1
    print(num_v)
    # Ya están la primera arista en output (dos vertices) ahora iremos añadiendo los vértices que están conectados con el último que esté en output
    # como ya hemos añadido el 0 y su sucesor, solo tenemos que añadir la talla de los vértices - 2
    print(salida)
    for e in range(num_v - 2):
        e = salida[e + 1]  # e ahora es el valor del último vértice añadido
        for c in edges:
            if c[0] == e and c[1] not in salida:
                salida.append(c[1])
                break
            if c[1] == e and c[0] not in salida:
                salida.append(c[0])
                break

    print(distanciaFinal)
    print(salida)
    return salida

if __name__ == '__main__':

    fichEntrada = leerFichero(argv[1])
    #Kruskal
    solGrafo = crearGrafo(fichEntrada)
    solKruskal = kruskalMod(solGrafo[0],solGrafo[1])
    solucionAlg1=muestraSalida(solKruskal[0],solKruskal[1],solKruskal[2])