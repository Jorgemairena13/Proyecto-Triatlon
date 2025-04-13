from os import system
from rich import print 
from rich.panel import Panel
from rich.align import Align
from prompt_toolkit import prompt
from prompt_toolkit.styles import Style
from rich.table import Table
from prompt_toolkit.completion import FuzzyWordCompleter
from rich.console import Console
from datetime import datetime
from time import sleep
import random
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn

# Menu principal
menu_principal = ("""
           
[#2e27ff]1. Gestión de eventos[/]
                  
[#9a27ff]2. Gestión de atletas[/]
                  
[#ff27f8]3. Registros y resultados[/]
                  
[#ff278c]4. Informes y estadísticas[/]
                  
[#ff2e27]5. Salir[/]


""")

menu_alineado = Panel(
    Align.center(menu_principal),
    border_style="#27e5ff",
    title="[blink][#fff933]SISTEMA DE GESTIÓN DE TRIATLONES [/]",
    expand= True)

# Menu de los eventos
menu_eventos = """
[#2e27ff]1. Crear nuevo evento

[#9a27ff]2. Editar eventos 

[#ff27f8]3. Ver calendario

[#ff2e27]4. Volver al menú principal[/]
"""

menu_eventos_alineado = Panel(
    Align.center(menu_eventos),
    border_style="#27e5ff",
    title="[blink][#fff933]Gestion de eventos[/]",
    expand= True)

# Menu de atletas
menu_atletas = """
[#2e27ff]1. Registrar atleta

[#9a27ff]2. Buscar atleta

[#ff27f8]3. Editar atleta

[#ff2e27]4. Volver al menú principal[/]
"""

menu_atletas_alineado = Panel(
    Align.center(menu_atletas),
    border_style="#27e5ff",
    title="[blink][#fff933]Gestion de atletas[/]",
    expand= True)

# Menu de registros
menu_registros = """
[#2e27ff]1. Registrar tiempos de natación

[#9a27ff]2. Registrar tiempos de ciclismo

[#ff27f8]3. Registrar tiempos de carrera

[#ff278c]4. Calcular tiempo total

[#ff2e27]5. Volver al menú principal[/]
"""

menu_registros_alineado = Panel(
    Align.center(menu_registros),
    border_style="#27e5ff",
    title="[blink][#fff933]Registrar tiempos[/]",
    expand= True)

# Menu de estadisticas
menu_estadisticas = """
[#2e27ff]1. Ver clasificación general

[#9a27ff]2. Ver clasificación por categorías

[#ff2e27]3. Volver al menú principal[/]
"""
menu_estadisticas_alineado = Panel(
    Align.center(menu_estadisticas),
    border_style="#27e5ff",
    title="[blink #fff933]Estadisticas[/]",
    expand= True)









