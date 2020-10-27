from typing import *
from sys import *
from algoritmia.datastructures.digraphs import UndirectedGraph
from algoritmia.datastructures.mergefindsets import MergeFindSet
from random import shuffle, seed
from labyrinthviewer import LabyrinthViewer

def laberintoMensaje(instancia):
    print(instancia)





def leerFichero(fichEntrada):
   fich=open(fichEntrada,"r",encoding="utf-8")
   lista=[]
   for linea in fich:
       elem = [int(x) for x in linea.rstrip("\n").split(" ")]
       elem=tuple(elem) #Convertimos lista a tupla
       lista.append(elem)
   return lista

if __name__ == '__main__':

   fichEntrada = leerFichero(argv[1])
   laberintoMensaje(fichEntrada)