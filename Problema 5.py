#ejercicio 5

def guardar_tabla_multiplicar(numero):
    nombre_archivo = f"tabla-{numero}.txt"
    with open(nombre_archivo, 'w') as archivo:
        for i in range(1, 11):
            archivo.write(f"{numero} x {i} = {numero*i}\n")

def mostrar_tabla_multiplicar(numero):
    nombre_archivo = f"tabla-{numero}.txt"
    try:
        with open(nombre_archivo, 'r') as archivo:
            print(f"Tabla de multiplicar de {numero}:")
            print(archivo.read())
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no existe.")

def mostrar_linea_tabla_multiplicar(numero, linea):
    nombre_archivo = f"tabla-{numero}.txt"
    try:
        with open(nombre_archivo, 'r') as archivo:
            lineas = archivo.readlines()
            if linea <= len(lineas):
                print(f"Línea {linea} de la tabla de multiplicar de {numero}:")
                print(lineas[linea-1].strip())
            else:
                print(f"La línea {linea} no existe en el archivo {nombre_archivo}.")
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no existe.")

def main():
    while True:
        print("1. Guardar tabla de multiplicar")
        print("2. Mostrar tabla de multiplicar")
        print("3. Mostrar línea de la tabla de multiplicar")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            numero = int(input("Ingrese un número entero entre 1 y 10: "))
            if 1 <= numero <= 10:
                guardar_tabla_multiplicar(numero)
            else:
                print("El número debe estar entre 1 y 10.")
        elif opcion == "2":
            numero = int(input("Ingrese un número entero entre 1 y 10: "))
            if 1 <= numero <= 10:
                mostrar_tabla_multiplicar(numero)
            else:
                print("El número debe estar entre 1 y 10.")
        elif opcion == "3":
            numero = int(input("Ingrese un número entero entre 1 y 10: "))
            linea = int(input("Ingrese el número de línea a mostrar: "))
            if 1 <= numero <= 10:
                mostrar_linea_tabla_multiplicar(numero, linea)
            else:
                print("El número debe estar entre 1 y 10.")
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
