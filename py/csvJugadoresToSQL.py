import csv

csvJugadores = '../csv/jugadoresDB.csv'
tabla = 'jugadores'

with open(csvJugadores, 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    # Leer la primera fila para obtener los nombres de las columnas
    columnas = next(reader)
    print(columnas)
