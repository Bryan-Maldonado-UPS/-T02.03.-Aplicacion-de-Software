from pydantic import BaseModel, Field
from typing import Optional


class DocenteCreate(BaseModel):
    """Schema para crear un docente"""
    nombre: str = Field(..., min_length=1, max_length=100)
    apellido: str = Field(..., min_length=1, max_length=100)
    titulo: Optional[str] = Field(None, max_length=100)
    correo: str = Field(..., min_length=5, max_length=100)

    class Config:
        json_schema_extra = {
            "example": {
                "nombre": "David",
                "apellido": "Acosta",
                "titulo": "Licenciado en Educación Matemática",
                "correo": "david.acosta@escuela.edu"
            }
        }


class DocenteUpdate(BaseModel):
    """Schema para actualizar un docente"""
    nombre: Optional[str] = Field(None, min_length=1, max_length=100)
    apellido: Optional[str] = Field(None, min_length=1, max_length=100)
    titulo: Optional[str] = Field(None, max_length=100)
    correo: Optional[str] = Field(None, min_length=5, max_length=100)

    class Config:
        json_schema_extra = {
            "example": {
                "nombre": "David Actualizado",
                "correo": "david.nuevo@escuela.edu"
            }
        }


class DocenteRead(BaseModel):
    """Schema para leer un docente"""
    id: int
    nombre: str
    apellido: str
    titulo: Optional[str]
    correo: str

    class Config:
        from_attributes = True
