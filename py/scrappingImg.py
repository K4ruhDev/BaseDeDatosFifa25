
import pandas as pd
import re
import random

def generar_enlace_imagen(codigo):
    if pd.isna(codigo):
        return None
    return f"https://cmtracker.fra1.cdn.digitaloceanspaces.com/DB/25/heads/p{codigo}.png"

def asignar_precio(rat):
    if pd.isna(rat) or rat == '':
        return None
    rat = int(rat)
    if rat >= 90:
        return random.randint(3000000, 4000000)
    elif rat >= 85:
        return random.randint(2000000, 3000000)
    elif rat >= 80:
        return random.randint(1500000, 2000000)
    elif rat >= 70:
        return random.randint(800000, 1500000)
    elif rat >= 60:
        return random.randint(400000, 800000)
    else:  #
        return random.randint(200000, 400000)

def main():
    archivo_csv = '../csv/cartasJugadores.csv'
    cartas = pd.read_csv(archivo_csv)
    cartas.columns = cartas.columns.str.strip() 
    cartas['precio'] = cartas['rat'].apply(asignar_precio)
    cartas.to_csv('../csv/cartasJugadores.csv', index=False)
    if 'codigo_Fifa' in cartas.columns:
        print(cartas[['codigo_Fifa']].head())
        cartas['codigo_Fifa'] = cartas['codigo_Fifa'].astype(str).str.strip()
        #cartas['enlace_imagen'] = cartas['codigo_Fifa'].apply(generar_enlace_imagen)
        # Generar ademas un precio a la cartas
        print(cartas[['codigo_Fifa', 'enlace_imagen']].head())
        print(cartas.columns)
        
if __name__ == "__main__":
    main()
    
    