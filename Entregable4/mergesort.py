from re import T
from typing import List, Iterable

from algoritmia.schemes.divideandconquer import IDivideAndConquerProblem, DivideAndConquerSolver


class MergesortProblem(IDivideAndConquerProblem):
    def __init__(self, a: List[int]):
        self.a = a

    def is_simple(self) -> bool:
        return len(self.a) <= 1

    def trivial_solution(self) -> List[int]:
        return self.a

    def divide(self) -> Iterable["MergesortProblem"]:
        yield MergesortProblem(self.a[:len(self.a)//2])
        yield MergesortProblem(self.a[len(self.a)//2:])

    def combine(self, s: Iterable[List[int]]) -> List[int]:
        a, b = tuple(s)
        c = [None] * (len(a)+len(b))
        i, j, k = 0, 0, 0
        while i < len(a) and j < len(b):
            if a[i] < b[j]: c[k] = a[i]; i += 1
            else: c[k] = b[j]; j += 1
            k += 1
        while i < len(a): c[k] = a[i]; i += 1; k += 1
        while j < len(b): c[k] = b[j]; j += 1; k += 1
        return c

if __name__ == '__main__':
    v = [11, 21, 3, 1, 98, 0, 12, 82, 29, 30, 11, 18, 43, 4, 75, 37]
    # ms_problem es un objeto de la clase MergeSortProblem(IDivideAndConquerProblem)
    ms_problem = MergesortProblem(v)
    # solve(...) es un método estático de la clase DivideAndConquerSolver que
    # recibe un objeto que debe cumplir la interfaz IDivideAndConquerProblem
    solution = DivideAndConquerSolver().solve(ms_problem)
    print("Solution:", solution)
