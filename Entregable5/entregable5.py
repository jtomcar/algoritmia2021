import sys
from time import time

def mayor_beneficio_mem_solve(m, n, M, N, v, x):
    def L(m, n):
        if m >= M or n >= N: return 0
        if (m, n) not in mem:
            mem[m, n] = max(L(m, n + 1), L(m + 1, n)) + v[m, n]
        return mem[m, n]

    mem = {}
    return L(m,n)

# ******************************************************************************************************
#    METODO DE ENTRADA
# ******************************************************************************************************

def leerFichero():
    v=dict()
    M, N = sys.stdin.readline().split(" ")
    x = sys.stdin.readline()
    for m in range(int(M)):
        for n in range(int(N)):
            v[m, n] = 0
    for elem in sys.stdin.readlines():
        a, b, c = elem.split(" ")
        v[int(a), int(b)] = int(c)

    return M, N, v, x

# ******************************************************************************************************
#    MAIN
# ******************************************************************************************************

if __name__ == '__main__':
    tiempo_inicial = time()

    sys.setrecursionlimit(5000) #Para que no limite la pila por las limitaciones de python

    M,N,v,x= leerFichero()

    # nf, nc = entrada[0].split(" ")
    # diamantes=entrada[2:]
    # print(diamantes)
    # v = dict()
    # for m in range(int(nf)):
    #     for n in range(int(nc)):
    #         v[m, n] = 0
    # for i in range(len(entrada[2:])):
    #     a, b, c = entrada[i + 2].split(" ")
    #     v[int(a), int(b)] = int(c)

    print(mayor_beneficio_mem_solve(0, 0, int(M), int(N), v, x))
    #
    tiempo_final = time()
    tiempo_ejecucion = tiempo_final - tiempo_inicial
    print("")
    print("El tiempo de ejecucion fue:", tiempo_ejecucion, "segundos")  # En segundos
