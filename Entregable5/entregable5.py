import sys

def mayor_beneficio_mem_solve(M, N, v):
    def L(m, n):
        if m == 0 and n == 0: return 0
        if (m, n) not in mem:
            if (m,n) not in v:
                if m == 0:
                    mem[m, n] = L(m, n - 1)
                elif n == 0:
                    mem[m, n] = L(m - 1, n)
                else:
                    mem[m, n] = max(L(m - 1, n), L(m, n - 1))
            else:
                if m == 0:
                    mem[m, n] = L(m, n - 1) + v[m, n]
                elif n == 0:
                    mem[m, n] = L(m - 1, n) + v[m, n]
                else:
                    mem[m, n] = max(L(m - 1, n), L(m, n - 1)) + v[m, n]

        return mem[m, n]
    mem = {}
    return L(M, N)

# ******************************************************************************************************
#    MAIN
# ******************************************************************************************************

if __name__ == '__main__':
    sys.setrecursionlimit(5000)
    v = {}
    M, N = sys.stdin.readline().split(" ")
    M = int(M)
    N = int(N)
    x = sys.stdin.readline()
    for elem in sys.stdin.readlines():
        a, b, c = elem.split(" ")
        v[int(a), int(b)] = int(c)

    print(mayor_beneficio_mem_solve(M - 1, N - 1, v))
