import collections
import sys
from time import time

from bt_scheme import *


Pos = Tuple[int, int]

def sokoban_solve ( level_map, player_pos, boxes_start, boxes_end, maximo ):
    class SokobanPS(PartialSolution):

        def __init__(self, decisiones, player_pos, boxes_start):
            self.decisiones: List[Pos] = decisiones #lista con las decisiones tomadas
            self.longDecis = len(self.decisiones) #tamaño lista decisones
            self.longPasillos = len(level_map[0])
            self.boxes_start = tuple(boxes_start) #lista para recorrer las cajas
            self.boxes_end = tuple(boxes_end)
            self.player_pos = player_pos

        def is_solution(self) -> bool:
            # cont=0
            # setBoxesStart = set(self.boxes_start)
            # setBoxesEnd=set(boxes_end)
            # for elem in setBoxesStart:
            #     if elem in setBoxesEnd:
            #         cont+=1
            #     if cont==3:
            #         cont=0
            #         print("Start", self.boxes_start)
            #         print("End", boxes_end)
            #         return True
            # return False

            if collections.Counter(self.boxes_start) == collections.Counter(self.boxes_end):
                print("Start", self.boxes_start)
                print("End", boxes_end)
                return True
            return False

        def get_solution(self) -> Solution:
            return self.decisiones

        def f(self) -> Union[int, float]:
            return self.longDecis

        def state(self) -> State:
            return (self.boxes_start, self.player_pos)


        def successors(self) -> Iterable["PartialSolutionWithOptimization"]:
            if self.longDecis < maximo: #Comprobar que no nos pasamos del maximo dado
                # ¿Puedo mover al jugador?
                if 0 < self.player_pos[0] < len(level_map)-1 and 0 < self.player_pos[1] < self.longPasillos-1: #No salimos del puzle
                    # Subimos
                    if level_map[self.player_pos[0] - 1][self.player_pos[1]] != "#":
                        #Puedo mover al jugardor
                        posSubidaJugador = (self.player_pos[0] - 1, self.player_pos[1])
                        #¿Hay una caja aqui?
                        if posSubidaJugador in self.boxes_start:
                            #¿Puedo mover la caja a la siguiente posicion?
                            if level_map[posSubidaJugador[0] - 1][posSubidaJugador[1]] != "#" and (posSubidaJugador[0]-1, posSubidaJugador[1]) not in self.boxes_start:
                                posSubidaCaja = (posSubidaJugador[0] - 1, posSubidaJugador[1])
                                boxes_start_cambiada = list(self.boxes_start[:])
                                #Muevo la caja
                                boxes_start_cambiada[boxes_start_cambiada.index((posSubidaJugador[0], posSubidaJugador[1]))] = posSubidaCaja
                                yield SokobanPS(self.decisiones + ("U",), posSubidaJugador, boxes_start_cambiada )
                        else:
                            yield SokobanPS(self.decisiones + ("U",), posSubidaJugador, self.boxes_start)


                    # Izquierda
                    if level_map[self.player_pos[0]][self.player_pos[1] - 1] != "#":
                        #Puedo mover al jugardor
                        posSubidaJugador = (self.player_pos[0], self.player_pos[1] - 1)
                        #¿Hay una caja aqui?
                        if posSubidaJugador in self.boxes_start:
                            #¿Puedo mover la caja a la siguiente posicion?
                            if level_map[posSubidaJugador[0]][posSubidaJugador[1]-1] != "#" and (posSubidaJugador[0], posSubidaJugador[1]-1) not in self.boxes_start:
                                posSubidaCaja = (posSubidaJugador[0], posSubidaJugador[1] - 1)
                                boxes_start_cambiada = list(self.boxes_start[:])
                                #Muevo la caja
                                boxes_start_cambiada[boxes_start_cambiada.index((posSubidaJugador[0], posSubidaJugador[1]))] = posSubidaCaja
                                yield SokobanPS(self.decisiones + ("L",), posSubidaJugador, boxes_start_cambiada )
                        else:
                            yield SokobanPS(self.decisiones + ("L",), posSubidaJugador, self.boxes_start)

                    # Bajamos
                    if level_map[self.player_pos[0] + 1][self.player_pos[1]] != "#":
                        #Puedo mover al jugardor
                        posSubidaJugador = (self.player_pos[0] + 1, self.player_pos[1])
                        #¿Hay una caja aqui?
                        if posSubidaJugador in self.boxes_start:
                            #¿Puedo mover la caja a la siguiente posicion?
                            if level_map[posSubidaJugador[0] + 1][posSubidaJugador[1]] != "#" and (posSubidaJugador[0]+1, posSubidaJugador[1]) not in self.boxes_start:
                                posSubidaCaja = (posSubidaJugador[0] + 1, posSubidaJugador[1])
                                boxes_start_cambiada = list(self.boxes_start[:])
                                #Muevo la caja
                                boxes_start_cambiada[boxes_start_cambiada.index((posSubidaJugador[0], posSubidaJugador[1]))] = posSubidaCaja
                                yield SokobanPS(self.decisiones + ("D",), posSubidaJugador, boxes_start_cambiada )
                        else:
                            yield SokobanPS(self.decisiones + ("D",), posSubidaJugador, self.boxes_start)

                    # Derecha
                    if level_map[self.player_pos[0]][self.player_pos[1] + 1] != "#":
                        #Puedo mover al jugardor
                        posSubidaJugador = (self.player_pos[0], self.player_pos[1] + 1)
                        #¿Hay una caja aqui?
                        if posSubidaJugador in self.boxes_start:
                            #¿Puedo mover la caja a la siguiente posicion?
                            if level_map[posSubidaJugador[0]][posSubidaJugador[1]+1] != "#" and (posSubidaJugador[0], posSubidaJugador[1]+1) not in self.boxes_start:
                                posSubidaCaja = (posSubidaJugador[0], posSubidaJugador[1]+ 1)
                                boxes_start_cambiada = list(self.boxes_start[:])
                                #Muevo la caja
                                boxes_start_cambiada[boxes_start_cambiada.index((posSubidaJugador[0], posSubidaJugador[1]))] = posSubidaCaja
                                yield SokobanPS(self.decisiones + ("R",), posSubidaJugador, boxes_start_cambiada )
                        else:
                            yield SokobanPS(self.decisiones + ("R",), posSubidaJugador, self.boxes_start)

    sokoban = SokobanPS((), player_pos, boxes_start)
    return BacktrackingOptSolver.solve(sokoban)


#******************************************************************************************************
#    METODO LEER NIVEL -> level_map: Matriz pareces y pasillos
#                         player_pos: posicion inicial jugador (f,c)
#                         boxes_start: Lista de tuplas (f,c) con posiciones iniciales cajas
#                         boxes_end: Lista de tuplas (f,c) con las posiciones finales de las cajas
#******************************************************************************************************

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

#******************************************************************************************************
#    METODO DE ENTRADA
#******************************************************************************************************

def leerFichero():
    lineas = sys.stdin.readlines()
    return lineas

#******************************************************************************************************
#    MAIN
#******************************************************************************************************

if __name__ == '__main__':

    tiempo_inicial = time()

    entrada = leerFichero()
    salida = read_level(entrada)

    imprime=list(sokoban_solve(salida[0], salida[1], salida[2], salida[3], int(sys.argv[1])))

    if len(imprime)==0:
        print("NO HAY SOLUCIÓN CON LOS MOVIMIENTOS PEDIDOS")
    else:
        for sol in imprime[-1]:
            print(sol, end="")


    tiempo_final = time()
    tiempo_ejecucion = tiempo_final - tiempo_inicial
    print("")
    print ("El tiempo de ejecucion fue:", tiempo_ejecucion, "segundos")  # En segundos


