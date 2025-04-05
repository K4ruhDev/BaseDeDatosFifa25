import csv
# Script para generar los inserts SQL a partir del CSV de ligas

def es_numero(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False

csvLigas = '../csv/leagues.csv'
tabla = 'ligas'

with open(csvLigas, 'r', encoding='utf-8') as csvfile:
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
                valorReal = valor.replace("'", "''")    
                valores.append(f"'{valorReal}'")

        insert = f"INSERT INTO {tabla} ({', '.join(columnas)}) VALUES ({', '.join(valores)});"
        inserts.append(insert)
print(inserts)


# Guardar los inserts en un archivo SQL
with open('../sql/insertLigas.sql', 'w', encoding='utf-8') as sqlfile:
    for insert in inserts:
        sqlfile.write(insert + '\n')
    print(f"Se han generado {len(inserts)} sentencias INSERT.")


