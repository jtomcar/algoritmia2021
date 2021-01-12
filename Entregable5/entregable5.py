import sys
from time import time


def mayor_beneficio_mem_solve(fil, col, nFilas: int, nColumnas: int, diamantes):
    def L(fil, col):
        if fil > nFilas - 1 or col > nColumnas - 1: return 0 #No sale de la matriz
        if fil == nFilas - 1 and col == nColumnas - 1:
            print(mem)
            return diamantes[fil, col] #Es la última posición
        if (fil, col) not in mem:
            print(mem)
            f_abajo, c_derecha = fil + 1, col + 1
            mem[fil, col] = max( diamantes[fil, col] + L(fil, c_derecha), diamantes[fil, col] + L(f_abajo, col))
        return mem[fil, col]

    mem = dict()
    return L(fil, col)


# ******************************************************************************************************
#    METODO DE ENTRADA Y SALIDA
# ******************************************************************************************************

def leerFichero():
    lineas = sys.stdin.readlines()
    return lineas


# ******************************************************************************************************
#    MAIN
# ******************************************************************************************************

if __name__ == '__main__':
    tiempo_inicial = time()

    sys.setrecursionlimit(5000) #Para que no limite la pila por las limitaciones de python

    entrada = leerFichero()
    nf, nc = entrada[0].split(" ")
    diamantes = dict()
    for fil in range(int(nf)):
        for col in range(int(nc)):
            diamantes[fil, col] = 0
    for i in range(len(entrada[2:])):
        a, b, c = entrada[i + 2].split(" ")
        diamantes[int(a), int(b)] = int(c)

    print(mayor_beneficio_mem_solve(0, 0, int(nf), int(nc), diamantes))

    tiempo_final = time()
    tiempo_ejecucion = tiempo_final - tiempo_inicial
    print("")
    print("El tiempo de ejecucion fue:", tiempo_ejecucion, "segundos")  # En segundos
