import requests
from bs4 import BeautifulSoup

url = 'https://www.cmtracker.net/players/238794'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

divs = soup.find_all('div', class_='Playerv2_player__main_info_box_item__6loQN')

div = divs[1]
span = div.find('span')
if span:
    print(span.text)