from recursos.interfaz import *
from recursos.eventos import *
from recursos.registros import *
from recursos.estadisticas import *
from os import system
consele = Console()

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
                    lugar = prompt('Introduce el lugar del evento: ')
                    distancia = prompt('Introduce la distacion total del evento: ')
                    triatlon.agregar_evento(id_evento, nombre, fecha, lugar, distancia)

                elif opcion == '2':
                    evento = int(prompt('ID del evento a editar: '))
                    nombre = prompt('Introduce el nombre del evento: ')
                    fecha = prompt('Introduce la fecha del evento [DIA-MES-AÑO]')
                    lugar = prompt('Introduce el lugar del evento: ')
                    distancia = prompt('Introduce la distacion total del evento: ')
                    triatlon.editar_evento(evento, nombre, fecha, lugar, distancia)
                    
                    
                elif opcion == '3':
                    triatlon.mostrar_eventos()
                    prompt()
                elif opcion == "4":
                    break

       
        
           
        elif opcion == "2":
            while True:
                system("cls")
                print(menu_atletas)
                opcion = prompt("Selecciona una opción: ")
                if opcion == '1':
                    print('Registrar atleta')
                    # Pedir datos del atleta
                    evento = int(prompt('ID del evento al que se inscribe: '))
                    dni = prompt('Introduce el dni del atleta: ')
                    nombre = prompt('Introduce el nombre del atleta: ').capitalize()
                    apellido = prompt('Introduce el apellido del atleta: ').capitalize()
                    fecha_nacimiento = prompt('Introduce la fecha de nacimiento del atleta [DIA-MES-AÑO]: ')
                    genero = prompt('Introduce el genero del atleta [M/F]').upper()
                    
                    # Agregamos el participante con el metodo
                    triatlon.agregar_participante(dni,nombre,apellido,fecha_nacimiento,genero,evento)
                    prompt()
                elif opcion == '2':
                    console.print('Buscar atleta')
                    triatlon.buscar_atleta()

                elif opcion == '3':
                    console.print('Editar atleta')
                    triatlon.editar_atleta()        
                elif opcion == "4":
                    break
        elif opcion == "3":
            while True:
                system("cls")
                print(menu_registros)
                opcion = prompt("Selecciona una opción: ")
                if opcion == "1":
                    triatlon.registrar_tiempo_natacion()

                elif opcion == "2":
                    triatlon.registrar_tiempo_ciclismo()

                elif opcion == "3":
                    triatlon.registrar_tiempo_carrera()

                elif opcion == "4":
                    triatlon.calcular_tiempo_total()

                elif opcion == "5":
                    break
        elif opcion == "4":
            while True:
                system("cls")
                print(menu_estadisticas)
                opcion = prompt("Selecciona una opción: ")
                if opcion == "3":
                    break

        elif opcion == "5":
            break


if __name__ == "__main__":
    main()
