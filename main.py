from recursos.interfaz import *
from recursos.eventos import *
from recursos.registros import *
from recursos.estadisticas import *
from os import system


triatlon = Triatlon()

def main():
    while True:
        system("cls")
        print(menu_principal)
        opcion = prompt("Selecciona una opción: ")
        # Añádir evento
        if opcion == '1':
             while True:
                system("cls")
                print(menu_eventos)
                opcion = prompt("Selecciona una opción: ")
                if opcion == '1':
                    id_evento = len(triatlon.eventos) + 1 
                    print(id_evento)
                    nombre = prompt('Introduce el nombre del evento: ')
                    fecha = prompt('Introduce la fecha del evento [DIA-MES-AÑO]')
                    lugar = prompt()
                    distancia= prompt()
                    triatlon.agregar_evento(id_evento, nombre, fecha, lugar, distancia)

                elif opcion == '2':
                    pass
                elif opcion == '3':
                    triatlon.mostrar_eventos()
                    prompt()
                elif opcion == "4":
                    break
                
                
            
            
        elif opcion == "5":
            break
        
           
        elif opcion == "2":
            while True:
                system("cls")
                print(menu_atletas)
                opcion = prompt("Selecciona una opción: ")
                if opcion == '1':
                    print('Registrar atleta')
                     #nombre, apellido, fecha_nacimiento, genero
                    nombre = prompt('Introduce el nombre del atleta: ').capitalize()
                    apellido = prompt('Introduce el apellido del atleta: ').capitalize()
                    fecha_nacimiento = prompt('Introduce la fecha de nacimiento del atleta [DIA-MES-AÑO]: ')
                    genero = prompt('Introduce el genero del atleta [M/F]').upper()
                    nuevo_atleta = Atleta(nombre,apellido,fecha_nacimiento,genero)
                    evento = prompt('A que evento se inscribe?')
                    prompt()
                if opcion == "4":
                    break
        elif opcion == "3":
            while True:
                system("cls")
                print(menu_registros)
                opcion = prompt("Selecciona una opción: ")
                if opcion == "6":
                    break
        elif opcion == "4":
            while True:
                system("cls")
                print(menu_estadisticas)
                opcion = prompt("Selecciona una opción: ")
                if opcion == "3":
                    break


if __name__ == "__main__":
    main()
