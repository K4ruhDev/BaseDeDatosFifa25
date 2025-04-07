import csv
import pandas

def es_numero(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False

csvCartas = '../csv/cartasJugadores.csv'
tabla = 'cartas'

with open(csvCartas, 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
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
                valorReal = valor.replace("'", "''")    
                valores.append(f"'{valorReal}'")            

        insert = f"INSERT INTO {tabla} ({', '.join(columnas)}) VALUES ({', '.join(valores)});"
        inserts.append(insert)

# Guardar los inserts en un archivo SQL
with open('../sql/insertCartas.sql', 'w', encoding='utf-8') as sqlfile:
    for insert in inserts:
        sqlfile.write(insert + '\n')
    print(f"Se han generado {len(inserts)} sentencias INSERT.")
