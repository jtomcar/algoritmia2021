import sys
from time import time

def mayor_beneficio_mem_solve(m, n, M, N, v, d):
    def L(m, n):
        if m >= M or n >= N: return 0
        if (m, n) not in mem:
            maximo=max(L(m+1,n), L(m,n+1)) + v[m, n]
            mem[m, n] = maximo
        return mem[m, n]

    mem = {}
    return L(m, n)



# ******************************************************************************************************
#    METODO DE ENTRADA
# ******************************************************************************************************

def leerFichero():
    v=dict()
    M, N = sys.stdin.readline().split(" ")
    x = sys.stdin.readline()
    diamantes=set()
    for m in range(int(M)):
        for n in range(int(N)):
            v[m, n] = 0
    for elem in sys.stdin.readlines():
        a, b, c = elem.split(" ")
        v[int(a), int(b)] = int(c)
        diamantes.add((a,b))

    return M, N, v, diamantes

# ******************************************************************************************************
#    MAIN
# ******************************************************************************************************

if __name__ == '__main__':
    tiempo_inicial = time()

    sys.setrecursionlimit(5000) #Para que no limite la pila por las limitaciones de python

    M,N,v, d = leerFichero()

    print(mayor_beneficio_mem_solve(0, 0, int(M), int(N), v, d ))
    #
    tiempo_final = time()
    tiempo_ejecucion = tiempo_final - tiempo_inicial
    print("")
    print("El tiempo de ejecucion fue:", tiempo_ejecucion, "segundos")  # En segundos
