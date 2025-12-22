from pydantic import BaseModel, Field
from typing import Optional


class CursoCreate(BaseModel):
    """Schema para crear un curso"""
    nombre: str = Field(..., min_length=1, max_length=50)
    nivel: str = Field(..., min_length=1, max_length=50)

    class Config:
        json_schema_extra = {
            "example": {
                "nombre": "Primero A",
                "nivel": "Primero"
            }
        }


class CursoUpdate(BaseModel):
    """Schema para actualizar un curso"""
    nombre: Optional[str] = Field(None, min_length=1, max_length=50)
    nivel: Optional[str] = Field(None, min_length=1, max_length=50)

    class Config:
        json_schema_extra = {
            "example": {
                "nombre": "Primero A Actualizado",
                "nivel": "Primero"
            }
        }


class CursoRead(BaseModel):
    """Schema para leer un curso"""
    id: int
    nombre: str
    nivel: str

    class Config:
        from_attributes = True
