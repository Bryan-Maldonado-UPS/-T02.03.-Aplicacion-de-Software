from pydantic import BaseModel, Field
from typing import Optional
from datetime import date
from enum import Enum


class EstadoMatriculaEnum(str, Enum):
    """Estados válidos para una matrícula"""
    REGISTRADO = "REGISTRADO"
    MATRICULADO = "MATRICULADO"
    ACTIVO = "ACTIVO"
    SUSPENDIDO = "SUSPENDIDO"
    RETIRADO = "RETIRADO"
    GRADUADO = "GRADUADO"


class MatriculaCreate(BaseModel):
    """Schema para crear una matrícula"""
    fecha: Optional[date] = None
    estudiante_id: int
    curso_id: int
    estado: EstadoMatriculaEnum = EstadoMatriculaEnum.REGISTRADO

    class Config:
        json_schema_extra = {
            "example": {
                "fecha": "2024-01-15",
                "estudiante_id": 1,
                "curso_id": 1,
                "estado": "ACTIVO"
            }
        }


class MatriculaUpdate(BaseModel):
    """Schema para actualizar una matrícula"""
    fecha: Optional[date] = None
    estudiante_id: Optional[int] = None
    curso_id: Optional[int] = None
    estado: Optional[EstadoMatriculaEnum] = None

    class Config:
        json_schema_extra = {
            "example": {
                "estado": "SUSPENDIDO"
            }
        }


class MatriculaRead(BaseModel):
    """Schema para leer una matrícula"""
    id: int
    fecha: date
    estudiante_id: int
    curso_id: int
    estado: str

    class Config:
        from_attributes = True
