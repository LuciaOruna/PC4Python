#Ejercicio 2
from pyfiglet import Figlet
import random

def obtener_fuente_aleatoria(fuentes):
    return random.choice(fuentes)

def main():
    # Crear una instancia de Figlet
    figlet = Figlet()

    # Obtener la lista de fuentes disponibles
    fuentes = figlet.getFonts()

    # Solicitar al usuario el nombre de la fuente o seleccionar una aleatoria si no se proporciona
    fuente = input("Ingrese el nombre de la fuente (deje en blanco para una selección aleatoria): ")
    if not fuente:
        fuente = obtener_fuente_aleatoria(fuentes)
        print(f"Se seleccionó aleatoriamente la fuente '{fuente}'")

    # Establecer la fuente seleccionada
    figlet.setFont(font=fuente)

    # Solicitar al usuario el texto
    texto = input("Ingrese el texto a imprimir: ")

    # Imprimir el texto utilizando la fuente seleccionada
    print(figlet.renderText(texto))

if __name__ == "__main__":
    main()
