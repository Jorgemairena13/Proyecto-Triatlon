from recursos.interfaz import *
from recursos.eventos import *
from recursos.atletas import *
from recursos.registros import *
from recursos.estadisticas import *
from os import system




def main():
    while True:
        system("cls")
        print(menu_principal)
        opcion = input("Selecciona una opción: ")
        if opcion == "5":
            
            break
        elif opcion == "1":
            while True:
                system("cls")
                print(menu_eventos)
                opcion = input("Selecciona una opción: ")
                if opcion == "4":
                    break
        elif opcion == "2":
            while True:
                system("cls")
                print(menu_atletas)
                opcion = input("Selecciona una opción: ")
                if opcion == "4":
                    break
        elif opcion == "3":
            while True:
                system("cls")
                print(menu_registros)
                opcion = input("Selecciona una opción: ")
                if opcion == "6":
                    break
        elif opcion == "4":
            while True:
                system("cls")
                print(menu_estadisticas)
                opcion = input("Selecciona una opción: ")
                if opcion == "3":
                    break

if __name__ == "__main__":
    main()
