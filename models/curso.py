"""
Modelo de Curso
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from config.database import Base


class Curso(Base):
    """
    Modelo para la tabla cursos.
    Representa los diferentes niveles y secciones de los cursos.
    """
    __tablename__ = "cursos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), nullable=False)
    nivel = Column(String(50), nullable=False)

    # Relaciones
    asignaturas = relationship("Asignatura", back_populates="curso", cascade="all, delete-orphan")
    matriculas = relationship("Matricula", back_populates="curso", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Curso(id={self.id}, nombre='{self.nombre}', nivel='{self.nivel}')>"
