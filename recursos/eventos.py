from rich.console import Console
console = Console()
class Atleta:
    #Constructor de atleta
    def __init__(self,dni, nombre, apellido, fecha_nacimiento, genero):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.genero = genero

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
        '''Muestra todos las  caracterictivas del evento '''
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

    # Agrega un participante al evento
    def agregar_participante(self, dni, nombre, apellido, fecha_nacimiento, genero, id_evento):
        if id_evento in self.eventos:
            # Añade el participante al diccionario de participantes del evento
            self.eventos[id_evento].participantes[dni] = Atleta(dni, nombre, apellido, fecha_nacimiento, genero)
            console.print(f'Atleta {nombre} registrado con exito')
        else:
            console.print(f"El evento con ID {id_evento} no existe")

    # Muestra los eventos que hemos creado
    def mostrar_eventos(self):
        ''''Muestra los eventos creados'''
        if self.eventos:
            for evento in self.eventos.values():
                evento.mostrar_evento()
                print('')
                console.print('Participantes')
                # Mejorar estetica ++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                for dni,participante in evento.participantes.items():
                    print(dni,participante.nombre)
        else:
            console.print('No hay eventos creados')

    def editar_evento(self,id_evento, nombre, fecha, lugar, distancia):
        if self.eventos:
            del self.eventos[id_evento]
            self.agregar_evento(id_evento, nombre, fecha, lugar, distancia)
        else:
            console.print('No hay eventos que editar')


    def buscar_atleta(self):
        pass

    def editar_atleta(self):
        pass
    
    def registrar_tiempo_natacion(self):
        pass

    def registrar_tiempo_ciclismo(self):
        pass

    def registrar_tiempo_carrera(self):
        pass

    def calcular_tiempo_total(self):
        pass

        
