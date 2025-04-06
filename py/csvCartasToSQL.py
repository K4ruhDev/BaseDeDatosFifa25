import csv
# Script para generar los inserts SQL a partir del CSV de general_players

def es_numero(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False

csvCartas = '../csv/general_players.csv'
tabla = 'cartas'

with open('../txt/castellano.txt', 'r', encoding='utf-8') as txtFile:
    castellano = [line.strip() for line in txtFile]

with open('../txt/english.txt', 'r', encoding='utf-8') as txtFile:
    english = [line.strip() for line in txtFile]

traductor = dict(zip(english, castellano))

with open(csvCartas, 'r', encoding='utf-8') as csvfile:
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
            else:
                if valor in traductor:
                    valor = traductor[valor]
                valorReal = valor.replace("'", "''")    
                valores.append(f"'{valorReal}'")

        insert = f"INSERT INTO {tabla} ({', '.join(columnas)}) VALUES ({', '.join(valores)});"
        inserts.append(insert)


# Guardar los inserts en un archivo SQL
"""with open('../sql/insertCartas.sql', 'w', encoding='utf-8') as sqlfile:
    for insert in inserts:
        sqlfile.write(insert + '\n')
    print(f"Se han generado {len(inserts)} sentencias INSERT.")"""


