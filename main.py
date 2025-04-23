from recursos.interfaz import *
from recursos.eventos import *


from os import system
from datetime import timedelta
style = Style.from_dict({
    'prompt': 'bold fg:#ffb027',
    '': 'fg:#ffffff'
})

console = Console()

triatlon = Triatlon()

# Fuciones que vamos a usar en ese programa
def completar_ids():
    '''
    Devuelve unos ids para que la funcion de complear funcione
    '''
    completar = list(map(str, triatlon.eventos.keys()))
    ids = FuzzyWordCompleter(completar)
    return ids

def completar_dni(id_evento):
    '''
    Devuelve unos participantes para que la funcion de complear funcione
    '''
    eventos = FuzzyWordCompleter(triatlon.eventos[id_evento].participantes.keys())
    return eventos

def validar_campo_vacio(campo_validar):
    '''
    Valida que el campo que se le pasa no este vacio
    '''
    if str(campo_validar).strip() == '':
        console.print(Panel('[bold #C70039]No se pueden introducir datos vacios!![/]',border_style='bold #C70039',width = 30))
        return False
    else:
        return True
    
def validar_dni(dni):
    '''
    Valida el dni con formato de 9 los 8 primeros digitos y el ultimo que sea una letra
    '''
    if len(dni) == 9 and dni[:8].isdigit() and dni[8].isalpha():
        return True
    else:
        console.print(Panel('[bold #C70039]El formato del dni no es valido!! [12345678A][/]',border_style='bold #C70039',width = 30))
        return False

def validar_solo_letras(campo_validar):
    '''
    Valida que el campo que se le pase solo sea numerico
    '''
    campo_validar = campo_validar.replace(" ", "")
    if campo_validar.isalpha():
        return True
    else:
        console.print(Panel('[bold #C70039]Solo se pueden introducir letras!![/]',border_style='bold #C70039',width = 30))
        return False


# Le decimos al usuario si quiere datos de muestra
opcion_datos = prompt('Quieres datos falsos para ver ejemplos? [S|N]: ',style=style).upper()
prompt('Poner en pantalla completa para mejor visualizacion',style=style)

if opcion_datos == 'S':
    # Agregamos 3 eventos
    triatlon.agregar_evento(1, "Triatlon Barcelona", "2025-05-15", "Barcelona", "51.5")
    triatlon.agregar_evento(2, "Triatlon Madrid", "2025-06-20", "Madrid", "32.0")
    triatlon.agregar_evento(3, "Triatlon Valencia", "2025-07-10", "Valencia", "25.7")

    # Agregar participantes a los eventos para pruebas

    # Participantes para el evento 1 Barcelona
    triatlon.agregar_participante("12345672G", "Juan", "García", "1990-03-15", "M", 1)
    triatlon.agregar_participante("23456789B", "María", "López", "1992-07-22", "F", 1)
    triatlon.agregar_participante("56789012E", "Pepe", "Martínez", "1988-11-05", "M", 1)
    triatlon.agregar_participante("56782012E", "Luis", "Martínez", "1988-11-05", "M", 1)
    triatlon.agregar_participante("56789092E", "Carlos", "Martínez", "1988-11-05", "M", 1)

    # Participantes para el evento 2 Madrid
    triatlon.agregar_participante("45678901D", "Laura", "Sánchez", "1995-02-18", "F", 2)
    triatlon.agregar_participante("76789012E", "Pedro", "Fernández", "1993-09-30", "M", 2)

    # Participantes para el evento 3 Valencia
    triatlon.agregar_participante("67890123F", "Ana", "Rodríguez", "1991-04-12", "F", 3)
    triatlon.agregar_participante("78901234G", "David", "González", "1989-08-25", "M", 3)
    triatlon.agregar_participante("89012345H", "Elena", "Pérez", "1994-06-07", "F", 3)


system('cls')    
logo_centrado = centrar_menu(logo)
console.print(logo_centrado)

