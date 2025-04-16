from recursos.interfaz import *
from recursos.eventos import *
from recursos.registros import *
from recursos.estadisticas import *

from os import system
from datetime import timedelta
style = Style.from_dict({
    'prompt': 'bold fg:#ffb027',
    '': 'fg:#ffffff'
})

console = Console()

triatlon = Triatlon()

def completar_ids():
    completar = list(map(str, triatlon.eventos.keys()))
    ids = FuzzyWordCompleter(completar)
    return ids

triatlon.agregar_evento(1, "Triatlon Barcelona", "2025-05-15", "Barcelona", "51.5 km")
triatlon.agregar_evento(2, "Triatlon Madrid", "2025-06-20", "Madrid", "32.0 km")
triatlon.agregar_evento(3, "Triatlon Valencia", "2025-07-10", "Valencia", "25.7 km")

# Agregar participantes a los eventos para pruebas

# Participantes para el evento 1 (Barcelona)
triatlon.agregar_participante("20", "Juan", "García", "1990-03-15", "M", 1)
triatlon.agregar_participante("23456789B", "María", "López", "1992-07-22", "F", 1)
triatlon.agregar_participante("4", "Pepe", "Martínez", "1988-11-05", "M", 1)
triatlon.agregar_participante("787", "Luis", "Martínez", "1988-11-05", "M", 1)
triatlon.agregar_participante("53151", "Carlos", "Martínez", "1988-11-05", "M", 1)

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
        opcion = prompt("Selecciona una opción: ",style=style)
        # Añádir evento
        if opcion == '1':
             while True:
                system("cls")
                console.print(menu_eventos_alineado)
                opcion = prompt("Selecciona una opción: ",style=style)
                if opcion == '1':
                    id_evento = len(triatlon.eventos) + 1 
                    console.print(id_evento)
                    nombre = prompt('Introduce el nombre del evento: ',style=style)
                    fecha = prompt('Introduce la fecha del evento [DIA-MES-AÑO]: ',style=style)
                    lugar = prompt('Introduce el lugar del evento: ',style=style)
                    distancia = prompt('Introduce la distacion total del evento: ',style=style)
                    triatlon.agregar_evento(id_evento, nombre, fecha, lugar, distancia)
                    prompt('Evento creado correctamente')
                    
                elif opcion == '2':
                    evento = int(prompt('ID del evento a editar: ',style=style,completer = completar_ids()))
                    nombre = prompt('Introduce el nombre del evento: ',style=style)
                    fecha = prompt('Introduce la fecha del evento [DIA-MES-AÑO]',style=style)
                    lugar = prompt('Introduce el lugar del evento: ', style=style)
                    distancia = prompt('Introduce la distacion total del evento: ',style=style)
                    triatlon.editar_evento(evento, nombre, fecha, lugar, distancia)
                    prompt(style=style)
                    
                elif opcion == '3':
                    triatlon.mostrar_eventos()
                    prompt(style=style)
                elif opcion == "4":
                    break

    
        elif opcion == "2":
            while True:
                system("cls")
                console.print(menu_atletas_alineado)
                opcion = prompt("Selecciona una opción: ",style=style)
                if opcion == '1':
                    
                    # Pedir datos del atleta
                    id_evento = int(prompt('ID del evento al que se inscribe: ',completer = completar_ids,style=style))
                    dni = prompt('Introduce el dni del atleta: ',style=style)
                    nombre = prompt('Introduce el nombre del atleta: ',style=style).capitalize()
                    apellido = prompt('Introduce el apellido del atleta: ',style=style).capitalize()
                    fecha_nacimiento = prompt('Introduce la fecha de nacimiento del atleta [DIA-MES-AÑO]: ',style=style)
                    genero = prompt('Introduce el genero del atleta [M/F]',style=style).upper()
                    
                    # Agregamos el participante con el metodo
                    triatlon.agregar_participante(dni,nombre,apellido,fecha_nacimiento,genero,id_evento)
                    prompt(style=style)
                elif opcion == '2':
                    id_evento = int(prompt('Introduce el id del evento donde participa: ',style=style,completer = completar_ids()))
                    dni = prompt('Introduce el dni del atleta a buscar: ',style=style)
                    
                    triatlon.buscar_atleta(id_evento,dni)
                    prompt(style=style)
                elif opcion == '3':

                    console.print('Editar atleta')

                    id_evento = int(prompt('Introduce el evento al que pertenece el atleta: ',completer = completar_ids(),style=style))
                    eventos = FuzzyWordCompleter(triatlon.eventos[id_evento].participantes.keys())
                    dni = prompt('Introduce el dni del aleta a editar:  ',completer = eventos,style=style)
                    nombre = prompt('Introduce el nombre: ',style=style)
                    apellido = prompt('Introduce el apellido: ',style=style)
                    fecha_nacimiento = prompt('Introduce la fecha de nacimiento: ',style=style)
                    genero = prompt('Introduce el genero [M/F]: ',style=style)
                    triatlon.editar_atleta(id_evento,dni,nombre,apellido,fecha_nacimiento,genero) 
                    prompt(style=style)

                elif opcion == "4":
                    break

        elif opcion == "3":

            while True:
                system("cls")
                console.print(menu_registros_alineado)
                opcion = prompt("Selecciona una opción: ",style=style)
                if opcion == "1":
                    
                    id_evento = int(prompt('Introduce el evento al que pertenece el atleta: ',completer = completar_ids(),style=style))
                    dni = prompt('Introduce el dni del aleta:  ',style=style)
                    tiempo = prompt("Introduce el tiempo en formato hh:mm:ss (por ejemplo, 1:35:42): ")
                    horas, minutos, segundos = map(int, tiempo.split(":"))
                    tiempo_natacion = timedelta(hours=horas, minutes=minutos, seconds=segundos)
                    triatlon.registrar_tiempo_natacion(id_evento,dni,tiempo_natacion)

                elif opcion == "2":
                    id_evento = int(prompt('Introduce el evento al que pertenece el atleta: ',style=style,completer = completar_ids()))
                    dni = prompt('Introduce el dni del aleta : ',style=style)
                    tiempo = prompt("Introduce el tiempo en formato hh:mm:ss (por ejemplo, 1:35:42): ",style=style)
                    horas, minutos, segundos = map(int, tiempo.split(":"))
                    tiempo_ciclismo = timedelta(hours=horas, minutes=minutos, seconds=segundos)
                    triatlon.registrar_tiempo_ciclismo(id_evento,dni,tiempo_ciclismo)

                elif opcion == "3":
                    # Pedimos los datos para registrar el tiempo de la carrera
                    id_evento = int(prompt('Introduce el evento al que pertenece el atleta: ',style=style,completer = completar_ids()))
                    dni = prompt('Introduce el dni del aleta:  ')
                    tiempo = prompt("Introduce el tiempo en formato hh:mm:ss (por ejemplo, 1:35:42): ",style=style)
                    horas, minutos, segundos = map(int, tiempo.split(":"))
                    tiempo_carrera = timedelta(hours=horas, minutes=minutos, seconds=segundos)
                    triatlon.registrar_tiempo_carrera(id_evento,dni,tiempo_carrera)

                elif opcion == "4":
                    # Pedimos los datos y luego usamos la funcion para que muestre el tiempo total del atleta
                    id_evento = int(prompt('Introduce el evento al que pertenece el atleta: ',style=style,completer = completar_ids()))
                    dni = prompt('Introduce el dni del aleta:  ',style=style)
                    console.print(triatlon.calcular_tiempo_total(id_evento,dni))
                    prompt(style=style)

                elif opcion == "5":
                    break
        elif opcion == "4":
            while True:
                system("cls")
                console.print(menu_estadisticas_alineado)
                opcion = prompt("Selecciona una opción: ",style=style)
                if opcion == "1":
                    triatlon.clasificacion_general()
                    prompt(style=style)
                elif opcion == "2":
                    categorias = FuzzyWordCompleter(['Natacion','Ciclismo','Carrera'])
                    categoria = prompt('De que categoria quieres mostrar los tiempos: ',completer = categorias).lower()
                    triatlon.clasificacion_categoria(categoria)
                    prompt(style=style)
                elif opcion == "3":
                    break

        elif opcion == "5":
            break


if __name__ == "__main__":
    main()
