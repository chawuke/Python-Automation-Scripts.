import requests
from bs4 import BeautifulSoup

def obtener_titulares(url):
    print(f"Extrayendo datos de: {url}...")
    try:
        # Simulamos un navegador para que no nos bloqueen
        headers = {'User-Agent': 'Mozilla/5.0'}
        respuesta = requests.get(url, headers=headers)
        
        soup = BeautifulSoup(respuesta.text, 'html.parser')
        
        # Busca todos los titulares (h3 es común en noticias)
        titulares = soup.find_all('h3')
        
        print("\n--- TITULARES ENCONTRADOS ---")
        for i, t in enumerate(titulares[:10], 1): # Solo los primeros 10
            print(f"{i}. {t.get_text().strip()}")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Ejemplo con un sitio de noticias tecnológicas
    obtener_titulares("https://news.ycombinator.com/")