def main():
    while True:
        console.print(menu_alineado)
        opcion = prompt("Selecciona una opción: ",style=style)
        system("cls")
        # Menu de eventos
        if opcion == '1':
             while True:
                system("cls")

                console.print(menu_eventos_alineado)
                opcion = prompt("Selecciona una opción: ",style=style)
                if opcion == '1':
                    id_evento = len(triatlon.eventos) + 1 
                    console.print(id_evento)
                    while True:
                        # Pedimos el nombre
                        nombre = prompt('Introduce el nombre del evento: ',style=style)
                        # Validamos el campo
                        
                        if  validar_campo_vacio(nombre) and validar_solo_letras(nombre):
                            break
                        else:
                            continue
                    
                    # Validamos la fecha con el formato correcto
                    while True:
                        try:
                            fecha = prompt('Introduce la fecha de nacimiento [dd-mm-aa]: ', style=style)
                            # Combrobamos que este vacia por si no quiere editar los datos
                            datetime.strptime(fecha, '%d-%m-%Y')
                            break
                        except:
                            console.print("[bold red]Fecha inválida[/]")
                            continue
                        
                    # Validamos el lugar 
                    while True:
                        lugar = prompt('Introduce el lugar del evento: ', style=style)
                        if validar_campo_vacio(lugar) and validar_solo_letras(lugar):
                            break
                        else:
                            continue
                    # Validamos la distancia
                    while True:
                        distancia = prompt('Introduce la distancia total del evento: ', style=style)
                        if validar_campo_vacio(distancia):
                            break
                        else:
                            continue
                    
                    # Agregamos el evento con el metodo correspondiente
                    triatlon.agregar_evento(id_evento, nombre, fecha, lugar, distancia)
                    prompt('Evento creado correctamente',style=style)
                    
                elif opcion == '2':
                    while True:
                        try:
                            evento = int(prompt('ID del evento a editar: ',style=style,completer = completar_ids()))
                            break
                                
                        except:
                            console.print(Panel('[bold #C70039]No se puede introducir otra cosa que no sea un numero!![/]',border_style='bold #C70039',width = 30))
                            continue
                        
                    while True:
                        nombre = prompt('Introduce el nombre del evento: ', style=style)
                        if validar_campo_vacio(nombre) and validar_solo_letras(nombre):
                            break
                        else:
                            continue

                    #Vvalidar la fecha con el formato correcto
                    while True:
                        
                        try:
                            fecha_nacimiento = prompt('Introduce la fecha de nacimiento [dd-mm-aa]: ', style=style)
                            # Combrobamos que este vacia por si no quiere editar los datos
                            
                            datetime.strptime(fecha_nacimiento, '%d-%m-%Y')
                            break
                        except:
                            console.print("[bold #C70039]Fecha inválida[/]")
                            continue

                    # Pedir y validar el lugar
                    while True:
                        lugar = prompt('Introduce el lugar del evento: ', style=style)
                        if validar_campo_vacio(lugar) and validar_solo_letras(lugar):
                            if lugar.isalpha():
                                break
                            else:
                                console.print("[bold red]Solo se pueden introducir fechas[/]")
                        else:
                            continue

                    # Pedir y validar la distancia
                    while True:
                        distancia = prompt('Introduce la distancia total del evento: ', style=style)
                        if validar_campo_vacio(distancia):
                            break
                        else:
                            continue
                    triatlon.editar_evento(evento, nombre, fecha_nacimiento, lugar, distancia)
                    prompt(style=style)
                    
                elif opcion == '3':
                    triatlon.mostrar_eventos()
                    prompt(style=style)

                elif opcion == '4':
                    while True:
                        try:
                            id_evento = int(prompt('ID del evento que se quiere borrar: ',completer = completar_ids(),style=style))
                            triatlon.eliminar_evento(id_evento)
                            break

                        except:
                            console.print(Panel("[bold #C70039]Introduce un numero!![/]",border_style='bold #C70039',width=30))
                            continue

                    prompt()
                elif opcion == "5":
                    break

        # Menu de atletas
        elif opcion == "2":
            while True:
                system("cls")
                console.print(menu_atletas_alineado)
                opcion = prompt("Selecciona una opción: ",style=style)
                if opcion == '1':
                    
                    # Pedir datos del atleta
                    while True:
                        try:
                            id_evento = int(prompt('ID del evento al que se inscribe: ',completer = completar_ids(),style=style))
                            break

                        except:
                            console.print(Panel("[bold #C70039]Introduce un numero!![/]",border_style='bold #C70039',width=30))
                            continue

                    while True:
                        dni = prompt('Introduce el dni del atleta: ', style=style)
                        if validar_campo_vacio(dni) and validar_dni(dni):
                            break 
                        else:
                            continue

                    while True:
                        nombre = prompt('Introduce el nombre del atleta: ', style=style).capitalize()
                        if validar_campo_vacio(nombre) and validar_solo_letras(nombre):
                            break
                        else:
                            continue

                    while True:
                        apellido = prompt('Introduce el apellido del atleta: ', style=style).capitalize()
                        if validar_campo_vacio(apellido) and validar_solo_letras(apellido):
                            break
                        else:
                            continue

                    while True:
                        
                        try:
                            fecha_nacimiento = prompt('Introduce la fecha de nacimiento [dd-mm-aa]: ', style=style)
                            # Combrobamos que este vacia por si no quiere editar los datos
                            
                            datetime.strptime(fecha_nacimiento, '%d-%m-%Y')
                            break
                        except:
                            console.print("[bold red]Fecha inválida[/]")
                            continue
                        

                    while True:
                        genero = prompt('Introduce el genero del atleta [M/F]: ', style=style).upper()
                        if validar_campo_vacio(genero) and genero in ['M', 'F']:
                            break
                        else:
                            console.print('[bold #C70039]Por favor, introduce M o F para el género.[/]')
                            continue

                    
                    # Agregamos el participante con el metodo
                    triatlon.agregar_participante(dni,nombre,apellido,fecha_nacimiento,genero,id_evento)
                    prompt(style=style)

                elif opcion == '2':
                    # Validar id sin errores
                    while True:
                        try:
                            id_evento = int(prompt('ID del evento al que pertenece: ',completer = completar_ids(),style=style))
                            break

                        except:
                            console.print(Panel("[bold #C70039]Introduce un numero!![/]",border_style='bold #C70039',width=30))
                            continue
                    while True:
                        dni = prompt('Introduce el dni del atleta a buscar: ', style=style)
                        if validar_campo_vacio(dni) and validar_dni(dni):
                            break
                        else:
                            continue
                    # Metodo para buscar un atleta
                    triatlon.buscar_atleta(id_evento,dni)
                    prompt(style=style)
                    
                elif opcion == '3':

                    console.print(Panel('[bold #f8ff26] Editar atributos del atleta[/]',border_style='bold #f8ff26'))
                    console.print(Panel('[bold blink #f8ff26]Recuerda si no quieres cambiar algun campo deja el campo vacio[/]',border_style='bold #f8ff26'))
                    # Validar el id para que no de error
                    while True:
                        try:
                            id_evento = int(prompt('ID del evento al que pertenece: ',completer = completar_ids(),style=style))
                            break

                        except:
                            console.print(Panel("[bold #C70039]Introduce un numero!![/]",border_style='bold #C70039',width=30))
                            continue
                    
                    # Validamos el dni sin que que este vacio y con su formato correcto
                    while True:
                        dni = prompt('Introduce el dni del aleta a editar:  ',completer  = completar_dni(id_evento),style=style)
                        if validar_campo_vacio(dni) and validar_dni(dni):
                            break
                        else:
                            continue    

                    # Validar nombre 
                    while True:
                        nombre = prompt('Introduce el nombre: ', style=style).capitalize().strip()
                        if nombre == "" or  validar_solo_letras(nombre) :
                            break
                        else:
                            continue

                    # Validar apellido sin espacios vacios
                    while True:
                        apellido = prompt('Introduce el apellido: ', style=style).capitalize()                        
                        if apellido == "" or  validar_solo_letras(apellido):
                            break
                        else:
                            continue

                    # Validar fecha de nacimiento con un formato correcto
                    while True:
                        try:
                            fecha_nacimiento = prompt('Introduce la fecha de nacimiento [dd-mm-aa]: ', style=style)
                            # Combrobamos que este vacia por si no quiere editar los datos
                            if fecha_nacimiento == "":
                                break
                            datetime.strptime(fecha_nacimiento, '%d-%m-%Y')
                            break
                        except:
                            console.print("[bold red]Fecha inválida[/]")
                            continue
                            
                    # Validar género
                    while True:
                        genero = prompt('Introduce el genero [M/F]: ', style=style).upper()
                        if genero == "" or genero in ['M', 'F']:
                            break
                        else:
                            console.print('[bold #C70039]Por favor, introduce M o F para el género.[/]')
                            continue

                    triatlon.editar_atleta(id_evento,dni,nombre,apellido,fecha_nacimiento,genero) 
                    prompt(style=style)
                elif opcion == "5":
                    orden = prompt("Por que quieres ordenar: ",style=style)
                    triatlon.ordenar_por_opcion(orden)
                    prompt()

                elif opcion == "6":
                    break
        # Menu de registros de tiempos
        elif opcion == "3":

            while True:
                system("cls")
                console.print(menu_registros_alineado)
                opcion = prompt("Selecciona una opción: ",style=style)
                if opcion == "1":
                    
                    while True:
                        try:
                            id_evento = int(prompt('ID del evento al que pertenece: ',completer = completar_ids(),style=style))
                            break

                        except:
                            console.print(Panel("[bold #C70039]Introduce un numero!![/]",border_style='bold #C70039',width=30))
                            continue
                    
                    while True:
                        dni = prompt('Introduce el dni del atleta: ', style=style)
                        if validar_campo_vacio(dni) and validar_dni(dni):
                            break
                        else:
                            continue

                    # Validamos campo vacio y que el formato sea correcto
                    while True:
                        # Pedimos el tiempo
                        tiempo = prompt("Introduce el tiempo en formato hh:mm:ss : ", style=style)
                        # Validamos que no este vacio
                        if validar_campo_vacio(tiempo):
                            # Dividmos en 3 partes
                            partes = tiempo.split(":")
                            if len(partes) == 3:
                                break
                            else:
                                console.print(Panel('[bold #C70039]Formato incorrecto. Debe tener 3 partes separadas por ":"[/]',border_style='bold #C70039'))
                        else:
                            continue

                    horas, minutos, segundos = map(int, tiempo.split(":"))
                    tiempo_natacion = timedelta(hours=horas, minutes=minutos, seconds=segundos)
                    triatlon.registrar_tiempo_natacion(id_evento,dni,tiempo_natacion)
                    prompt(style=style)

                elif opcion == "2":

                    while True:
                        try:
                            id_evento = int(prompt('ID del evento al que pertenece el atleta: ',completer = completar_ids(),style=style))
                            break

                        except:
                            console.print(Panel("[bold #C70039]Introduce un numero!![/]",border_style='bold #C70039',width=30))
                            continue

                    while True:
                        dni = prompt('Introduce el dni del atleta: ', style=style)
                        if validar_campo_vacio(dni) and validar_dni(dni):
                            break
                        else:
                            continue

                    # Validamos campo vacio y que el formato sea correcto
                    while True:
                        # Pedimos el tiempo
                        tiempo = prompt("Introduce el tiempo en formato hh:mm:ss : ", style=style)
                        # Validamos que no este vacio
                        if validar_campo_vacio(tiempo):
                            # Dividmos en 3 partes
                            partes = tiempo.split(":")
                            if len(partes) == 3:
                                break
                            else:
                                console.print(Panel('[bold #C70039]Formato incorrecto. Debe tener 3 partes separadas por ":"[/]',border_style='bold #C70039'))
                        else:
                            continue
                    horas, minutos, segundos = map(int, tiempo.split(":"))
                    tiempo_ciclismo = timedelta(hours=horas, minutes=minutos, seconds=segundos)
                    triatlon.registrar_tiempo_ciclismo(id_evento,dni,tiempo_ciclismo)

                elif opcion == "3":
                    # Pedimos los datos para registrar el tiempo de la carrera
                    while True:
                        try:
                            id_evento = int(prompt('ID del evento al que pertenece el atleta: ',completer = completar_ids(),style=style))
                            break

                        except:
                            console.print(Panel("[bold #C70039]Introduce un numero!![/]",border_style='bold #C70039',width=30))
                            continue

                    while True:
                        dni = prompt('Introduce el dni del atleta: ', style=style)
                        if validar_campo_vacio(dni) and validar_dni(dni):
                            break
                        else:
                            continue

                    # Validamos campo vacio y que el formato sea correcto
                    while True:
                        # Pedimos el tiempo
                        tiempo = prompt("Introduce el tiempo en formato hh:mm:ss : ", style=style)
                        # Validamos que no este vacio
                        if validar_campo_vacio(tiempo):
                            # Dividmos en 3 partes
                            partes = tiempo.split(":")
                            if len(partes) == 3:
                                break
                            else:
                                console.print(Panel('[bold #C70039]Formato incorrecto. Debe tener 3 partes separadas por ":"[/]',border_style='bold #C70039'))
                        else:
                            continue
                    horas, minutos, segundos = map(int, tiempo.split(":"))
                    tiempo_carrera = timedelta(hours=horas, minutes=minutos, seconds=segundos)
                    triatlon.registrar_tiempo_carrera(id_evento,dni,tiempo_carrera)

                elif opcion == "4":
                    # Pedimos los datos y luego usamos la funcion para que muestre el tiempo total del atleta
                    while True:
                        try:
                            id_evento = int(prompt('Introduce el id del atleta para calcular el tiempo total: ',completer = completar_ids(),style=style))
                            break

                        except:
                            console.print(Panel("[bold #C70039]Introduce un numero!![/]",border_style='bold #C70039',width=30))
                            continue
                    while True:
                        # Pedimos y validamos el dni
                        dni = prompt('Introduce el dni del atleta: ', style=style)
                        if validar_campo_vacio(dni) and validar_dni(dni):
                            break
                        else:
                            continue
                    console.print(triatlon.calcular_tiempo_total(id_evento,dni))
                    prompt(style=style)

                elif opcion == "5":
                    break

        # Menu de estadisicas
        elif opcion == "4":

            while True:
                system("cls")
                console.print(menu_estadisticas_alineado)
                # Pedimos la opcion
                opcion = prompt("Selecciona una opción: ",style=style)

                if opcion == "1":
                    # Mostramos toda la clasificacion de los tiempos
                    triatlon.clasificacion_general()
                    prompt(style=style)
                    

                elif opcion == "2":
                    # Auto completado con las categorias del triatlon
                    categorias = FuzzyWordCompleter(['Natacion','Ciclismo','Carrera'])
                    # Pedimos la categoria
                    categoria = prompt('De que categoria quieres mostrar los tiempos: ',completer = categorias,style=style).lower()
                    # Usamos el metodo para mostrar la clasificacion por categoria
                    triatlon.clasificacion_categoria(categoria)
                    prompt(style=style)
                    
                elif opcion == "3":
                    system("cls")
                    break

        elif opcion == "5":
            break


if __name__ == "__main__":
    main()
