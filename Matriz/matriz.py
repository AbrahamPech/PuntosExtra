import random

class Matriz:
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.matriz = self.generar_matriz()

    def generar_matriz(self):
    

    def mostrar_matriz(self):
        for fila in self.matriz:
            print(fila)