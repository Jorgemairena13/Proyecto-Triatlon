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
menu_principal = Panel("""
===== SISTEMA DE GESTIÓN DE TRIATLONES =====
1. Gestión de eventos
2. Gestión de atletas
3. Registros y resultados
4. Informes y estadísticas
5. Salir


""",border_style='blue')

# Menu de los eventos
menu_eventos = """
===== GESTIÓN DE EVENTOS =====
1. Crear nuevo evento
2. Editar eventos 
3. Ver calendario
4. Volver al menú principal
"""

# Menu de atletas
menu_atletas = """
===== GESTIÓN DE ATLETAS =====
1. Registrar atleta
2. Buscar atleta
3. Editar atleta
4. Volver al menú principal
"""

# Menu de registros
menu_registros = """
===== REGISTROS Y RESULTADOS =====
1. Inscribir atleta a evento
2. Registrar tiempos de natación
3. Registrar tiempos de ciclismo
4. Registrar tiempos de carrera
5. Calcular tiempo total
6. Volver al menú principal
"""

# Menu de estadisticas
menu_estadisticas = """
===== INFORMES Y ESTADÍSTICAS =====
1. Ver clasificación general
2. Ver clasificación por categorías
3. Volver al menú principal
"""








