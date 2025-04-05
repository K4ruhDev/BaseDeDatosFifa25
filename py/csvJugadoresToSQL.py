import csv
# Script para generar los inserts SQL a partir del CSV de jugadores

def es_numero(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False

csvJugadores = '../csv/jugadoresDB.csv'
tabla = 'jugadores'

with open('../py/countries.txt', 'r', encoding='utf-8') as txtFile:
    countries = [line.strip() for line in txtFile]

with open('../py/paises.txt', 'r', encoding='utf-8') as txtFile:
    paises = [line.strip() for line in txtFile]

traductor = dict(zip(countries, paises))

with open(csvJugadores, 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    # Leer la primera fila para obtener los nombres de las columnas
    columnas = next(reader)
    print(columnas)
    
    inserts = []

    for fila in reader:
        valores = []
        for valor in fila:
            valor = valor.strip()
            if valor == '':
                valores.append('NULL')
            elif es_numero(valor):
                valores.append(valor)
            elif valor == 'Right':
                valores.append("'Diestro'")
            elif valor == 'Left':
                valores.append("'Zurdo'")
            else:
                if valor in traductor:
                    valor = traductor[valor]

                valorReal = valor.replace("'", "''")    
                valores.append(f"'{valorReal}'")

        insert = f"INSERT INTO {tabla} ({', '.join(columnas)}) VALUES ({', '.join(valores)});"
        inserts.append(insert)
print(inserts)

# Guardar los inserts en un archivo SQL
with open('../sql/insertJugadores.sql', 'w', encoding='utf-8') as sqlfile:
    for insert in inserts:
        sqlfile.write(insert + '\n')
    print(f"Se han generado {len(inserts)} sentencias INSERT.")


