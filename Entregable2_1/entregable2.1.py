from algoritmia.datastructures.digraphs import UndirectedGraph
from algoritmia.datastructures.mergefindsets import MergeFindSet
from typing import *
import sys
import math

Vertex = TypeVar('Vertex')


def load_file():
    nr_puntos = 0
    puntos = []

    try:
        nr_puntos = sys.stdin.readline()

        for line in sys.stdin.readlines():
            x1, y1 = line.split(" ")
            punto = (float(x1), float(y1))
            puntos.append(punto)
    except IOError:
        print("File cannot be open!")
    return nr_puntos, puntos


def load_file2():
    nr_puntos = 0
    puntos = []

    try:
        f = open(sys.argv[1])
        nr_puntos = f.readline()

        for line in f.readlines():
            x1, y1 = line.split(" ")
            punto = (float(x1), float(y1))
            puntos.append(punto)
    except IOError:
        print("File cannot be open!")
    return int(nr_puntos), puntos


def create_graph(puntos):
    aristas = dict()

    for v in range(len(puntos)):
        for w in range(len(puntos)):
            if v != w:
                weight = euclidean_distance(puntos[v], puntos[w])
                aristas[(v, w)] = weight
                # aristas[(w, v)] = weight

    return aristas

#Todo: se puede mejorar quitando los argumentos del principio
def euclidean_distance(x, y):
    x1 = x[0]
    y1 = x[1]
    x2 = y[0]
    y2 = y[1]

    return math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))


"""algoritmo kruskal
Ordenar todas las aristas en orden creciente de su peso.
elegir una arista, mirar si tiene ciclo con el spanning tree formado hasta el momento. Si no tiene ciclo, 
hacer un merge y sacar los vertices, si tiene, descartar la arista y pasar a la siguiente
repetir hasta V-1 aristas en el spt"""

"""
REQUISITO:
el segundo elemento de la lista que representa el camino será el vértice de menor índice entre los sucesores 
del vértice 0
"""


# TODO: finish implementation or getting the second vertex of path index 2
# def min_vertex(g: UndirectedGraph, v):
#     lista_vertices_vecinos = min(sorted(g.succs(v)))
#     print(min(sorted(g.succs(v))))
#     return lista_vertices_vecinos


def kruskal(aristas, g):
    path = []
    aristas_ordenadas = sorted(aristas.items(), key=lambda x: x[1])
    print(aristas_ordenadas)
    mfs = MergeFindSet()
    distance = 0

    for v in g.V:
        mfs.add(v)
    orden(aristas_ordenadas)

    for edge, w in aristas_ordenadas:
        u = edge[0]
        v = edge[1]
        if mfs.find(u) != mfs.find(v):
            if len(path) == 0:

                path.append(u)  # vertice a mirar

                # mirar los succesores del vertice cero, o el primer vertice del grafo, no el segundo vertice

                vertice_a_elegir = min(sorted(g.succs(u)))
                # print(vertice_a_elegir)
                if vertice_a_elegir < v:
                    path.append(vertice_a_elegir)
                mfs.merge(u, vertice_a_elegir)
                distance += aristas[u, vertice_a_elegir]

                # print(u, v, "not a cicle")
            # ----
            else:
                mfs.merge(u, v)
                if u not in path:
                    path.append(u)
                    distance += w
                if v not in path:
                    path.append(v)
                    distance += w
                # print(u, v, "not a cicle")

        # else:
        # print("yes a cycle")
    print(distance)
    # print(aristas_ordenadas)
    return path


def orden(aristas_ordenadas):
    for e, w in aristas_ordenadas:
        print(e, w)


def check_distance(aristas, path):
    path = [0, 1, 4, 3, 2]
    total = 0
    for i in range(len(path) - 1):
        total += aristas[path[i], path[i + 1]]
        print("De {} a {} = {}. Acumulado = {}".format(path[i], path[i + 1], (aristas[path[i], path[i + 1]]), total))
    print("Distancia total del camino = {}".format(total))


if __name__ == '__main__':
    nr_puntos, puntos = load_file2()
    aristas = create_graph(puntos)

    g = UndirectedGraph(E=aristas.keys())
    # print(g.V)
    # print(g.E)
    kruskal_path = kruskal(aristas, g)
    print(kruskal_path)
    check_distance(aristas, kruskal_path)
