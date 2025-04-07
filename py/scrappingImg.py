
import pandas as pd
import re

def generar_enlace_imagen(codigo):
    if pd.isna(codigo):
        return None
    return f"https://cmtracker.fra1.cdn.digitaloceanspaces.com/DB/25/heads/p{codigo}.png"


def main():
    archivo_csv = '../csv/cartasJugadores.csv'
    cartas = pd.read_csv(archivo_csv)
    cartas.columns = cartas.columns.str.strip() 
    if 'codigo_Fifa' in cartas.columns:
        print(cartas[['codigo_Fifa']].head())
        cartas['codigo_Fifa'] = cartas['codigo_Fifa'].astype(str).str.strip()
        cartas['enlace_imagen'] = cartas['codigo_Fifa'].apply(generar_enlace_imagen)
        print(cartas[['codigo_Fifa', 'enlace_imagen']].head())
        print(cartas.columns)
        cartas.to_csv('../csv/cartasJugadores.csv', index=False)
        
if __name__ == "__main__":
    main()