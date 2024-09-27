import random

class Matriz:
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.matriz = self.generar_matriz()

    def generar_matriz(self):
        return [[random.randint(0, 100) for _ in range(self.columnas)] for _ in range(self.filas)]

    def mostrar_matriz(self):
        for fila in self.matriz:
            print(fila)