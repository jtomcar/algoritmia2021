import math
import operator
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


def crearGrafo(fichEntrada) -> Tuple[UndirectedGraph, Dict[Tuple[int, int], float], MergeFindSet]:
    vertices = fichEntrada[1:len(fichEntrada)]
    aristas = dict()
    mfs = MergeFindSet()

    for u in range(len(vertices)):
        mfs.add(u)
        for v in range(len(vertices)):
            if u != v:
                dist = distancia(vertices[u], vertices[v])
                aristas[(u, v)] = dist

    return UndirectedGraph(E=aristas.keys()), aristas, mfs


def kruskalMod(grafo, aristas, mfs) -> Tuple[UndirectedGraph, int, Union[int, Any]]:
    # Aristas
    aristasOriginal = aristas
    aristas = sorted(aristas.items(), key=operator.itemgetter(1))  # Ordenamos por valor
    edges = []
    # Vertices clave:vertice, valor:vecesVistos
    vertices = dict()
    vistos = []
    for i in range(len(grafo.V)):
        vertices[i] = 0
        vistos.append(i)
    #Distancia final
    distanciaFinal = 0

    for arista, distancia in aristas:
        u = arista[0]
        v = arista[1]
        if mfs.find(u) != mfs.find(v) and vertices[u] <=1 and vertices[v] <=1:
            vertices[u]+=1
            vertices[v]+=1
            if vertices[u]==2:
                vistos.remove(u)
            if vertices[v]==2:
                vistos.remove(v)
            mfs.merge(u, v)
            edges.append((u, v))
            distanciaFinal = distanciaFinal + distancia

    print(edges)
    edges.append((vistos[0], vistos[1]))
    distanciaFinal = distanciaFinal + aristasOriginal[(vistos[0], vistos[1])]

    return UndirectedGraph(E=edges), len(grafo.V), distanciaFinal

def primMod(grafo, aristas, mfs) -> Tuple[UndirectedGraph, int, Union[int, Any]]:

    grafo.succs(0)
    print(grafo.succs(0))
    pos=0
    listaDistancias=[]
    sol=[]
    conjuntoBolsa=set()

    for elem in aristas.items():
        if elem[0][1] in range(len(grafo.V)) and elem[0][0]==pos:
            listaDistancias.append((elem[1],elem[0]))
    minimo=min(listaDistancias)
    minimoReves = (minimo[0], (minimo[1][1], minimo[1][0]))
    if minimoReves in listaDistancias: listaDistancias.remove(minimoReves)
    sol.append(minimo)
    listaDistancias.remove(minimo)

    pos+=1
    for elem in aristas.items():
        if elem[0][1] in range(len(grafo.V)) and elem[0][0]==pos:
            listaDistancias.append((elem[1],elem[0]))
    minimo=min(listaDistancias)
    minimoReves = (minimo[0], (minimo[1][1], minimo[1][0]))
    if minimoReves in listaDistancias: listaDistancias.remove(minimoReves)
    sol.append(minimo)
    listaDistancias.remove(minimo)

    pos+=1
    for elem in aristas.items():
        if elem[0][1] in range(len(grafo.V)) and elem[0][0]==pos:
            listaDistancias.append((elem[1],elem[0]))
    minimo=min(listaDistancias)
    minimoReves = (minimo[0], (minimo[1][1], minimo[1][0]))
    if minimoReves in listaDistancias: listaDistancias.remove(minimoReves)
    sol.append(minimo)
    listaDistancias.remove(minimo)

    pos+=1
    for elem in aristas.items():
        if elem[0][1] in range(len(grafo.V)) and elem[0][0]==pos:
            listaDistancias.append((elem[1],elem[0]))
    minimo=min(listaDistancias)
    minimoReves = (minimo[0], (minimo[1][1], minimo[1][0]))
    if minimoReves in listaDistancias: listaDistancias.remove(minimoReves)
    sol.append(minimo)
    listaDistancias.remove(minimo)

    pos+=1
    for elem in aristas.items():
        if elem[0][1] in range(len(grafo.V)) and elem[0][0]==pos:
            listaDistancias.append((elem[1],elem[0]))
    minimo=min(listaDistancias)
    minimoReves = (minimo[0], (minimo[1][1], minimo[1][0]))
    if minimoReves in listaDistancias:
        print("Hola")
        listaDistancias.remove(minimoReves)
    sol.append(minimo)
    listaDistancias.remove(minimo)

    print("Min", min(listaDistancias))
    print("Conjunto", conjuntoBolsa)
    print("lista", listaDistancias)
    print("sol", sol)


# Metodo calculo de distancias
def distancia(punto1, punto2):
    return math.sqrt((punto2[0] - punto1[0]) ** 2 + ((punto2[1] - punto1[1]) ** 2))


# ********* Metodos para entrada y salida del programa *********************************************
def leerFichero(fichEntrada):
    fich = open(fichEntrada, "r", encoding="utf-8")
    lista = []
    i = 0
    for linea in fich:
        i += 1
        elem = linea.rstrip("\n").split(" ")
        elem = tuple(elem)
        if (i > 1):  # Formato arista
            u = (float(elem[0]), float(elem[1]))
            lista.append(u)
        else:
            lista.append(elem)
    return lista  # Devolvemos lista de tuplas, cada elemento una linea del fichero


def muestraSalida(grafoSol, nVertices, distanciaFinal):

    salida = []
    salida.append(0)
    mete=min(grafoSol.succs(0)) #3
    salida.append(mete)
    i=0
    while i <= nVertices-3:
        aux=salida[len(salida)-2] #Penultimo metido
        for elem in grafoSol.succs(mete):
            if elem != aux:
                salida.append(elem)
                mete=elem
        i+=1

    # salida = []
    # print(grafoSol)
    # salida.append(0)
    # mete=min(grafoSol.succs(0)) #3
    # salida.append(mete)
    # i=0
    # while i <= nVertices-3:
    #     aux=salida[len(salida)-2] #Penultimo metido
    #     sucesores=tuple(grafoSol.succs(mete))
    #     if sucesores[0]!=aux:
    #         salida.append(sucesores[0])
    #         mete = sucesores[0]
    #     else:
    #         salida.append(sucesores[1])
    #         mete = sucesores[1]
    #     i+=1

    print(distanciaFinal)
    print(salida)
    return salida
if __name__ == '__main__':
    fichEntrada = leerFichero(argv[1])
    solGrafo = crearGrafo(fichEntrada)
    # Kruskal
    solKruskal = kruskalMod(solGrafo[0], solGrafo[1], solGrafo[2])
    solucionAlg1 = muestraSalida(solKruskal[0], solKruskal[1], solKruskal[2])
    # Prim
    solPrim = primMod(solGrafo[0], solGrafo[1], solGrafo[2])
