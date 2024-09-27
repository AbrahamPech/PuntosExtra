from matriz import Matriz

filas = int(input("Introduce el número de filas: "))
columnas = int(input("Introduce el número de columnas: "))

matriz = Matriz(filas, columnas)

print("\nMatriz generada con números aleatorios:")
matriz.mostrar_matriz()