"""
Rutas e inicialización del Router
"""
from fastapi import APIRouter
from . import representante, estudiante, docente, curso, asignatura, matricula, calificacion, asistencia

# Crear router principal
api_router = APIRouter(prefix="/api/v1")

# Incluir todos los routers
api_router.include_router(representante.router)
api_router.include_router(estudiante.router)
api_router.include_router(docente.router)
api_router.include_router(curso.router)
api_router.include_router(asignatura.router)
api_router.include_router(matricula.router)
api_router.include_router(calificacion.router)
api_router.include_router(asistencia.router)

__all__ = ["api_router"]
