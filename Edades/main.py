
from media import Media

size = int(input("Indique cuántas edades va a ingresar\n: "))
edades = []

for i in range(size):
    edad = int(input(f"Ingresa la edad {i+1}: "))
    edades.append(edad)

media_calculadora = Media(edades)

media = media_calculadora.calcular_media()

print(f"La media de las edades es: {media:.2f}")
