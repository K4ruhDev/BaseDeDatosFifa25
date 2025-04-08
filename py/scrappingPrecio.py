import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

def asignar_precio(codigo):
    try:
        if pd.isna(codigo) or codigo == '':
            return None
        
        url = f'https://www.cmtracker.net/players/{codigo}'  # Formato correcto de URL con f-string
        
        response = requests.get(url)
        response.raise_for_status()  # Verifica si la solicitud fue exitosa
        
        soup = BeautifulSoup(response.text, 'html.parser')
        divs = soup.find_all('div', class_='Playerv2_player__main_info_box_item__6loQN')
        
        if len(divs) < 2:
            return None
            
        div = divs[1]
        span = div.find('span')
        
        if span:
            precio = span.text.strip()
            if 'K' in precio:
                valor = float(precio[1:].replace('K', ''))
                convertido = str(int(valor * 1000))
                print(convertido)
                return convertido
            else:
                print('no entar')
                return precio  # Devuelve el precio sin formato 'k'
        return None  # Si no encuentra el span
    
    except Exception as e:
        print(f"Error al procesar el código {codigo}: {str(e)}")
        return None

def main():
    archivo_csv = '../csv/cartasJugadores.csv'
    
    # Verifica si el archivo existe
    if not os.path.exists(archivo_csv):
        print(f"El archivo {archivo_csv} no existe.")
        return
    
    try:
        cartas = pd.read_csv(archivo_csv)
        cartas.columns = cartas.columns.str.strip()
        print(cartas.columns)
        
        if 'cod_carta' in cartas.columns:
            cartas['cod_carta'] = cartas['cod_carta'].astype(str).str.strip()         
            # Generar además un precio a las cartas
            cartas['precio'] = cartas['cod_carta'].apply(asignar_precio)
            with open('../txt/precios.txt', 'w') as txt:
                for index, row in cartas.iterrows():
                    txt.write(f"{row['precio']}\n")
                print("Precios asignados y archivo guardado correctamente.")
        else:
            print("La columna 'cod_carta' no existe en el dataframe.")
    
    except Exception as e:
        print(f"Error al procesar el archivo CSV: {str(e)}")

if __name__ == "__main__":
    main()
