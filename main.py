from recursos.interfaz import *
from recursos.eventos import *
from recursos.registros import *
from recursos.estadisticas import *
from os import system
from datetime import timedelta

console = Console()

triatlon = Triatlon()

triatlon.agregar_evento(1, "Triatlon Barcelona", "2025-05-15", "Barcelona", "51.5 km")
triatlon.agregar_evento(2, "Triatlon Madrid", "2025-06-20", "Madrid", "32.0 km")
triatlon.agregar_evento(3, "Triatlon Valencia", "2025-07-10", "Valencia", "25.7 km")

# Agregar participantes a los eventos para pruebas

# Participantes para el evento 1 (Barcelona)
triatlon.agregar_participante("20", "Juan", "García", "1990-03-15", "M", 1)
triatlon.agregar_participante("23456789B", "María", "López", "1992-07-22", "F", 1)
triatlon.agregar_participante("34567890C", "Carlos", "Martínez", "1988-11-05", "M", 1)

# Participantes para el evento 2 (Madrid)
triatlon.agregar_participante("45678901D", "Laura", "Sánchez", "1995-02-18", "F", 2)
triatlon.agregar_participante("56789012E", "Pedro", "Fernández", "1993-09-30", "M", 2)

# Participantes para el evento 3 (Valencia)
triatlon.agregar_participante("67890123F", "Ana", "Rodríguez", "1991-04-12", "F", 3)
triatlon.agregar_participante("78901234G", "David", "González", "1989-08-25", "M", 3)
triatlon.agregar_participante("89012345H", "Elena", "Pérez", "1994-06-07", "F", 3)

