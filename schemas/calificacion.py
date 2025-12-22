from pydantic import BaseModel, Field
from typing import Optional


class CalificacionCreate(BaseModel):
    """Schema para crear una calificación"""
    nota: float = Field(..., ge=0, le=10)
    quimestre: int = Field(..., ge=1, le=3)
    matricula_id: int
    asignatura_id: int

    class Config:
        json_schema_extra = {
            "example": {
                "nota": 8.5,
                "quimestre": 1,
                "matricula_id": 1,
                "asignatura_id": 1
            }
        }


class CalificacionUpdate(BaseModel):
    """Schema para actualizar una calificación"""
    nota: Optional[float] = Field(None, ge=0, le=10)
    quimestre: Optional[int] = Field(None, ge=1, le=3)
    matricula_id: Optional[int] = None
    asignatura_id: Optional[int] = None

    class Config:
        json_schema_extra = {
            "example": {
                "nota": 9.0,
                "quimestre": 2
            }
        }


class CalificacionRead(BaseModel):
    """Schema para leer una calificación"""
    id: int
    nota: float
    quimestre: int
    matricula_id: int
    asignatura_id: int

    class Config:
        from_attributes = True
