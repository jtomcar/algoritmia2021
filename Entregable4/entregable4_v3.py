import sys
from time import time
from typing import *

from algoritmia.problems.orderstatistics.minmax import MinMaxFinder
from algoritmia.schemes.divideandconquer import *

class Funambulista(IDivideAndConquerProblem):
    def __init__(self, a: List[int]):
        self.a = a

    def is_simple(self) -> "bool":
        return len(self.a) <= 2

    def trivial_solution(self):
        return self.a

    def divide(self) -> Iterable["Funambulista"]:
        yield Funambulista(self.a[:len(self.a) // 2])
        yield Funambulista(self.a[len(self.a) // 2:])

    def combine(self, s: Iterable[List[int]]) -> List[int]:
        a, b = tuple(s)
        c = [None] * (len(a) + len(b))
        i, j, k = 0, 0, 0
        while i < len(a) and j < len(b):
            if a[i] > b[j]:
                c[k] = a[i]
                i += 1
            else:
                c[k] = b[j]
                j += 1
            k += 1
        while i < len(a):
            c[k] = a[i]
            i += 1
            k += 1
        while j < len(b):
            c[k] = b[j]
            j += 1
            k += 1
        sol = MinMaxFinder.min_max(self, edificios)
        return sol


# ******************************************************************************************************
#    METODO DE ENTRADA
# ******************************************************************************************************

def leerFichero():
    lineas = sys.stdin.readlines()
    return lineas


# ******************************************************************************************************
#    MAIN
# ******************************************************************************************************

if __name__ == '__main__':

    tiempo_inicial = time()

    entrada=[int(i) for i in leerFichero()]
    num_edificios = entrada[0]
    edificios = entrada[1:]
    # fun_problem = Funambulista(edificios)
    # sol = DivideAndConquerSolver().solve(fun_problem)

    edif1=0
    edif2=0
    valle=0
    altura=0
    posValle=0
    posEdif1=0
    posEdif2=0
    k=0
    i=0
    minimo=max(edificios)
    lista=list()
    sigue=True
    while sigue:
        while sigue:
            edif1=edificios[k]
            if edificios[i] > edif1 and valle==0:
                k=i
            if edificios[i]<edif1 and edificios[i]<minimo:
                valle=edificios[i]
                minimo=edificios[i]
                posValle=i
            if edificios[i]>=edif1 and valle!=0:
                edif2=edificios[i]
                posEdif2=i
                posEdif1=k
                altura=edif1-valle
                break
            if i==len(edificios)-1:
                sigue=False
            i=i+1

        if sigue==False:
            break

        lista.append((posEdif1,posEdif2,posValle,altura))
        k=posEdif2
        i=posEdif2
        edif2 = 0
        valle = 0
        minimo=max(edificios)


    edificios2=list()
    for i in reversed(edificios):
        edificios2.append(i)
    edificios=edificios2[:]


    edif1 = 0
    edif2 = 0
    valle = 0
    altura = 0
    posValle = 0
    posEdif1 = 0
    posEdif2 = 0
    k = 0
    i = 0
    minimo = max(edificios)
    sigue = True
    while sigue:
        while sigue:
            edif1 = edificios[k]
            if edificios[i] > edif1 and valle==0:
                k=i
            if edificios[i] < edif1 and edificios[i] < minimo:
                valle = edificios[i]
                minimo = edificios[i]
                posValle = i
            if edificios[i] >= edif1 and valle != 0:
                edif2 = edificios[i]
                posEdif2 = i
                posEdif1 = k
                altura = edif1 - valle
                break
            if i == len(edificios) - 1:
                sigue = False
            i = i + 1

        if sigue == False:
            break

        lista.append(((len(edificios)-1)-posEdif2, (len(edificios)-1)-posEdif1, (len(edificios)-1)-posValle, altura))
        k = posEdif2
        i = posEdif2
        edif2 = 0
        valle = 0
        minimo = max(edificios)

    maximo=0
    solu=()
    for elem in lista:
        if elem[3]>maximo:
            maximo=elem[3]
            solu=elem

    print(solu)

    #*******************************************************************************************

    tiempo_final = time()
    tiempo_ejecucion = tiempo_final - tiempo_inicial
    print("")
    print("El tiempo de ejecucion fue:", tiempo_ejecucion, "segundos")  # En segundos