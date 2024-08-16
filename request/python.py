#Request para LIDER
import requests
from bs4 import BeautifulSoup

# Lista de URLs
urls = [
    'https://www.lider.cl/catalogo/product/sku/23ANNGJUTCWN/playstation-hogwarts-legacy-4-eu-import',
    'https://www.lider.cl/catalogo/product/sku/1014062/nintendo-videojuego-super-smash-bros-ultimate',
    'https://www.lider.cl/catalogo/product/sku/1YO7GODU9JMJ/nintendo-mario-sonic-at-the-olympic-games-switch']

for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Buscar el elemento <h1> que contiene el nombre del juego
    titulo_elemento = soup.find('h1', class_='server-title')

    # Buscar el elemento <strong> que contiene el precio
    precio_elemento = soup.find('strong', string=lambda t: t and 'Precio' in t)

    # Imprimir el nombre del juego y el precio
    if titulo_elemento:
        print(f"Nombre del juego: {titulo_elemento.text.strip()}")
    else:
        print("No se encontró el nombre del juego.")
    
    if precio_elemento:
        print(f"Precio: {precio_elemento.text.strip()}")
    else:
        print("No se encontró el precio.")
    
    print()  # Línea en blanco para separar los resultados de diferentes URLs
