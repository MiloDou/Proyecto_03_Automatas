# logic.py
import re

class Text:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'Texto: {self.value}'

def procesar_regex():
    print("=== Herramienta de búsqueda con regex ===")
    
    regex = input("Ingresa una expresión regular: ")
    texto = input("Ingresa el texto a analizar: ")
    
    try:
        coincidencias = re.findall(regex, texto)
        if coincidencias:
            print("\nCoincidencias encontradas:")
            for i, match in enumerate(coincidencias, 1):
                print(f"{i}. {match}")
        else:
            print("\nNo se encontraron coincidencias.")
    except re.error as e:
        print(f"\nError en la expresión regular: {e}")