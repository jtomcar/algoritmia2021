import sys
from time import time
from typing import *

from algoritmia.schemes.divideandconquer import *

def trocea(edificios, k, i):
    edif2 = valle = altura = posValle = posEdif1 = posEdif2 = 0
    minimo = max(edificios)
    while True:
        edif1 = edificios[k]
        if edificios[i] > edif1 and valle == 0:
            k = i
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
            break
        i = i + 1
    return (posEdif1,posEdif2,posValle,altura,posEdif2,posEdif2)

class Funambulista(IDivideAndConquerProblem):
    def __init__(self, edificios: List[int], sol: List[int], k, i):
        self.edificios = edificios
        self.k = k
        self.i = i
        self.sol = sol

    def is_simple(self) -> "bool":
        return len(self.sol) >= self.k+1

    def trivial_solution(self):
        if len(edificios) <=2:
            return 0
        return self.sol

    def divide(self) -> Iterable["Funambulista"]:
        trozo=trocea(self.edificios,self.k,self.i)
        self.sol.append(trozo[:4])
        yield Funambulista(self.edificios, self.sol, trozo[4], trozo[5])

    def combine(self, s: Iterable[List[int]]) -> Union[tuple, int]:
        a = tuple(s)
        maximo = 0
        solucion=list()
        for elem in self.sol:
            if elem[3] > maximo:
                maximo = elem[3]
                solucion = elem

        return solucion

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

    entrada = [int(i) for i in leerFichero()]
    num_edificios = entrada[0]
    edificios = entrada[1:]

    edificios2=list()
    for i in reversed(edificios):
        edificios2.append(i)
    reves=edificios2[:]

    fun_problem = Funambulista(edificios, list(), 0, 0)
    fun_problemR = Funambulista(reves, list(), 0, 0)
    solucion = list(DivideAndConquerSolver().solve(fun_problem))
    solucionR = list(DivideAndConquerSolver().solve(fun_problemR))

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
