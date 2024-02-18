import requests
import os


os.chdir('/workspaces/PC4Python/Problema04')

url = 'https://api.coindesk.com/v1/bpi/currentprice.json'

response = requests.get(url)
with open('obtener_precio_bitcoin.txt', 'wb') as f:
    f.write(response.content)
    pass
