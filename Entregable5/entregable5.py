import sys
from time import time


def mayor_beneficio_mem_solve(M, N, v):
    def L(m, n):
        if m < 0 or n < 0: return 0
        if m == 0 and n == 0: return 0
        if (m, n) not in mem:
            if n == 0:
                mem[m, n] = L(m, n - 1) + v[m, n]
            if m == 0:
                mem[m, n] = L(m - 1, n) + v[m, n]
            else:
                mem[m, n] = max(L(m - 1, n), L(m, n - 1)) + v[m, n]
        return mem[m, n]

    mem = {}
    return L(M, N)


# ******************************************************************************************************
#    METODO DE ENTRADA
# ******************************************************************************************************

def leerFichero():
    v = dict()
    M, N = sys.stdin.readline().split(" ")
    x = sys.stdin.readline()
    for m in range(int(M)):
        for n in range(int(N)):
            v[m, n] = 0
    for elem in sys.stdin.readlines():
        a, b, c = elem.split(" ")
        v[int(a), int(b)] = int(c)

    return M, N, v


# ******************************************************************************************************
#    MAIN
# ******************************************************************************************************

if __name__ == '__main__':
    tiempo_inicial = time()

    sys.setrecursionlimit(5000)  # Para que no limite la pila por las limitaciones de python

    M, N, v = leerFichero()

    print(mayor_beneficio_mem_solve(int(M) - 1, int(N) - 1, v))
    #
    tiempo_final = time()
    tiempo_ejecucion = tiempo_final - tiempo_inicial
    print("")
    print("El tiempo de ejecucion fue:", tiempo_ejecucion, "segundos")  # En segundos
