from pydantic import BaseModel, Field
from typing import Optional


class AsignaturaCreate(BaseModel):
    """Schema para crear una asignatura"""
    nombre: str = Field(..., min_length=1, max_length=100)
    descripcion: Optional[str] = None
    curso_id: int
    docente_id: Optional[int] = None

    class Config:
        json_schema_extra = {
            "example": {
                "nombre": "Matemática",
                "descripcion": "Curso de matemática básica",
                "curso_id": 1,
                "docente_id": 1
            }
        }


class AsignaturaUpdate(BaseModel):
    """Schema para actualizar una asignatura"""
    nombre: Optional[str] = Field(None, min_length=1, max_length=100)
    descripcion: Optional[str] = None
    curso_id: Optional[int] = None
    docente_id: Optional[int] = None

    class Config:
        json_schema_extra = {
            "example": {
                "nombre": "Matemática Avanzada",
                "descripcion": "Curso de matemática avanzada"
            }
        }


class AsignaturaRead(BaseModel):
    """Schema para leer una asignatura"""
    id: int
    nombre: str
    descripcion: Optional[str]
    curso_id: int
    docente_id: Optional[int]

    class Config:
        from_attributes = True
