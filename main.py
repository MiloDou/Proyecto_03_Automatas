import re
import os

def Clear():
    os.system('cls' if os.name == 'nt' else 'clear')
def Continue():
    input("\n Presiona ENTER para continuar...")
    Clear()

def main():
    Clear()
    while True:
        print("----------BIENVENIDO\n")
        print("  1. Ingresar expresión.")
        print("  2. Salir.\n")
        option = int(input("Ingresa una opción: "))
        match option:
            case 1:
                Clear()
                print("----INGRESAR EXPRESIÓN\n")
                Continue()
            case 2:
                print("\n----Adiós")
                break
            case _:
                print("no existe")
                Continue()


if __name__ == "__main__":
    main()