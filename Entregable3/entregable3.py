from typing import *
import sys
from Utils.bt_scheme import PartialSolutionWithOptimization, BacktrackingOptSolver, State, Solution


Pos = Tuple[int, int]


def read_level(puzle_lines: List[str]) -> Tuple[List[str], Pos, List[Pos], List[Pos]]:
    # Averigua la posición del jugador y las posiciones iniciales y finales de las cajas
    player_pos, boxes_start, boxes_end = None, [], []
    num_rows = len(puzle_lines)
    num_cols = len(puzle_lines[0].strip())
    for r in range(num_rows):
        for c in range(num_cols):
            if puzle_lines[r][c] == 'p':
                player_pos = (r, c)
            elif puzle_lines[r][c] == 'o':
                boxes_start.append((r, c))
            elif puzle_lines[r][c] == 'x':
                boxes_end.append((r, c))

    # Crea un mapa (incluye únicamente paredes y pasillos, borra 'p','x' y 'o'):
    tr = str.maketrans("pxo", "   ")
    level_map = []
    for l in puzle_lines:
        level_map.append(l.strip().translate(tr))

    return level_map, player_pos, boxes_start, boxes_end

# def solucion():


def leerFichero():
    lineas = sys.stdin.readlines()
    return lineas



if __name__ == '__main__':
    entrada = leerFichero()
    salida = read_level(entrada)

    for elem in salida[0]:
        print(elem)
    print(salida[1])
    print(salida[2])
    print(salida[3])





