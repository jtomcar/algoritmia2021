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
        self.posMax=self.edificios.index(max(self.edificios))

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
            valle = altura = posValle = posEdif1 = posEdif2 = 0
            minimo = max(edificios)
            a = b = self.b
            while True:
                edif1 = edificios[b]
                if edificios[a] > edif1 and valle == 0:
                    b = a
                if edificios[a] < edif1 and edificios[a] < minimo:
                    valle = edificios[a]
                    minimo = edificios[a]
                    posValle = a
                if edificios[a] >= edif1 and valle != 0:
                    posEdif2 = a
                    posEdif1 = b
                    altura = edif1 - valle
                    break
                if a == len(edificios) - 1:
                    break
                a = a + 1
            self.sol.append((posEdif1,posEdif2,posValle,altura))
            maximo = 0
            solucion=list()
            for elem in self.sol:
                if elem[3] > maximo:
                    maximo = elem[3]
                    solucion = elem
            return solucion
        self.edificios=list()
        return self.sol

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

    entrada = [int(a) for a in leerFichero()]
    num_edificios = entrada[0]
    edificios = entrada[1:]

    edificios2=list()
    for a in reversed(edificios):
        edificios2.append(a)
    reves=edificios2[:]

    fun_problem = Funambulista(edificios, list(), edificios, 0)
    fun_problemR = Funambulista(reves, list(), reves, 0)
    solucion = list(DivideAndConquerSolver().solve(fun_problem))
    solucionR = list(DivideAndConquerSolver().solve(fun_problemR))

    # print("SOLUCION")
    # print(solucion)
    # print(solucionR)

    if not solucion and not solucionR:
        print("NO HAY SOLUCIÓN")
        exit(0)
    else:
        if not solucionR:
            for sol in solucion:
                print(sol, end=" ")
            print("")
        elif not solucion:
            solucionR = (len(edificios) - 1) - solucionR[1], (len(edificios) - 1) - solucionR[0], (len(edificios) - 1) - \
                        solucionR[2], solucionR[3]
            for sol in solucionR:
                print(sol, end=" ")
            print("")
        else:
            if solucion[3] > solucionR[3]:
                for sol in solucion:
                    print(sol, end=" ")
                print("")
            else:
                solucionR = (len(edificios) - 1) - solucionR[1], (len(edificios) - 1) - solucionR[0], (
                            len(edificios) - 1) - solucionR[2], solucionR[3]
                for sol in solucionR:
                    print(sol, end=" ")
                print("")



    tiempo_final = time()
    tiempo_ejecucion = tiempo_final - tiempo_inicial
    print("")
    print("El tiempo de ejecucion fue:", tiempo_ejecucion, "segundos")  # En segundos
