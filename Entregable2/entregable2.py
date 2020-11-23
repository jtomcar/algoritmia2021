import math
import operator
import sys
from typing import *
from sys import *
from algoritmia.datastructures.digraphs import UndirectedGraph
from algoritmia.datastructures.mergefindsets import MergeFindSet
from time import time

from algoritmia.datastructures.prioritymaps import MinHeapMap

Vertex = Tuple[float, float]
Edge = Tuple[Vertex, Vertex]

#******************************************************************************************************
#    METODO PARA CREAR EL GRAFO
#******************************************************************************************************

def crearGrafo(fichEntrada) -> Tuple[
    UndirectedGraph, Dict[Tuple[int, int], float], MergeFindSet, List[Tuple[int, int]]]:
    vertices = fichEntrada[1:len(fichEntrada)]
    aristas = dict()
    mfs = MergeFindSet()

    for u in range(len(vertices)):
        mfs.add(u)
        for v in range(len(vertices)):
            if u != v:
                dist = distancia(vertices[u], vertices[v])
                aristas[(u, v)] = dist

    aristasOrdenadas = sorted(aristas.items(), key=operator.itemgetter(1))  # Ordenamos por distancia


    return UndirectedGraph(E=aristas.keys()), aristas, mfs, aristasOrdenadas

# Metodo calculo de distancias
def distancia(punto1, punto2):
    return math.sqrt((punto2[0] - punto1[0]) ** 2 + ((punto2[1] - punto1[1]) ** 2))


#******************************************************************************************************
#    ALGORITMO KRUSKAL, MODIFICADO
#******************************************************************************************************

def kruskalMod(grafo, aristas, mfs, aristasOrdenadas) -> Tuple[UndirectedGraph, int, Union[int, Any]]:

    edges = []
    # Vertices clave:vertice, valor:vecesVistos
    vertices = dict()
    vistos = set()
    for i in range(len(grafo.V)):
        vertices[i] = 0
        vistos.add(i)
    #Distancia final
    distanciaFinal = 0
    aristasOrdenadas = dict(aristasOrdenadas)

    for arista, distancia in aristasOrdenadas.items():
        u = arista[0]
        v = arista[1]
        if mfs.find(u) != mfs.find(v):
            if vertices[u] <=1 and vertices[v] <=1:
                vertices[u]+=1
                vertices[v]+=1
                if vertices[u]==2:
                    vistos.remove(u)
                if vertices[v]==2:
                    vistos.remove(v)
                mfs.merge(u, v)
                edges.append((u, v))
                distanciaFinal = distanciaFinal + distancia

    pos1=vistos.pop()
    pos2=vistos.pop()
    edges.append((pos1,pos2))
    distanciaFinal = distanciaFinal + aristas[(pos1,pos2)]

    return UndirectedGraph(E=edges), len(grafo.V), distanciaFinal

#******************************************************************************************************
#    ALGORITMO PRIM, MODIFICADO
#******************************************************************************************************

def primMod(grafo, aristas, aristasOrdenadas) -> Tuple[UndirectedGraph, int, Union[int, Any]]:

    #Comprobaciones
    listaVistos = [0] * len(grafo.V) #0 no vistas
    #Inicializamos con un solo vertice, el 0
    listaVistos[0]=1
    ultimo=set()
    pos=0
    empieza=True
    sigue=True
    #Salidas
    distanciaFinal=0
    edges=[]
    aristasOrdenadas=dict(aristasOrdenadas)


    while sigue:
        for elem in aristasOrdenadas.items():
            if elem[1] != 0:
                # Vamos a seguir el patron de cambiar la distancia a 0, a las aristas que ya no nos sirven,
                # de esta forma no las volvemos a seleccionar
                if listaVistos[elem[0][0]] != 0 and listaVistos[elem[0][1]] != 0:
                    aristasOrdenadas[elem[0]]=0
                else:
                    # Restriccion: Cada vertice solo puede aparecer como max en 2 aristasOrdenadas
                    # En caso contrario, distancia a 0
                    if listaVistos[elem[0][0]] > 1 or listaVistos[elem[0][1]] > 1:
                        aristasOrdenadas[elem[0]]=0
                    else:
                        # Si aparecen una o ninguna, a la salida -> edges
                        if listaVistos[elem[0][0]] != 0 or listaVistos[elem[0][1]] != 0:
                            pos+=1
                            if pos == len(grafo.V) - 1: sigue = False
                            distanciaFinal = distanciaFinal+elem[1]
                            listaVistos[elem[0][0]] += 1
                            listaVistos[elem[0][1]] += 1
                            # Para que 0 entre tres veces, ya que empezamos por el
                            if elem[0][0]==0 and empieza:
                                listaVistos[0]=1
                                empieza=False
                            edges.append(elem[0])
                            break



    #Buscamos los que solo han aparecido 1 vez
    for i in range(len(listaVistos)):
        if listaVistos[i]==1:
            ultimo.add(i)

    #y lo añadimos, sumamos tambien su distancia
    pos1=ultimo.pop()
    pos2=ultimo.pop()
    edges.append((pos1,pos2))
    distanciaFinal = distanciaFinal + aristas[(pos1,pos2)]

    return UndirectedGraph(E=edges), len(grafo.V), distanciaFinal

#******************************************************************************************************
#    METODOS ENTRADA Y SALIDA DEL PROGRAMA
#******************************************************************************************************

def leerFichero(fichEntrada):
    #fich = open(fichEntrada, "r", encoding="utf-8")
    lines = sys.stdin.readlines()
    lista = []
    i = 0
    for linea in lines:
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

    print(distanciaFinal)
    print(salida)
    return salida

#******************************************************************************************************
#    MAIN
#******************************************************************************************************

if __name__ == '__main__':

    # tiempo_inicial = time()

    fichEntrada = leerFichero(argv[1])
    solGrafo = crearGrafo(fichEntrada)
    # Kruskal
    solKruskal = kruskalMod(solGrafo[0], solGrafo[1], solGrafo[2], solGrafo[3])
    muestraSalida(solKruskal[0], solKruskal[1], solKruskal[2])
    # Prim
    solPrim = primMod(solGrafo[0], solGrafo[1], solGrafo[3])
    muestraSalida(solPrim[0], solPrim[1], solPrim[2])

    # tiempo_final = time()
    # tiempo_ejecucion = tiempo_final - tiempo_inicial
    #
    # print ("El tiempo de ejecucion fue:", tiempo_ejecucion, "segundos")  # En segundos