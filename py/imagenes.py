import os
import requests
import re

carpeta = "../img/"
txt = "../txt/links.txt"

with open(txt,'r') as f:
    enlaces = f.readlines()

patron = r'p(\d+)\.png'

for i, url in enumerate(enlaces):
    url = url.strip()
    if not url: continue
    
    try:
        coincidencia = re.search(patron, url)
        if coincidencia:
            nombreFoto = f"{coincidencia.group(1)}.png"
        else:
            nombreFoto = f"imagen_{i}"
        ruta = os.path.join(carpeta,nombreFoto)
        
        resp = requests.get(url, timeout=5)
        with open(ruta,'wb') as archivo:
            archivo.write(resp.content)
    except Exception as e:    
        print(f"Error: {e}")