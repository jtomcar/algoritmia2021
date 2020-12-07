import sys
from time import time
from typing import *

from algoritmia.schemes.divideandconquer import *

class Funambulista(IDivideAndConquerProblem):
    def __init__(self, edificios: List[int]):
        self.edificios=edificios
        self.num_elem = len(edificios)
        self.b = 0
        self.e = len(edificios)
        self.h = (self.b + self.e) // 2

    def is_simple(self) -> "bool":
        return self.num_elem <= 3

    def trivial_solution(self) -> Tuple[int, int, int, int]:
        if self.num_elem==3:
            if self.edificios[self.h] < self.edificios[self.b] and self.edificios[self.h] < self.edificios[self.e - 1]:
                return self.b, self.e - 1, self.h, min(self.edificios[self.b], self.edificios[self.e - 1]) - self.edificios[self.h]
        return 0, 0, 0, 0  # trivial_solution

    def divide(self):
        pass

    def combine(self, solutions):
        pass
    # def divide(self) -> "Iterable<IDivideAndConquerProblem>":
    #     pass
    #
    # def combine(self, solutions: "Iterable<Solution>") -> "Solution":
    #     pass


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
    ms_problem = Funambulista(entrada[1:])
    solucion = DivideAndConquerSolver().solve(ms_problem)

    if solucion == (0, 0, 0, 0):
        print("NO HAY SOLUCIÓN")
    else:
        for sol in solucion:
            print(sol, end=" ")
        print("")

    tiempo_final = time()
    tiempo_ejecucion = tiempo_final - tiempo_inicial
    print("")
    print("El tiempo de ejecucion fue:", tiempo_ejecucion, "segundos")  # En segundos
