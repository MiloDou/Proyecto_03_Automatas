# main.py
import os
from logic import procesar_regex

def Clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def Continue():
    input("\nPresiona ENTER para continuar...")
    Clear()

def main():
    Clear()
    while True:
        print("----------BIENVENIDO\n")
        print("  1. Ingresar expresión.")
        print("  2. Salir.\n")
        try:
            option = int(input("Ingresa una opción: "))
        except ValueError:
            print(" Opción inválida. Ingresa un número.")
            Continue()
            continue

        match option:
            case 1:
                Clear()
                print("----INGRESAR EXPRESIÓN\n")
                procesar_regex()
                Continue()
            case 2:
                print("\n----Adiós")
                break
            case _:
                print("⚠️ Opción no existe.")
                Continue()

if __name__ == "__main__":
    main()