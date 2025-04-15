# Sistema de Gestión de Triatlón

Este proyecto es un sistema de gestión para eventos de triatlón que permite administrar atletas, eventos y sus tiempos en las diferentes disciplinas.

## Características Principales

- Gestión de eventos de triatlón
- Registro y gestión de atletas
- Seguimiento de tiempos en las tres disciplinas:
  - Natación
  - Ciclismo
  - Carrera
- Cálculo automático de tiempos totales
- Sistema de búsqueda y edición de atletas

## Requisitos del Sistema

- Python 3.x
- Módulo `rich` para la interfaz de consola

## Instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/Jorgemairena13/Proyecto-Triatlon
```

2. Instalar las dependencias:
```bash
pip install rich
```

## Estructura del Proyecto

```
Triatlon/
├── recursos/
│   └── eventos.py    # Contiene las clases principales del sistema
└── README.md         # Este archivo
```

## Clases Principales

### Atleta
- Gestiona la información personal de los atletas
- Registra y calcula tiempos en las diferentes disciplinas
- Permite mostrar información detallada del atleta

### Evento
- Administra la información de cada evento
- Gestiona la lista de participantes
- Almacena detalles como fecha, lugar y distancia

### Triatlon
- Clase principal que coordina eventos y atletas
- Proporciona métodos para:
  - Agregar/editar eventos
  - Registrar/editar atletas
  - Registrar tiempos
  - Calcular tiempos totales

## Uso

El sistema se utiliza a través de la consola, proporcionando una interfaz intuitiva para:
- Crear y gestionar eventos
- Registrar atletas
- Introducir tiempos de competición
- Consultar resultados

## Contribución

Las contribuciones son bienvenidas. Por favor, asegúrate de:
1. Hacer fork del proyecto
2. Crear una rama para tu feature 
3. Commit de tus cambios 
4. Push a la rama 
5. Abrir un Pull Request

## Licencia


