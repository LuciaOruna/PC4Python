#ejercicio 3

import requests
import zipfile
from io import BytesIO

def descargar_imagen(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.content
    else:
        print("Error al descargar la imagen:", response.status_code)
        return None

def comprimir_zip(nombre_archivo, contenido):
    with zipfile.ZipFile(nombre_archivo, 'w') as zipf:
        zipf.writestr('imagen.jpg', contenido)

def descomprimir_zip(nombre_archivo):
    with zipfile.ZipFile(nombre_archivo, 'r') as zipf:
        zipf.extractall()

def main():
    # URL de la imagen a descargar
    url_imagen = "https://images.unsplash.com/photo-1546527868-ccb7ee7dfa6a?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"

    # Descargar la imagen desde la URL
    contenido_imagen = descargar_imagen(url_imagen)
    if contenido_imagen is not None:
        # Comprimir la imagen en un archivo zip
        nombre_zip = "imagen_zip.zip"
        comprimir_zip(nombre_zip, contenido_imagen)
        print("Imagen comprimida en el archivo:", nombre_zip)

        # Descomprimir el archivo zip
        print("Descomprimiendo archivo zip...")
        descomprimir_zip(nombre_zip)
        print("Archivo zip descomprimido")

if __name__ == "__main__":
    main()
