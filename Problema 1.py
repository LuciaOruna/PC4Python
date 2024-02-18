#Ejecicio 1

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

def main():
    cantidad_bitcoins = float(input("Ingrese la cantidad de Bitcoins que posee: "))
    precio_bitcoin = obtener_precio_bitcoin()

    if precio_bitcoin is not None:
        costo_total = cantidad_bitcoins * precio_bitcoin
        print(f"El costo actual de {cantidad_bitcoins} Bitcoins en USD es: ${costo_total:,.4f}")
    else:
        print("No se pudo obtener el precio de Bitcoin. Por favor, inténtelo nuevamente.")

if __name__ == "__main__":
    main()