def main():
    while True:
        system("cls")
        print(menu_alineado)
        opcion = prompt("Selecciona una opción: ")
        # Añádir evento
        if opcion == '1':
             while True:
                system("cls")
                console.print(menu_eventos_alineado)
                opcion = prompt("Selecciona una opción: ")
                if opcion == '1':
                    id_evento = len(triatlon.eventos) + 1 
                    console.print(id_evento)
                    nombre = prompt('Introduce el nombre del evento: ')
                    fecha = prompt('Introduce la fecha del evento [DIA-MES-AÑO]')
                    lugar = prompt('Introduce el lugar del evento: ')
                    distancia = prompt('Introduce la distacion total del evento: ')
                    triatlon.agregar_evento(id_evento, nombre, fecha, lugar, distancia)
                    console.input('Evento creado correctamente')
                    
                elif opcion == '2':
                    evento = int(prompt('ID del evento a editar: '))
                    nombre = prompt('Introduce el nombre del evento: ')
                    fecha = prompt('Introduce la fecha del evento [DIA-MES-AÑO]')
                    lugar = prompt('Introduce el lugar del evento: ')
                    distancia = prompt('Introduce la distacion total del evento: ')
                    triatlon.editar_evento(evento, nombre, fecha, lugar, distancia)
                    prompt()
                    
                elif opcion == '3':
                    triatlon.mostrar_eventos()
                    prompt()
                elif opcion == "4":
                    break

    
        elif opcion == "2":
            while True:
                system("cls")
                console.print(menu_atletas_alineado)
                opcion = prompt("Selecciona una opción: ")
                if opcion == '1':
                    
                    # Pedir datos del atleta
                    completar = list(map(str, triatlon.eventos.keys())) # Usamos la fucnion map para pasar a str y que se pueda usar el auto completado
                    ids = FuzzyWordCompleter(completar)
                    id_evento = int(prompt('ID del evento al que se inscribe: ',completer=ids))
                    dni = prompt('Introduce el dni del atleta: ')
                    nombre = prompt('Introduce el nombre del atleta: ').capitalize()
                    apellido = prompt('Introduce el apellido del atleta: ').capitalize()
                    fecha_nacimiento = prompt('Introduce la fecha de nacimiento del atleta [DIA-MES-AÑO]: ')
                    genero = prompt('Introduce el genero del atleta [M/F]').upper()
                    
                    # Agregamos el participante con el metodo
                    triatlon.agregar_participante(dni,nombre,apellido,fecha_nacimiento,genero,id_evento)
                    prompt()
                elif opcion == '2':
                    id_evento = int(prompt('Introduce el id del evento donde participa: '))
                    dni = prompt('Introduce el dni del atleta a buscar: ')
                    
                    triatlon.buscar_atleta(id_evento,dni)
                    prompt()
                elif opcion == '3':

                    console.print('Editar atleta')
                    # Pedimos los datos para editar el atleta
                    completar = list(map(str, triatlon.eventos.keys())) # Usamos la fucnion map para pasar a str y que se pueda usar el auto completado
                    # Auto completado para que sea mas facil la interactividad
                    ids = FuzzyWordCompleter(completar)
                    id_evento = int(prompt('Introduce el evento al que pertenece el atleta: ',completer = ids))
                    eventos = FuzzyWordCompleter(triatlon.eventos[id_evento].participantes.keys())
                    dni = prompt('Introduce el dni del aleta a editar:  ',completer = eventos)
                    nombre = prompt('Introduce el nombre: ')
                    apellido = prompt('Introduce el apellido: ')
                    fecha_nacimiento = prompt('Introduce la fecha de nacimiento: ')
                    genero = prompt('Introduce el genero [M/F]: ')
                    triatlon.editar_atleta(id_evento,dni,nombre,apellido,fecha_nacimiento,genero) 
                    prompt()

                elif opcion == "4":
                    break

        elif opcion == "3":

            while True:
                system("cls")
                console.print(menu_registros_alineado)
                opcion = prompt("Selecciona una opción: ")
                if opcion == "1":
                    id_evento = int(prompt('Introduce el evento al que pertenece el atleta: '))
                    dni = prompt('Introduce el dni del aleta:  ')
                    tiempo = input("Introduce el tiempo en formato hh:mm:ss (por ejemplo, 1:35:42): ")
                    horas, minutos, segundos = map(int, tiempo.split(":"))
                    tiempo_natacion = timedelta(hours=horas, minutes=minutos, seconds=segundos)
                    triatlon.registrar_tiempo_natacion(id_evento,dni,tiempo_natacion)

                elif opcion == "2":
                    id_evento = int(prompt('Introduce el evento al que pertenece el atleta: '))
                    dni = prompt('Introduce el dni del aleta :  ')
                    tiempo = input("Introduce el tiempo en formato hh:mm:ss (por ejemplo, 1:35:42): ")
                    horas, minutos, segundos = map(int, tiempo.split(":"))
                    tiempo_ciclismo = timedelta(hours=horas, minutes=minutos, seconds=segundos)
                    triatlon.registrar_tiempo_ciclismo(id_evento,dni,tiempo_ciclismo)

                elif opcion == "3":
                    # Pedimos los datos para registrar el tiempo de la carrera
                    id_evento = int(prompt('Introduce el evento al que pertenece el atleta: '))
                    dni = prompt('Introduce el dni del aleta:  ')
                    tiempo = input("Introduce el tiempo en formato hh:mm:ss (por ejemplo, 1:35:42): ")
                    horas, minutos, segundos = map(int, tiempo.split(":"))
                    tiempo_carrera = timedelta(hours=horas, minutes=minutos, seconds=segundos)
                    triatlon.registrar_tiempo_carrera(id_evento,dni,tiempo_carrera)

                elif opcion == "4":
                    # Pedimos los datos y luego usamos la funcion para que muestre el tiempo total del atleta
                    id_evento = int(prompt('Introduce el evento al que pertenece el atleta: '))
                    dni = prompt('Introduce el dni del aleta:  ')
                    triatlon.calcular_tiempo_total(id_evento,dni)
                    prompt()

                elif opcion == "5":
                    break
        elif opcion == "4":
            while True:
                system("cls")
                console.print(menu_estadisticas_alineado)
                opcion = prompt("Selecciona una opción: ")
                if opcion == "1":
                    pass
                elif opcion == "2":
                    break
                elif opcion == "3":
                    break

        elif opcion == "5":
            break


if __name__ == "__main__":
    main()
