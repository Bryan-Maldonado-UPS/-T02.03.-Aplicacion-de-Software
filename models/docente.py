"""
Modelo de Docente
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from config.database import Base


class Docente(Base):
    """
    Modelo para la tabla docentes.
    Representa a los profesores de la institución.
    """
    __tablename__ = "docentes"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    titulo = Column(String(100))
    correo = Column(String(100), unique=True, nullable=False, index=True)

    # Relaciones
    asignaturas = relationship("Asignatura", back_populates="docente", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Docente(id={self.id}, nombre='{self.nombre} {self.apellido}', titulo='{self.titulo}')>"
