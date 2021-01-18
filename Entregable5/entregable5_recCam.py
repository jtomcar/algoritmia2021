import sys
from time import time

from algoritmia.utils import infinity


def mayor_beneficio_mem_solve(M, N, v):
    def L(m, n):
        if m < 0 or n < 0: return 0
        if m == 0 and n == 0: return 0
        if (m, n) not in mem:
            mem[m,n]=-infinity, ()
            if m == 0:
                mem[m, n] = L(m, n - 1) + v[m, n],(m,n-1)
            elif n == 0:
                mem[m, n] = L(m - 1, n) + v[m, n],(m-1,n)
            else:
                if v[m-1,n]>v[m,n-1]:
                    mPrev, nPrev = m-1, n
                else:
                    mPrev, nPrev = m , n-1
                mem[m, n] = max(L(m - 1, n), L(m, n - 1)) + v[m, n],(mPrev,nPrev)
        return mem[m, n][0]
    mem = {}
    score=L(M,N)
    sol=[]
    m,n = M,N
    while (m,n) != (0,0):
        _,(mPrev,nPrev) = mem[m,n]
        if mPrev!=0 and nPrev!=0:
            sol.append(max(v[mPrev-1, nPrev],v[mPrev, nPrev-1])+v[mPrev, nPrev])
        m,n=mPrev,nPrev
    sol.reverse()
    return score, sol


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
