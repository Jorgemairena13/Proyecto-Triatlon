from rich.console import Console
from datetime import timedelta
from rich.panel import Panel
from rich.table import Table
from rich.align import Align

console = Console()

def centrar_menu(menu):
    ''''
    Crea un panel con color de la terminal para centrar el panel creado
    '''
    menu_alineado = Panel(
    Align.center(menu),
    border_style='#0c0c0c'
    )
    return menu_alineado

class Atleta:
    #Constructor de atleta
    def __init__(self,dni, nombre, apellido, fecha_nacimiento, genero):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.genero = genero
        self.tiempo_natacion = timedelta(hours=0, minutes=0, seconds=0)
        self.tiempo_ciclismo = timedelta(hours=0, minutes=0, seconds=0)
        self.tiempo_carrera = timedelta(hours=0, minutes=0, seconds=0)
        self.tiempo_final = timedelta(hours=0, minutes=0, seconds=0)

    def establecer_tiempo_natacion(self,tiempo):
        self.tiempo_natacion = tiempo

    def establecer_tiempo_ciclismo(self,tiempo):
        self.tiempo_ciclismo = tiempo

    def establecer_tiempo_carrera(self,tiempo):
        self.tiempo_carrera = tiempo

    def calcular_tiempo_total(self):
        tiempo_natacion = self.tiempo_natacion 
        tiempo_ciclismos = self.tiempo_ciclismo
        tiempo_carrera = self.tiempo_carrera
        tiempo_total = tiempo_natacion + tiempo_ciclismos + tiempo_carrera
        self.tiempo_final = tiempo_total
        return self.tiempo_final
        


    def mostrar_atleta(self):
        '''Muestra todos las  caractericticas del atleta '''
            
        console.print("")
        console.print(f"DNI: {self.dni}")
        console.print(f"Nombre: {self.nombre}")
        console.print(f"Apellido: {self.apellido}")
        console.print(f"Fecha de nacimiento: {self.fecha_nacimiento}")
        console.print(f"Genero: {self.genero}")

    def mostrar_tiempos(self):
        """Muestra los tiempos del atleta"""
        console.print("")
        console.print(f"Tiempos de {self.nombre}")
        console.print(f"Tiempo natacion: {self.tiempo_natacion}")
        console.print(f"Tiempo ciclismo: {self.tiempo_ciclismo}")
        console.print(f"Tiempo carrera: {self.tiempo_carrera}")
        console.print(f"Tiempo total: {self.calcular_tiempo_total()}")
        

    
# Clase evento
class Evento:
    # Constructor
    def __init__(self,id_evento, nombre, fecha, lugar, distancia):
        
        self.id = id_evento
        self.nombre = nombre
        self.fecha = fecha
        self.lugar = lugar
        self.distancia = distancia
        self.participantes = {}
        
    # Funcion para mostra el evento
    def mostrar_evento(self):
        '''Muestra todos las  caractericticas del evento '''
        console.print("")
        console.print(f"ID: {self.id}")
        console.print(f"Nombre: {self.nombre}")
        console.print(f"Fecha: {self.fecha}")
        console.print(f"Lugar: {self.lugar}")
        console.print(f"Distancia total en KM: {self.distancia}")
    
