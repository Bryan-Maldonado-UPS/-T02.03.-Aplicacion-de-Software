"""
Modelo de Representante
"""
from sqlalchemy import Column, Integer, String
from config.database import Base


class Representante(Base):
    """
    Modelo para la tabla representantes.
    Representa a los padres/tutores de los estudiantes.
    """
    __tablename__ = "representantes"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    telefono = Column(String(20), nullable=False)

    def __repr__(self):
        return f"<Representante(id={self.id}, nombre='{self.nombre}')>"
