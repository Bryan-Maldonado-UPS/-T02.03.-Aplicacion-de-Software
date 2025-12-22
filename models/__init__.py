"""
Módulo de modelos SQLAlchemy
Importa todos los modelos para facilitar el acceso
"""

from models.enums import EstadoMatricula, EstadoAsistencia
from models.representante import Representante
from models.docente import Docente
from models.curso import Curso
from models.estudiante import Estudiante
from models.asignatura import Asignatura
from models.matricula import Matricula
from models.asistencia import Asistencia
from models.calificacion import Calificacion

__all__ = [
    "EstadoMatricula",
    "EstadoAsistencia",
    "Representante",
    "Docente",
    "Curso",
    "Estudiante",
    "Asignatura",
    "Matricula",
    "Asistencia",
    "Calificacion",
]
