import requests
from bs4 import BeautifulSoup
import pandas as pd

def asignar_precio(codigo):
    url = 'https://www.cmtracker.net/players/{codigo}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    divs = soup.find_all('div', class_='Playerv2_player__main_info_box_item__6loQN')
    div = divs[1]
    span = div.find('span')
    if span:
        precio = span.text.strip()
        if 'k' in precio:
            return precio.replace('k', '') + '000'

def main():
    archivo_csv = '../csv/cartasJugadores.csv'
    cartas = pd.read_csv(archivo_csv)
    cartas.columns = cartas.columns.str.strip() 
    if 'codigo_fifa' in cartas.columns:
        # Generar ademas un precio a la cartas
        cartas['precio'] = cartas['codigo_fifa'].apply(asignar_precio)
        cartas.to_csv('../csv/cartasJugadores.csv', index=False)
    
if __name__ == "__main__":
    main()