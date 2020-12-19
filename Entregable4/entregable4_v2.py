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


    # def divide(self)
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
    num_edificios = entrada[0]
    edificios = entrada[1:]
    # fun_problem = Funambulista(edificios)
    # sol = DivideAndConquerSolver().solve(fun_problem)
    listaMaximos=list()
    lista=list()
    maximo = 0
    resta=0
    pos = 0
    pos2 = 0
    ordenados=list(edificios)
    ordenados.sort(reverse=True)
    while len(listaMaximos) < 10:
        maximo = 0
        for i in range(len(edificios)):
            for j in range(len(edificios)):
                resta=edificios[i]-edificios[j]
                if resta > maximo and resta not in listaMaximos and i<j:
                    maximo = resta
                    pos = i
                    pos2 = j
        lista.append((pos,pos2,maximo))
        listaMaximos.append(maximo)

    continua = True
    while continua:
        for i in range(len(edificios[lista[0][1]:])):
            if edificios[lista[0][0]] <= edificios[lista[0][0]+i]:
                print("Hola", lista[0][1])
                continua=False
            else:
                lista.pop(0)


    print(lista)
    print(listaMaximos)

    #************  PRUEBA **********************************************************
    # sigue=True
    # copia=edificios[:]
    # while sigue:
    #     print("tamCopia",len(copia))
    #     print("tamEdif", len(edificios))
    #     fun_problem = Funambulista(copia)
    #     sol = DivideAndConquerSolver().solve(fun_problem)
    #     sigue=True
    #     ordenados=list(edificios)
    #     ordenados.sort(reverse=True)
    #
    #     k=0
    #     l=1
    #     print("masAlto", sol[1])
    #     masAlto=sol[1]
    #     masBajo=sol[0]
    #     posMasBajo=0
    #     posMasAlto=0
    #     segMasAlto = 0
    #     posSegMasAlto = 0
    #     for i in range(len(ordenados)):
    #         if ordenados[i]==masAlto:
    #             segMasAlto=ordenados[i+1]
    #             break
    #
    #     for i in range(len(edificios)):
    #         if edificios[i]==masBajo:
    #             posMasBajo=i
    #         if edificios[i]==masAlto:
    #             posMasAlto=i
    #         if edificios[i]==segMasAlto:
    #             posSegMasAlto=i
    #             break
    #
    #     print(posMasBajo,posMasAlto)
    #     print("segMasAlto", segMasAlto, posSegMasAlto)
    #
    #     if masBajo in edificios[min(posMasAlto,posSegMasAlto):max(posMasAlto,posSegMasAlto)]:
    #         print("Esta entre ellos")
    #         print(posSegMasAlto, posMasAlto, posMasBajo)
    #         sigue=False
    #     else:
    #         copia.remove(masAlto)


#**************************************************************************************



    # while sigue:
    #     for i in range(len(edificios)):
    #         if ordenados[k]==edificios[i]:
    #             x=i
    #         if ordenados[l]==edificios[i]:
    #             y=i
    #     print(min(edificios))
    #     # #if edificios[min(x,y)]>edificios[max(x,y)]:
    #     # if min(edificios) not in edificios[min(x,y):max(x,y)]:
    #     #     k=k+1
    #     #     l=l+1
    #     #     print("1")
    #     # else:
    #     sigue = False
    #     for elem in edificios[min(x,y)+1:max(x,y)]:
    #         if elem>=min(edificios[x],edificios[y]):
    #             print("2")
    #             k = k + 1
    #             l = l + 1
    #             sigue=True
    #             break
    #
    #     print(edificios[min(x,y)], edificios[max(x,y)])
    #
    # solucion2=edificios[min(x,y):max(x,y)]
    # solucion2.sort()
    # for i in range(len(edificios)):
    #     if solucion2[0]==edificios[i]:
    #         z=i
    #
    # print(min(x,y),max(x,y),z,min(edificios[x],edificios[y])-edificios[z])

    #******************************************************************************

    tiempo_final = time()
    tiempo_ejecucion = tiempo_final - tiempo_inicial
    print("")
    print("El tiempo de ejecucion fue:", tiempo_ejecucion, "segundos")  # En segundos