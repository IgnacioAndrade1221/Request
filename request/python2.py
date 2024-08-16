import requests

url = 'https://www.lider.cl/catalogo/product/sku/23ANNGJUTCWN/playstation-hogwarts-legacy-4-eu-import'
response = requests.get(url)

# Imprime una parte del HTML para inspeccionar
print(response.text[:10000])  # Imprime los primeros 2000 caracteres del HTML
print