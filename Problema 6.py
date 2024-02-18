#ejercicio 6

def contar_lineas_codigo(archivo):
    try:
        with open(archivo, 'r') as f:
            lineas = f.readlines()
            lineas_codigo = 0
            for linea in lineas:
                # Eliminar espacios en blanco al inicio y al final de la línea
                linea = linea.strip()
                # Excluir líneas en blanco y comentarios
                if linea and not linea.startswith("#"):
                    lineas_codigo += 1
            return lineas_codigo
    except FileNotFoundError:
        print(f"El archivo '{archivo}' no existe.")
        return None

def main():
    ruta_archivo = input("Ingrese la ruta del archivo .py: ")
    if not ruta_archivo.endswith(".py"):
        print("El archivo debe tener extensión .py")
    else:
        lineas_codigo = contar_lineas_codigo(ruta_archivo)
        if lineas_codigo is not None:
            print(f"El número de líneas de código en '{ruta_archivo}' es: {lineas_codigo}")

if __name__ == "__main__":
    main()
