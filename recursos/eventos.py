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


    def mostrar_atleta(self):
            '''Muestra todos las  caractericticas del atleta '''
            
            console.print("")
            console.print(f"DNI: {self.dni}")
            console.print(f"Nombre: {self.nombre}")
            console.print(f"Apellido: {self.apellido}")
            console.print(f"Fecha de nacimiento: {self.fecha_nacimiento}")
            console.print(f"Genero: {self.genero}")

    def eliminar_atleta(self,dni):
        pass
        
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
        self.eventos = {
    
}

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
                
                for dni,participante in evento.participantes.items():
                    participante.mostrar_atleta()
        else:
            console.print('No hay eventos creados')

    def editar_evento(self,id_evento, nombre, fecha, lugar, distancia):
        if self.eventos:
            del self.eventos[id_evento]
            self.agregar_evento(id_evento, nombre, fecha, lugar, distancia)
        else:
            console.print('No hay eventos que editar')


    def buscar_atleta(self,id_evento,dni):
        if self.eventos:
            for dni_buscar,atleta in self.eventos[id_evento].participantes.items():
                if dni_buscar == dni:
                    atleta.mostrar_atleta()
                    break
                else:
                    console.print('No se encuentra el dni buscado')
        else:
            console.print('No hay eventos que editar')

    # Añade este método a la clase Triatlon
    def editar_atleta(self, id_evento, dni, nombre='', apellido='', fecha_nacimiento='', genero=''):
        """
        Edita los datos de un atleta existente en un evento específico
        Permite modificar solo los campos que se proporcionen, manteniendo los demás igual
        """
        # Verificar que el evento existe
        if id_evento not in self.eventos:
            console.print(f"El evento con ID {id_evento} no existe")
            return
        
        # Verificar que el atleta existe en ese evento
        if dni not in self.eventos[id_evento].participantes:
            console.print(f"No existe un atleta con DNI {dni} en este evento")
            return
        
        # Obtener el atleta actual
        atleta = self.eventos[id_evento].participantes[dni]
        
        # Modificar solo los campos proporcionados
        if nombre is not '':
            atleta.nombre = nombre
        if apellido is not '':
            atleta.apellido = apellido
        if fecha_nacimiento is not '':
            atleta.fecha_nacimiento = fecha_nacimiento
        if genero is not '':
            atleta.genero = genero
        
        console.print(f"Atleta con DNI {dni} actualizado correctamente")
        
        # Mostrar los datos actualizados
        atleta.mostrar_atleta()
    
    def registrar_tiempo_natacion(self):
        pass

    def registrar_tiempo_ciclismo(self):
        pass

    def registrar_tiempo_carrera(self):
        pass

    def calcular_tiempo_total(self):
        pass




        
