#ejercicio 4

import requests

def obtener_precio_bitcoin():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()  # Levanta una excepción si la respuesta no es exitosa
        data = response.json()
        precio = data["bpi"]["USD"]["rate_float"]
        return precio
    except requests.RequestException as e:
        print("Error al obtener el precio de Bitcoin:", e)
        return None

def guardar_precio_en_archivo(precio, nombre_archivo="precios_bitcoin.txt"):
    with open(nombre_archivo, 'a') as archivo:
        archivo.write(str(precio) + '\n')

def main():
    precio_bitcoin = obtener_precio_bitcoin()

    if precio_bitcoin is not None:
        guardar_precio_en_archivo(precio_bitcoin)
        print("Precio de Bitcoin guardado en el archivo 'precios_bitcoin.txt'")
    else:
        print("No se pudo obtener el precio de Bitcoin. No se ha guardado nada en el archivo.")

if __name__ == "__main__":
    main()
