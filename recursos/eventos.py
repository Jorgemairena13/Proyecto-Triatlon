

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
        print(f"Nombre: {self.nombre}")
        print(f"Fecha: {self.fecha}")
        print(f"Lugar: {self.lugar}")
        print(f"Distancia total en KM: {self.distancia}")
    
     
# Clase triatlon para gestionar los participantes y los eventos
class Triatlon():

    # Constructor con un diccionario para añadir los eventos y los participantes
    def __init__(self):
        self.eventos = {}

    # Agrega un obejego de la clase evento al dic con clave en el id
    def agregar_evento(self,id_evento, nombre, fecha, lugar, distancia):
        self.eventos[id_evento] = Evento(id_evento, nombre, fecha, lugar, distancia)

    # Agrega un participante al evento
    def agregar_participante(self,dni,nombre, apellido, fecha_nacimiento, genero,id_evento):
        '''Agrega un participante al evento'''
        self.eventos[id_evento][dni] = Atleta(dni,nombre,apellido,fecha_nacimiento,genero)

    # Muestra los eventos que hemos creado
    def mostrar_eventos(self):
        ''''Muestra los eventos creados'''
        for evento in self.eventos.values():
            print(f'ID: {evento.id} - Nombre: {evento.nombre} - Fecha: {evento.fecha} - Lugar: {evento.distancia} ')
