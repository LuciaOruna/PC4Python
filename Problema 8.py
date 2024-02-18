#ejercicio 8

import requests
import sqlite3
from datetime import datetime

def obtener_precio_bitcoin():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        if response.status_code == 200:
            datos = response.json()
            return datos["bpi"]
        else:
            print("Error al obtener el precio del Bitcoin:", response.status_code)
            return None
    except requests.RequestException as e:
        print("Error de solicitud:", e)
        return None

def obtener_tipo_cambio_sunat(fecha):
    try:
        url = "https://api.apis.net.pe/v1/tipo-cambio"
        parametros = {"fecha": fecha, "moneda": "PEN"}
        response = requests.get(url, params=parametros)
        if response.status_code == 200:
            datos = response.json()
            return datos["compra"]
        else:
            print("Error al obtener el tipo de cambio del PEN:", response.status_code)
            return None
    except requests.RequestException as e:
        print("Error de solicitud:", e)
        return None

def almacenar_datos_en_tabla(precio_bitcoin, tipo_cambio_pen):
    if precio_bitcoin and tipo_cambio_pen:
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        conexion = sqlite3.connect("base.db")
        cursor = conexion.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS bitcoin (
                            fecha TEXT PRIMARY KEY,
                            precio_usd REAL,
                            precio_gbp REAL,
                            precio_eur REAL,
                            precio_pen REAL
                        )''')
        cursor.execute('''INSERT INTO bitcoin (fecha, precio_usd, precio_gbp, precio_eur, precio_pen)
                            VALUES (?, ?, ?, ?, ?)''', (fecha, precio_bitcoin["USD"]["rate_float"],
                                                        precio_bitcoin["GBP"]["rate_float"],
                                                        precio_bitcoin["EUR"]["rate_float"],
                                                        precio_bitcoin["USD"]["rate_float"] * tipo_cambio_pen))
        conexion.commit()
        conexion.close()
    else:
        print("No se pueden almacenar datos vacíos.")

def calcular_precio_compra_10_bitcoins():
    conexion = sqlite3.connect("base.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT precio_pen, precio_eur FROM bitcoin ORDER BY fecha DESC LIMIT 1")
    fila = cursor.fetchone()
    if fila:
        precio_pen = fila[0]
        precio_eur = fila[1]
        precio_compra_10_bitcoins_pen = precio_pen * 10
        precio_compra_10_bitcoins_eur = precio_eur * 10
        print(f"Precio de comprar 10 bitcoins en PEN: {precio_compra_10_bitcoins_pen} PEN")
        print(f"Precio de comprar 10 bitcoins en EUR: {precio_compra_10_bitcoins_eur} EUR")
    else:
        print("No se encontraron datos en la tabla bitcoin.")
    conexion.close()

def main():
    precio_bitcoin = obtener_precio_bitcoin()
    if precio_bitcoin:
        tipo_cambio_pen = obtener_tipo_cambio_sunat(datetime.now().strftime("%Y-%m-%d"))
        if tipo_cambio_pen:
            almacenar_datos_en_tabla(precio_bitcoin, tipo_cambio_pen)
            calcular_precio_compra_10_bitcoins()

if __name__ == "__main__":
    main()
