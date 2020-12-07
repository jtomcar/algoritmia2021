import sys
from time import time
from typing import List, Tuple, Iterable

from bt_scheme import PartialSolution, Solution, Union, State, BacktrackingOptSolver

Pos = Tuple[int, int]


def nuevo_mapa(level_map, player_pos, boxes_start, boxes_end, pos_caja, decide):
    decision = ""
    if decide == 0:
        decision = ("U",)
    if decide == 1:
        decision = ("L",)
    if decide == 2:
        decision = ("D",)
    if decide == 3:
        decision = ("R",)
    if pos_caja == 0:
        return (level_map, player_pos, boxes_start, boxes_end, decision)
    else:
        boxes_start[boxes_start.index(player_pos)] = pos_caja
        return (level_map, player_pos, boxes_start, boxes_end, decision)

def sokoban_solve(initial_level, maximo):
    class SokobanPS(PartialSolution):
        def __init__(self, decisiones, new_level):
            self.level_map = new_level[0]
            self.decisiones: List[Pos] = decisiones #lista con las decisiones tomadas
            self.longDecis = len(self.decisiones)  # tamaño lista decisones
            self.boxes_start = set(new_level[2])  # lista para recorrer las cajas
            self.boxes_end = set(new_level[3])
            self.player_pos = new_level[1]

        def is_solution(self) -> bool:
            if self.boxes_start == self.boxes_end:
                return True
            return False

        def get_solution(self) -> Solution:
            return self.decisiones

        def f(self) -> Union[int, float]:
            return self.longDecis  # Valor del diccionario

        def state(self) -> State:
            return (self.player_pos+tuple(self.boxes_start))  # Es la clave del diccionario

        def successors(self) -> Iterable["SokobanPS"]:
            if self.longDecis < maximo:
                # Subimos
                if self.level_map[self.player_pos[0] - 1][self.player_pos[1]] != "#":
                    if (self.player_pos[0] - 1, self.player_pos[1]) in self.boxes_start:
                        if self.level_map[self.player_pos[0] - 2][self.player_pos[1]] != "#":
                            if (self.player_pos[0] - 2, self.player_pos[1]) not in self.boxes_start:
                                nuevo_nivel = nuevo_mapa(self.level_map, (self.player_pos[0] - 1, self.player_pos[1]),
                                                         list(self.boxes_start),
                                                         self.boxes_end, (self.player_pos[0] - 2, self.player_pos[1]),
                                                         0)
                                yield SokobanPS(self.decisiones + nuevo_nivel[-1], nuevo_nivel[0:4])
                    else:
                        nuevo_nivel = nuevo_mapa(self.level_map, (self.player_pos[0] - 1, self.player_pos[1]),
                                                 self.boxes_start, self.boxes_end, 0, 0)
                        yield SokobanPS(self.decisiones + nuevo_nivel[-1], nuevo_nivel[0:4])

                # Izquierda
                if self.level_map[self.player_pos[0]][self.player_pos[1] - 1] != "#":
                    if (self.player_pos[0], self.player_pos[1] - 1) in self.boxes_start:
                        if self.level_map[self.player_pos[0]][self.player_pos[1] - 2] != "#":
                            if (self.player_pos[0], self.player_pos[1] - 2) not in self.boxes_start:
                                nuevo_nivel = nuevo_mapa(self.level_map, (self.player_pos[0], self.player_pos[1] - 1),
                                                         list(self.boxes_start),
                                                         self.boxes_end, (self.player_pos[0], self.player_pos[1] - 2),
                                                         1)
                                yield SokobanPS(self.decisiones + nuevo_nivel[-1], nuevo_nivel[0:4])
                    else:
                        nuevo_nivel = nuevo_mapa(self.level_map, (self.player_pos[0], self.player_pos[1] - 1),
                                                 self.boxes_start, self.boxes_end, 0, 1)
                        yield SokobanPS(self.decisiones + nuevo_nivel[-1], nuevo_nivel[0:4])

                # Bajamos
                if self.level_map[self.player_pos[0] + 1][self.player_pos[1]] != "#":
                    if (self.player_pos[0] + 1, self.player_pos[1]) in self.boxes_start:
                        if self.level_map[self.player_pos[0] + 2][self.player_pos[1]] != "#":
                            if (self.player_pos[0] + 2, self.player_pos[1]) not in self.boxes_start:
                                nuevo_nivel = nuevo_mapa(self.level_map, (self.player_pos[0] + 1, self.player_pos[1]),
                                                         list(self.boxes_start),
                                                         self.boxes_end, (self.player_pos[0] + 2, self.player_pos[1]),
                                                         2)
                                yield SokobanPS(self.decisiones + nuevo_nivel[-1], nuevo_nivel[0:4])
                    else:
                        nuevo_nivel = nuevo_mapa(self.level_map, (self.player_pos[0] + 1, self.player_pos[1]),
                                                 self.boxes_start, self.boxes_end, 0, 2)
                        yield SokobanPS(self.decisiones + nuevo_nivel[-1], nuevo_nivel[0:4])

                # Derecha
                if self.level_map[self.player_pos[0]][self.player_pos[1] + 1] != "#":
                    if (self.player_pos[0], self.player_pos[1] + 1) in self.boxes_start:
                        if self.level_map[self.player_pos[0]][self.player_pos[1] + 2] != "#":
                            if (self.player_pos[0], self.player_pos[1] + 2) not in self.boxes_start:
                                nuevo_nivel = nuevo_mapa(self.level_map, (self.player_pos[0], self.player_pos[1] + 1),
                                                         list(self.boxes_start),
                                                         self.boxes_end, (self.player_pos[0], self.player_pos[1] + 2),
                                                         3)
                                yield SokobanPS(self.decisiones + nuevo_nivel[-1], nuevo_nivel[0:4])
                    else:
                        nuevo_nivel = nuevo_mapa(self.level_map, (self.player_pos[0], self.player_pos[1] + 1),
                                                 self.boxes_start, self.boxes_end, 0, 3)
                        yield SokobanPS(self.decisiones + nuevo_nivel[-1], nuevo_nivel[0:4])

    sokoban = SokobanPS((), initial_level)
    return BacktrackingOptSolver.solve(sokoban)


# ******************************************************************************************************
#    METODO LEER NIVEL -> self.level_map: Matriz pareces y pasillos
#                         player_pos: posicion inicial jugador (f,c)
#                         boxes_start: Lista de tuplas (f,c) con posiciones iniciales cajas
#                         boxes_end: Lista de tuplas (f,c) con las posiciones finales de las cajas
# ******************************************************************************************************

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

    # Crea un level_map (incluye únicamente paredes y pasillos, borra 'p','x' y 'o'):
    tr = str.maketrans("pxo", "   ")
    level_map = []
    for l in puzle_lines:
        level_map.append(l.strip().translate(tr))

    return level_map, player_pos, boxes_start, boxes_end


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

    # tiempo_inicial = time()

    solucion = list(sokoban_solve(read_level(leerFichero()), int(sys.argv[1])))

    if len(solucion):
        for sol in solucion[-1]:
            print(sol, end="")
    else:
        print("NO HAY SOLUCIÓN CON LOS MOVIMIENTOS PEDIDOS")
    #
    #
    # tiempo_final = time()
    # tiempo_ejecucion = tiempo_final - tiempo_inicial
    # print("")
    # print("El tiempo de ejecucion fue:", tiempo_ejecucion, "segundos")  # En segundos
