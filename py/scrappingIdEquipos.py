import requests
from bs4 import BeautifulSoup
import time

def get_team_ids():
    """Obtiene las IDs de los equipos de CMTracker y guarda en un archivo de texto"""
    
    # Lista de equipos del archivo proporcionado
    with open('../txt/equipos.txt', 'r', encoding='utf-8') as f:
        teams = [line.strip() for line in f if line.strip()]
    
    # URL base
    base_url = "https://www.cmtracker.net/en/teams/"
    
    # Obtener la página principal de equipos
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Diccionario para almacenar {nombre_equipo: id}
    team_ids = {}
    
    # Encontrar todos los enlaces a equipos
    team_links = soup.select('a[href^="/en/teams/"]')
    
    for link in team_links:
        team_name = link.text.strip()
        href = link.get('href')
        if href and '/en/teams/' in href:
            team_id = href.split('/')[-1]
            # Solo guardar si es un ID numérico
            if team_id.isdigit():
                team_ids[team_name] = team_id
    
    # Crear un archivo de texto con los resultados
    with open('../txt/equiposId.txt', 'w', encoding='utf-8') as txtfile:
        txtfile.write("Nombre\tID\n")  # Encabezado
        
        # Buscar coincidencias para cada equipo de la lista
        for team in teams:
            if team in team_ids:
                txtfile.write(f"{team}\t{team_ids[team]}\n")
            else:
                # Buscar coincidencias parciales
                matches = []
                for key in team_ids.keys():
                    if team.lower() in key.lower() or key.lower() in team.lower():
                        matches.append((key, team_ids[key]))
                
                if matches:
                    # Usar la primera coincidencia parcial
                    txtfile.write(f"{team}\t{matches[0][1]} (posible coincidencia con {matches[0][0]})\n")
                else:
                    txtfile.write(f"{team}\tNo encontrado\n")
    
    print(f"Se han procesado {len(teams)} equipos y guardado los resultados en 'team_ids.txt'")

if __name__ == "__main__":
    get_team_ids()