# Clase triatlon para gestionar los participantes y los eventos
class Triatlon():

    # Constructor con un diccionario para añadir los eventos y los participantes
    def __init__(self):
        self.eventos = {}

    # Agrega un obejego de la clase evento al dic con clave en el id
    def agregar_evento(self,id_evento, nombre, fecha, lugar, distancia):
        self.eventos[id_evento] = Evento(id_evento, nombre, fecha, lugar, distancia)
        

    def eliminar_evento(self,id_evento):
        '''
        Elimina un evento pasandole el id del eventto que se quiere eliminar
        '''
        if id_evento in self.eventos:
            # Mensaje de confirmacion de la eliminacion
            console.print(Panel(f'[bold #28a745]Evento {self.eventos[id_evento].nombre} eliminado  con exito[/]',width=30,border_style='bold #28a745'))
            del self.eventos[id_evento]
        else:
            # Mensaje de que no se encuentra el id que nos ha pasado
            console.print(Panel(f"[bold #C70039]El evento con ID {id_evento} no se encuentra[/]",border_style='bold #C70039',width=30))
        
    # Agrega un participante al evento
    def agregar_participante(self, dni, nombre, apellido, fecha_nacimiento, genero, id_evento):
        if id_evento in self.eventos:
            # Añade el participante al diccionario de participantes del evento
            self.eventos[id_evento].participantes[dni] = Atleta(dni, nombre, apellido, fecha_nacimiento, genero)
            console.print(Panel(f'[bold #28a745]Atleta {nombre} registrado con exito[/]',width=30,border_style='bold #28a745'))
        else:
            # Mensaje de que no se encuentra el ID
            console.print(Panel(f"[bold #C70039]El evento con ID {id_evento} no se encuentra[/]",border_style='bold #C70039',width=30))

    # Muestra los eventos que hemos creado
    def mostrar_eventos(self):
        ''''Muestra los eventos creados'''
        if self.eventos:
            # Creamos la tabla 
            tabla = Table(title = '[bold]Lista de eventos[/]',expand=True,border_style='bold #27e5ff')
            #Le añadimos las columnas
            tabla.add_column('ID')
            tabla.add_column('Nombre')
            tabla.add_column('Fecha')
            tabla.add_column('Lugar')
            tabla.add_column('Distancia')
            # Por evento que exista le añadimos una fila con los datos del evento
            for evento in self.eventos.values():
                tabla.add_row(str(evento.id),evento.nombre,evento.fecha,evento.lugar,evento.distancia)

            # Mostramos la tabla
            console.print(tabla)

            # Mensaje por si no hay eventos creados
        else:
            console.print('No hay eventos creados')

    def editar_evento(self,id_evento, nombre, fecha, lugar, distancia):
        if id_evento in self.eventos:
            del self.eventos[id_evento]
            self.agregar_evento(id_evento, nombre, fecha, lugar, distancia)
            self.eventos[id_evento].mostrar_evento()
        else:
            console.print(Panel('No existe el evento que quieres editar',border_style='bold #C70039',width=30))


    def buscar_atleta(self,id_evento,dni):
        '''
        Busca un atleta en un evento con un id de evento y su dni
        '''
        if id_evento in self.eventos:
            if dni in self.eventos[id_evento].participantes:
                atleta = self.eventos[id_evento].participantes[dni]
                atleta.mostrar_atleta()
                
            else:
                console.print(Panel("[bold #C70039]No se encuentra el atleta con ese DNI[/]", border_style='bold #C70039'))
        
        else:
             console.print(Panel("[bold #C70039]No se encuentra el evento[/]", border_style='bold #C70039'))


    # Metodo para editar al atleta
    def editar_atleta(self, id_evento, dni, nombre='', apellido='', fecha_nacimiento='', genero=''):
        """
        Edita los datos de un atleta existente en un evento específico
        Permite modificar solo los campos que se proporcionen, manteniendo los demás igual
        """
        # Verificar que el evento existe
        if id_evento not in self.eventos:
            console.print(Panel(f"[bold #C70039]El evento con id: {id_evento} no existe [/]", border_style='bold #C70039'))
            return
        
        # Verificar que el atleta existe en ese evento
        if dni not in self.eventos[id_evento].participantes:
            console.print(Panel(f"No existe un atleta con DNI {dni} en este evento", border_style='bold #C70039'))
            return
        
        # Obtener el atleta actual
        atleta = self.eventos[id_evento].participantes[dni]
        
        # Modificar solo los campos proporcionados
        if nombre:
            atleta.nombre = nombre
        if apellido:
            atleta.apellido = apellido
        if fecha_nacimiento:
            atleta.fecha_nacimiento = fecha_nacimiento
        if genero:
            atleta.genero = genero
        
        console.print(f"Atleta con DNI {dni} actualizado correctamente")
        
        # Mostrar los datos actualizados
        atleta.mostrar_atleta()
    
    def registrar_tiempo_natacion(self,id_evento,dni,tiempo):
        """
        Comprueba evento al que se quiere agregar y que el atleta exista y el tiempo del atleta
        """

        # Combrobamos que el evento exista si no le devolvemos el mensaje de que no existe
        if id_evento not in self.eventos:
            console.print(Panel(f"[bold #C70039]El evento con id: {id_evento} no existe [/]", border_style='bold #C70039'))
            return
        
        # Combrobamos que el dni exista en ese evento donde vamos a  registrar el timepo
        if dni not in self.eventos[id_evento].participantes:
            console.print(Panel(f"No existe un atleta con DNI {dni} en este evento", border_style='bold #C70039'))
            return
        
        self.eventos[id_evento].participantes[dni].establecer_tiempo_natacion(tiempo) 


    def registrar_tiempo_ciclismo(self,id_evento,dni,tiempo):
        # Comprobamos que el evento exista
        if id_evento not in self.eventos:
            console.print(Panel(f"[bold #C70039]El evento con id: {id_evento} no existe [/]", border_style='bold #C70039'))
            return
        
        # Combrobamos que el dni exista en ese evento donde vamos a  registrar el timepo
        if dni not in self.eventos[id_evento].participantes:
            console.print(Panel(f"No existe un atleta con DNI {dni} en este evento", border_style='bold #C70039'))
            return
        # Registramos el tiempo del atleta
        self.eventos[id_evento].participantes[dni].establecer_tiempo_ciclismo(tiempo)

    def registrar_tiempo_carrera(self,id_evento,dni,tiempo):

        # Comprobamos que el evento exista
        if id_evento not in self.eventos:
            console.print(Panel(f"[bold #C70039]El evento con id: {id_evento} no existe [/]", border_style='bold #C70039'))
            return
        
        # Combrobamos que el dni exista en ese evento donde vamos a  registrar el timepo
        if dni not in self.eventos[id_evento].participantes:
            console.print(Panel(f"No existe un atleta con DNI {dni} en este evento", border_style='bold #C70039'))
            return
        
        # Agregamos el tiempo a ese atleta
        self.eventos[id_evento].participantes[dni].establecer_tiempo_carrera(tiempo)

    def calcular_tiempo_total(self,id_evento,dni):
        
        # Comprobamos que el evento exista
        if id_evento not in self.eventos:
            console.print(Panel(f"[bold #C70039]El evento con id: {id_evento} no existe [/]", border_style='bold #C70039'))
            return
        
        # Combrobamos que el dni exista en ese evento donde vamos a  registrar el timepo
        if dni not in self.eventos[id_evento].participantes:
            console.print(Panel(f"No existe un atleta con DNI {dni} en este evento", border_style='bold #C70039'))
            return
        
        # Calculamos el tiempo total del atleta
        return self.eventos[id_evento].participantes[dni].calcular_tiempo_total()

    def clasificacion_general(self):
        """Muestra la clasificación de todos los eventos ordenada por tiempo"""
    
        for id_evento, evento in self.eventos.items():
            # Primero calculamos los tiempos totales de todos los participantes
            for atleta in evento.participantes.values():
                atleta.calcular_tiempo_total()
            
            # Ordenamos por tiempo del más rápido al más lento
            atletas_ordenados = sorted(evento.participantes.values(), 
                                    key=lambda atleta: atleta.tiempo_final)
            
            # Mostramos la clasificación del evento
            panel_titulo = Panel(f"[#af54fe]Clasificación del evento: {evento.nombre}[/]", border_style='bold #af54fe',padding = 1)
            panel_evento = centrar_menu(panel_titulo)
            console.print(panel_evento)
            for posicion, atleta in enumerate(atletas_ordenados, 1):
                if posicion == 1:
                    panel1 = Panel(f"[bold #FFD700]👑 {posicion}. {atleta.nombre}: {atleta.tiempo_final}",width = 30,padding=1,border_style='bold #FFD700')
                    panel_alineado = centrar_menu(panel1)
                    console.print(panel_alineado)
                elif posicion == 2:
                    panel2 = Panel(f"[bold #C0C0C0]🥈 {posicion}. {atleta.nombre}: {atleta.tiempo_final}",width = 30,padding=1,border_style='bold #C0C0C0')
                    panel_alineado = centrar_menu(panel2)
                    console.print(panel_alineado)
                elif posicion == 3:
                    panel3 = Panel(f"[bold #CD7F32]🥉 {posicion}. {atleta.nombre}: {atleta.tiempo_final}",width = 30,padding=1,border_style='bold #CD7F32')
                    panel_alineado = centrar_menu(panel3)
                    console.print(panel_alineado)
                else:
                    panel_sencillo = (Panel(f"   {posicion}. {atleta.nombre}: {atleta.tiempo_final}",width = 30,padding=1,border_style='#27e5ff'))
                    panel_alineado = centrar_menu(panel_sencillo)
                    console.print(panel_alineado)
                
            

    def clasificacion_categoria(self,categoria):
        """
        Muestra la clasificación de todos los eventos ordenada por tiempo
        """
    
        for id_evento, evento in self.eventos.items():
            
            # Primero calculamos los tiempos totales de todos los participantes
            for atleta in evento.participantes.values():
                atleta.calcular_tiempo_total()
            
            if categoria == 'natacion':
                panel_categoria = Panel(f"[#af54fe]Clasificación del evento: {evento.nombre} Categoria {categoria}[/]", border_style='bold #af54fe',padding = 1)
                panel_categorias = centrar_menu(panel_categoria)
                console.print(panel_categorias)
                # Ordenamos por tiempo (del más rápido al más lento)
                atletas_ordenados = sorted(evento.participantes.values(), 
                                        key=lambda atleta: atleta.tiempo_natacion)
                
                for posicion, atleta in enumerate(atletas_ordenados, 1):
                    if posicion == 1:
                        panel1 = Panel(f"[bold #FFD700]👑 {posicion}. {atleta.nombre}: {atleta.tiempo_natacion}",width = 30,padding=1,border_style='bold #FFD700')
                        panel_alineado = centrar_menu(panel1)
                        console.print(panel_alineado)
                    elif posicion == 2:
                        panel2 = Panel(f"[bold #C0C0C0]🥈 {posicion}. {atleta.nombre}: {atleta.tiempo_natacion}",width = 30,padding=1,border_style='bold #C0C0C0')
                        panel_alineado = centrar_menu(panel2)
                        console.print(panel_alineado)
                    elif posicion == 3:
                        panel3 = Panel(f"[bold #CD7F32]🥉 {posicion}. {atleta.nombre}: {atleta.tiempo_natacion}",width = 30,padding=1,border_style='bold #CD7F32')
                        panel_alineado = centrar_menu(panel3)
                        console.print(panel_alineado)
                    else:
                        panel_sencillo = (Panel(f"   {posicion}. {atleta.nombre}: {atleta.tiempo_natacion}",width = 30,padding=1,border_style='#27e5ff'))
                        panel_alineado = centrar_menu(panel_sencillo)
                        console.print(panel_alineado)

            elif categoria == 'ciclismo':
                panel_categoria = Panel(f"[#af54fe]Clasificación del evento: {evento.nombre} Categoria {categoria}[/]", border_style='bold #af54fe',padding = 1)
                panel_categorias = centrar_menu(panel_categoria)
                console.print(panel_categorias)
                atletas_ordenados = sorted(evento.participantes.values(), 
                                        key=lambda atleta: atleta.tiempo_ciclismo)
                
                for posicion, atleta in enumerate(atletas_ordenados, 1):
                    if posicion == 1:
                        panel1 = Panel(f"[bold #FFD700]👑 {posicion}. {atleta.nombre}: {atleta.tiempo_ciclismo}",width = 30,padding=1,border_style='bold #FFD700')
                        panel_alineado = centrar_menu(panel1)
                        console.print(panel_alineado)
                    elif posicion == 2:
                        panel2 = Panel(f"[bold #C0C0C0]🥈 {posicion}. {atleta.nombre}: {atleta.tiempo_ciclismo}",width = 30,padding=1,border_style='bold #C0C0C0')
                        panel_alineado = centrar_menu(panel2)
                        console.print(panel_alineado)
                    elif posicion == 3:
                        panel3 = Panel(f"[bold #CD7F32]🥉 {posicion}. {atleta.nombre}: {atleta.tiempo_ciclismo}",width = 30,padding=1,border_style='bold #CD7F32')
                        panel_alineado = centrar_menu(panel3)
                        console.print(panel_alineado)
                    else:
                        panel_sencillo = (Panel(f"   {posicion}. {atleta.nombre}: {atleta.tiempo_ciclismo}",width = 30,padding=1,border_style='#27e5ff'))
                        panel_alineado = centrar_menu(panel_sencillo)
                        console.print(panel_alineado)

            elif categoria == 'carrera':
                panel_categoria = Panel(f"[#af54fe]Clasificación del evento: {evento.nombre} Categoria {categoria}[/]", border_style='bold #af54fe',padding = 1)
                panel_categorias = centrar_menu(panel_categoria)
                console.print(panel_categorias)
                atletas_ordenados = sorted(evento.participantes.values(), 
                                        key=lambda atleta: atleta.tiempo_carrera)
                
                for posicion, atleta in enumerate(atletas_ordenados, 1):
                    if posicion == 1:
                        panel1 = Panel(f"[bold #FFD700]👑 {posicion}. {atleta.nombre}: {atleta.tiempo_carrera}",width = 30,padding=1,border_style='bold #FFD700')
                        panel_alineado = centrar_menu(panel1)
                        console.print(panel_alineado)
                    elif posicion == 2:
                        panel2 = Panel(f"[bold #C0C0C0]🥈 {posicion}. {atleta.nombre}: {atleta.tiempo_carrera}",width = 30,padding=1,border_style='bold #C0C0C0')
                        panel_alineado = centrar_menu(panel2)
                        console.print(panel_alineado)
                    elif posicion == 3:
                        panel3 = Panel(f"[bold #CD7F32]🥉 {posicion}. {atleta.nombre}: {atleta.tiempo_carrera}",width = 30,padding=1,border_style='bold #CD7F32')
                        panel_alineado = centrar_menu(panel3)
                        console.print(panel_alineado)
                    else:
                        panel_sencillo = (Panel(f"   {posicion}. {atleta.nombre}: {atleta.tiempo_carrera}",width = 30,padding=1,border_style='#27e5ff'))
                        panel_alineado = centrar_menu(panel_sencillo)
                        console.print(panel_alineado)
            else:
                console.print(Panel("[bold #C70039]No se encuentra la categoria[/]",border_style='bold #C70039'))
                break
            

            
            




        
