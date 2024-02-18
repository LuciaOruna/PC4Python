#ejercicio 7

import requests
import sqlite3

def obtener_datos_tipo_cambio():
    # URL del API de SUNAT para obtener el tipo de cambio del dólar
    url = "https://api.apis.net.pe/v1/tipo-cambio-mensual"

    # Parámetros de la solicitud
    parametros = {
        "anio": 2023,
        "moneda": "USD"
    }

    # Realizar la solicitud HTTP
    response = requests.get(url, params=parametros)

    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        # Convertir la respuesta a JSON
        datos = response.json()
        return datos
    else:
        print("Error al obtener los datos del tipo de cambio:", response.status_code)
        return None

def almacenar_datos_en_base_de_datos(datos):
    if datos:
        # Conectar a la base de datos SQLite
        conexion = sqlite3.connect("base.db")
        cursor = conexion.cursor()

        # Crear la tabla 'sunat_info' si no existe
        cursor.execute('''CREATE TABLE IF NOT EXISTS sunat_info (
                            fecha TEXT PRIMARY KEY,
                            compra REAL,
                            venta REAL
                        )''')

        # Insertar los datos en la tabla
        for dato in datos:
            cursor.execute('''INSERT INTO sunat_info (fecha, compra, venta)
                                VALUES (?, ?, ?)''', (dato['fecha'], dato['compra'], dato['venta']))
        
        # Confirmar los cambios y cerrar la conexión
        conexion.commit()
        conexion.close()
    else:
        print("No se pueden almacenar datos vacíos.")

def mostrar_contenido_tabla():
    # Conectar a la base de datos SQLite
    conexion = sqlite3.connect("base.db")
    cursor = conexion.cursor()

    # Consultar todos los registros en la tabla 'sunat_info'
    cursor.execute("SELECT * FROM sunat_info")
    filas = cursor.fetchall()

    # Mostrar los resultados
    for fila in filas:
        print(f"Fecha: {fila[0]}, Compra: {fila[1]}, Venta: {fila[2]}")

    # Cerrar la conexión
    conexion.close()

def main():
    # Obtener los datos del tipo de cambio del API de SUNAT
    datos_tipo_cambio = obtener_datos_tipo_cambio()

    # Almacenar los datos en la base de datos
    if datos_tipo_cambio:
        almacenar_datos_en_base_de_datos(datos_tipo_cambio)

    # Mostrar el contenido de la tabla
    mostrar_contenido_tabla()

if __name__ == "__main__":
    main()
