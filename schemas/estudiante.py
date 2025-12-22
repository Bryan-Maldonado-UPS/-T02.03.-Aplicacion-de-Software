from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from datetime import date


class EstudianteCreate(BaseModel):
    """Schema para crear un estudiante"""
    nombre: str = Field(..., min_length=1, max_length=100)
    apellido: str = Field(..., min_length=1, max_length=100)
    cedula: str = Field(..., min_length=5, max_length=20)
    fecha_nacimiento: date
    correo: Optional[str] = None
    representante_id: int

    class Config:
        json_schema_extra = {
            "example": {
                "nombre": "Juan",
                "apellido": "Rodríguez",
                "cedula": "1001234567",
                "fecha_nacimiento": "2015-03-21",
                "correo": "juan.rodriguez@estudiante.edu",
                "representante_id": 1
            }
        }


class EstudianteUpdate(BaseModel):
    """Schema para actualizar un estudiante"""
    nombre: Optional[str] = Field(None, min_length=1, max_length=100)
    apellido: Optional[str] = Field(None, min_length=1, max_length=100)
    cedula: Optional[str] = Field(None, min_length=5, max_length=20)
    fecha_nacimiento: Optional[date] = None
    correo: Optional[str] = None
    representante_id: Optional[int] = None

    class Config:
        json_schema_extra = {
            "example": {
                "nombre": "Juan Actualizado",
                "correo": "juan.nuevo@estudiante.edu"
            }
        }


class EstudianteRead(BaseModel):
    """Schema para leer un estudiante"""
    id: int
    nombre: str
    apellido: str
    cedula: str
    fecha_nacimiento: date
    correo: Optional[str]
    representante_id: int

    class Config:
        from_attributes = True
