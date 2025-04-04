import csv
# Script para generar los inserts SQL a partir del CSV de jugadores

csvJugadores = '../csv/jugadoresDB.csv'
tabla = 'jugadores'

with open(csvJugadores, 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    # Leer la primera fila para obtener los nombres de las columnas
    columnas = next(reader)
    print(columnas)
    
    inserts = []

    for fila in reader:
        valores = []
        for valor in fila:
            valorReal = valor.replace("'", "''")  
            valores.append(f"'{valorReal}'")

        insert = f"INSERT INTO {tabla} ({', '.join(columnas)}) VALUES ({', '.join(valores)});"
        inserts.append(insert)


# Guardar los inserts en un archivo SQL
with open('../sql/insertJugadores.sql', 'w', encoding='utf-8') as sqlfile:
    for insert in inserts:
        sqlfile.write(insert + '\n')
    print(f"Se han generado {len(inserts)} sentencias INSERT.")

