"""
Módulo de Repositorios
"""
from repositories.base import BaseRepository
from repositories.repositories import (
    RepresentanteRepository,
    EstudianteRepository,
    DocenteRepository,
    CursoRepository,
    AsignaturaRepository,
    MatriculaRepository,
    AsistenciaRepository,
    CalificacionRepository
)

__all__ = [
    "BaseRepository",
    "RepresentanteRepository",
    "EstudianteRepository",
    "DocenteRepository",
    "CursoRepository",
    "AsignaturaRepository",
    "MatriculaRepository",
    "AsistenciaRepository",
    "CalificacionRepository",
]
