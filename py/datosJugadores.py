# Script usado para crear el CSV de jugadores para la base de datos usando pandas
import pandas as pd

# Leer los archivos CSV
jugadores = pd.read_csv('../csv/general_players.csv')
equipos = pd.read_csv('../csv/teams.csv')

jugadores['Team'] = jugadores['Team'].str.strip()
equipos['equipo'] = equipos['equipo'].str.strip()

#Crear un diccionario para mapear los nombres de los equipos a sus IDs
equipoToId = dict(zip(equipos['equipo'], equipos['id_equipo']))

# # Añadir la columna 'idEquipo' a los jugadores usando el diccionario
jugadores['idEquipo'] = jugadores['Team'].map(equipoToId)

# print(jugadores[['Team', 'idEquipo']]) Print para debug

"""
Columnas del CSV Jugadores
Unnamed: 0.1,Unnamed: 0,Rank,Name,RAT,PAC,SHO,PAS,DRI,DEF,PHY,Position,Weak foot,Preferred foot,Height,Nation,League,Team,url,idEquipo
"""

columnasBorrar = [
    'Rank', 'RAT', 'PAC', 'SHO', 'PAS',
    'DRI', 'DEF', 'PHY', 'Position', 'Weak foot', 'Team',
    'League', 'url'
]

nuevosJugadores = jugadores.drop(columns=columnasBorrar)

nuevosJugadores.to_csv('../csv/jugadoresDB.csv', index=False)

# Sacar las cartas de los jugadores
columnasBorrar = [
    "Preferred foot", "Height", "Nation", "League"
]

jugadores['codigo_Fifa'] = jugadores['url'].str.extract(r'/(\d+)$')

cartasJugadores = jugadores.drop(columns=columnasBorrar)

cartasJugadores.to_csv('../csv/cartasJugadores.csv')


