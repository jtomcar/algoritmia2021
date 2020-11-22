from typing import *
from math import sqrt
import sys

from algoritmia.datastructures.digraphs import UndirectedGraph
from algoritmia.datastructures.mergefindsets import MergeFindSet

Vertex = int
Edge = Tuple[Vertex, Vertex]


# Función que lee los datos y devuelve una tupla con cada línea del texto
def leer_datos():
    sys.stdin = open(sys.argv[1], "r", encoding="utf-8")
    lines = sys.stdin.readlines()
    datos = []
    for elem in lines:
        datos.append(tuple(elem[0:-1].split(" ")))
    return datos


def get_d_euclidea(x: Tuple[str, str], y: Tuple[str, str]) -> float:
    return sqrt((float(x[0]) - float(y[0])) ** 2 + (
            float(x[1]) - float(y[1])) ** 2)


def crear_grafo(datos: Tuple[str, ...]):
    edges: Edge = []  # lista de vértices
    pesos: float = []
    vertices: int = []
    n = datos[0][0]
    ''' Tenemos que crear un grafo totalmente contectado, para ello contectatemos cada punto con el resto con una arista
        Como la arista que contecta 1 y 2 (1,2) es la misma que (2,1), evitamos poner ambas, el grafo no es dirigido
        en prueba.py hay pequeño programa de prueba para ver que estos fors generan la lista justa'''
    n: int = int(n)  # tamaño del grafo n x n
    for i in range(n):
        for j in range(n - i - 1):
            edges.append((i, j + i + 1))
            pesos.append(get_d_euclidea(datos[i + 1], datos[j + i + 1 + 1]))
    for v in range(n):
        vertices.append(v)
    indices_ordenados = sorted(range(len(edges)), key=lambda i: pesos[i])

    return vertices, edges, pesos, indices_ordenados


def crear_output2(pasillos, num_v):
    output: List[int] = [0]
    # candidato se inicializa en una cantidad imposible mayor que todas para ir comparando y quedarse con el más pequeño
    candidato = num_v + 1
    for i in pasillos:
        if i[0] == 0:
            if i[1] < candidato:
                candidato = i[1]
        if i[1] == 0:
            if i[0] < candidato:
                candidato = i[0]
    output.append(candidato)
    # Ya están la primera arista en output (dos vertices) ahora iremos añadiendo los vértices que están conectados con el último que esté en output
    # como ya hemos añadido el 0 y su sucesor, solo tenemos que añadir la talla de los vértices - 2
    for e in range(num_v - 2):
        e = output[e + 1]  # e ahora es el valor del último vértice añadido
        for c in pasillos:
            if c[0] == e and c[1] not in output:
                output.append(c[1])
                break
            if c[1] == e and c[0] not in output:
                output.append(c[0])
                break
    return output

def crear_output(pasillos, num_v):
    output = [0]
    grafo = UndirectedGraph(E=pasillos)
    s0 = grafo.succs(0)
    output.append(min(s0))
    for i in range(num_v-2):
        s0=grafo.succs(output[len(output)-1])
        s0_0=s0.pop()
        if s0_0 != output[len(output)-2]:
            output.append(s0_0)
        else:
            s0_1=s0.pop()
            output.append(s0_1)
    return output


def kruskal(datos, vertices, edges, pesos, indices_ordenados):
    '''
    Ahora creamos una lista con los índices ordenados de la lista edges respecto a la distancia euclídea de los puntos
    que forman la arista
    '''
    num_v = int(datos[0][0])

    mfs: MergeFindSet[Vertex] = MergeFindSet()
    # Añadimos todos los vértices al mfs para poder hacer el recorrido sin ciclos

    for v in vertices:
        mfs.add(v)

    pasillos: List[Edge] = []

    # peso total de las aristas que forman parte del camino
    peso_total = 0

    # visitados controlará que para cada vértice, representado por el índice en la lista, no se visite más de dos veces
    visitados: List[int] = [0] * num_v

    for i in indices_ordenados:
        u: Vertex = edges[i][0]
        v: Vertex = edges[i][1]
        if mfs.find(u) != mfs.find(v):
            if visitados[u] < 2 and visitados[v] < 2:
                mfs.merge(u, v)
                pasillos.append((u, v))
                visitados[u] += 1
                visitados[v] += 1
                peso_total += pesos[i]
    vis_1_vez = -1
    i = 0
    # vamos a buscar los vértices que solo han sido visitados una vez, para poder crear el ciclo hamiltoniano
    for e in visitados:
        if e == 1:
            if vis_1_vez != -1:
                pasillos.append((vis_1_vez, i))
                peso_total += sqrt((float(datos[vis_1_vez + 1][0]) - float(datos[i + 1][0])) ** 2 + (
                        float(datos[vis_1_vez + 1][1]) - float(datos[i + 1][1])) ** 2)
            else:
                vis_1_vez = i
        i += 1
    # en corridors tenemos las aristas que forman parte del ciclo, pero necesitamos una secuencia de vértices para la salida
    # output empezará por el 0 y luego le añadirá el vértice contectado con el 0 que sea más pequeño
    output: List[int] = crear_output(pasillos, num_v)

    print("K")
    print(peso_total)
    print(output)


def prim(datos, edges, pesos, i_o):
    num_v = int(datos[0][0])
    pasillos: Edge = []
    visitados = []  # visitados[i][0] True visitado, False no // visitados[i][1] numero de aristas, 0,1 o 2
    for i in range(num_v):
        visitados.append([False, 0])
    visitados[0][0] = True
    peso_total = 0
    while len(pasillos) < num_v-1:
        # quitar un pasillo es que indices_ordenados[i]=-1
        for i in range(len(i_o)):
            if i_o[i] != -1:
                v1 = visitados[edges[i_o[i]][0]]
                v2 = visitados[edges[i_o[i]][1]]
                if v1[1] == 2 or v2[1] == 2:  # si los dos vértices están en dos arístas descartamos la arista
                    i_o[i] = -1
                elif v1[0] and v2[0]:  # caso en el que se han visitado los dos vértices, descartamos la arista

                    i_o[i] = -1
                elif v1[0] or v2[0]:  # caso en el que solo se ha visitado un vértice, añadimos arista a vertices
                    v1[0] = True
                    v2[0] = True
                    v1[1] += 1
                    v2[1] += 1
                    pasillos.append(edges[i_o[i]])
                    peso_total += pesos[i_o[i]]
                    break


    vis_1_vez = -1
    i = 0
    # vamos a buscar los vértices que solo han sido visitados una vez, para poder crear el ciclo hamiltoniano
    for e in visitados:
        if e[1] == 1:
            if vis_1_vez != -1:
                pasillos.append((vis_1_vez, i))
                peso_total += sqrt((float(datos[vis_1_vez + 1][0]) - float(datos[i + 1][0])) ** 2 + (
                        float(datos[vis_1_vez + 1][1]) - float(datos[i + 1][1])) ** 2)
            else:
                vis_1_vez = i
        i += 1
    print(pasillos)
    output = crear_output(pasillos, num_v)
    print("PRIM")
    print(peso_total)
    print(output)


if __name__ == '__main__':
    datos = leer_datos()
    vertices, edges, pesos, indices_ordenados = crear_grafo(datos)
    kruskal(datos, vertices, edges, pesos, indices_ordenados)
    prim(datos, edges, pesos, indices_ordenados)
    print("")
