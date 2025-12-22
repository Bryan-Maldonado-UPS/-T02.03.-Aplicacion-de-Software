from pydantic import BaseModel, Field
from typing import Optional
from datetime import date
from enum import Enum


class EstadoAsistenciaEnum(str, Enum):
    """Estados válidos para la asistencia"""
    PRESENTE = "PRESENTE"
    AUSENTE = "AUSENTE"
    ATRASO = "ATRASO"
    JUSTIFICADO = "JUSTIFICADO"


class AsistenciaCreate(BaseModel):
    """Schema para crear una asistencia"""
    fecha: Optional[date] = None
    estado: EstadoAsistenciaEnum
    matricula_id: int
    asignatura_id: int

    class Config:
        json_schema_extra = {
            "example": {
                "fecha": "2024-12-15",
                "estado": "PRESENTE",
                "matricula_id": 1,
                "asignatura_id": 1
            }
        }


class AsistenciaUpdate(BaseModel):
    """Schema para actualizar una asistencia"""
    fecha: Optional[date] = None
    estado: Optional[EstadoAsistenciaEnum] = None
    matricula_id: Optional[int] = None
    asignatura_id: Optional[int] = None

    class Config:
        json_schema_extra = {
            "example": {
                "estado": "ATRASO"
            }
        }


class AsistenciaRead(BaseModel):
    """Schema para leer una asistencia"""
    id: int
    fecha: date
    estado: str
    matricula_id: int
    asignatura_id: int

    class Config:
        from_attributes = True
