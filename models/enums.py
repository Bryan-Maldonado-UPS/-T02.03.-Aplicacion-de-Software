"""
Enumeraciones para los estados de la aplicación
"""
from enum import Enum

class EstadoMatricula(str, Enum):
    """Estados posibles de una matrícula"""
    REGISTRADO = "REGISTRADO"
    MATRICULADO = "MATRICULADO"
    ACTIVO = "ACTIVO"
    SUSPENDIDO = "SUSPENDIDO"
    RETIRADO = "RETIRADO"
    GRADUADO = "GRADUADO"


class EstadoAsistencia(str, Enum):
    """Estados posibles de la asistencia"""
    PRESENTE = "PRESENTE"
    AUSENTE = "AUSENTE"
    ATRASO = "ATRASO"
    JUSTIFICADO = "JUSTIFICADO"
