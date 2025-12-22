from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class RepresentanteCreate(BaseModel):
    """Schema para crear un representante"""
    nombre: str = Field(..., min_length=1, max_length=100)
    telefono: str = Field(..., min_length=5, max_length=20)

    class Config:
        json_schema_extra = {
            "example": {
                "nombre": "Carlos García",
                "telefono": "+593-2-2123456"
            }
        }


class RepresentanteUpdate(BaseModel):
    """Schema para actualizar un representante"""
    nombre: Optional[str] = Field(None, min_length=1, max_length=100)
    telefono: Optional[str] = Field(None, min_length=5, max_length=20)

    class Config:
        json_schema_extra = {
            "example": {
                "nombre": "Carlos García Actualizado",
                "telefono": "+593-2-2999999"
            }
        }


class RepresentanteRead(BaseModel):
    """Schema para leer un representante"""
    id: int
    nombre: str
    telefono: str

    class Config:
        from_attributes = True
