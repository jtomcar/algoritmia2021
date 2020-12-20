import sys
from time import time
from typing import *

from algoritmia.schemes.divideandconquer import *

class Funambulista(IDivideAndConquerProblem):
    def __init__(self, edificios: List[int], sol: List[int], e, b):
        self.edificios = edificios
        self.b = b
        self.e = e
        self.sol = sol
        self.posMax = self.edificios.index(max(self.edificios))

    def is_simple(self) -> "bool":
        return len(self.edificios) <= 1

    def trivial_solution(self):
        return self.edificios

    def divide(self) -> Iterable["Funambulista"]:
        yield Funambulista(self.edificios[:self.posMax], self.sol, self.e, self.posMax)
        yield Funambulista(self.edificios[self.posMax:], self.sol, self.e, self.posMax)

    def combine(self, s: Iterable[List[int]]) -> List[int]:
        if self.posMax != 0:
            a, b = tuple(s)
            valle = altura = posEdif1 = posEdif2 = 0
            minimo = max(self.e)
            posValle = a, b
            a = b = self.b
            while True:
                edif1 = self.e[b]
                if self.e[a] > edif1 and valle == 0:
                    b = a
                if self.e[a] < edif1 and self.e[a] < minimo:
                    valle = self.e[a]
                    minimo = self.e[a]
                    posValle = a
                if self.e[a] >= edif1 and valle != 0:
                    posEdif2 = a
                    posEdif1 = b
                    altura = edif1 - valle
                    break
                if a == len(self.e) - 1:
                    break
                a = a + 1
            self.sol.append((posEdif1, posEdif2, posValle, altura))
            maximo = 0
            solucion = list()
            for elem in self.sol:
                if elem[3] > maximo:
                    maximo = elem[3]
                    solucion = elem
            return solucion
        self.edificios = list()
        return self.sol


# ******************************************************************************************************
#    METODO DE ENTRADA Y SALIDA
# ******************************************************************************************************

def leerFichero():
    lineas = sys.stdin.readlines()
    return lineas


def salida(a, b):
    tam = len(edificios) - 1
    if (not a and not b) or (len(a) and len(b)) == 1:
        print("NO HAY SOLUCIÓN")
    else:
        if not b:
            print(str(a[0])+" "+str(a[1])+" "+str(a[2])+" "+str(a[3]))
            print("")
        elif not a:
            print(str(tam - b[1])+" "+str(tam - b[0])+" "+str(tam - b[2])+" "+str(b[3]))
            print("")
        else:
            if a[3] > b[3]:
                print(str(a[0])+" "+str(a[1])+" "+str(a[2])+" "+str(a[3]))
                print("")
            else:
                print(str(tam - b[1])+" "+str(tam - b[0])+" "+str(tam - b[2])+" "+str(b[3]))
                print("")


# ******************************************************************************************************
#    MAIN
# ******************************************************************************************************

if __name__ == '__main__':
    # tiempo_inicial = time()

    entrada = [int(a) for a in leerFichero()]
    num_edificios = entrada[0]
    edificios = e = entrada[1:]

    edificios2 = list()
    for a in reversed(edificios):
        edificios2.append(a)
    reves = r = edificios2[:]

    fun_problem = Funambulista(edificios, list(), e, 0)
    fun_problemR = Funambulista(reves, list(), r, 0)
    solucion = list(DivideAndConquerSolver().solve(fun_problem))
    solucionR = list(DivideAndConquerSolver().solve(fun_problemR))

    salida(solucion, solucionR)
    #
    # tiempo_final = time()
    # tiempo_ejecucion = tiempo_final - tiempo_inicial
    # print("")
    # print("El tiempo de ejecucion fue:", tiempo_ejecucion, "segundos")  # En segundos
