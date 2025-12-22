"""
Modelo de Asignatura
"""
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base


class Asignatura(Base):
    """
    Modelo para la tabla asignaturas.
    Representa las materias/cursos que se imparten en la institución.
    """
    __tablename__ = "asignaturas"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(Text)
    curso_id = Column(Integer, ForeignKey("cursos.id"), nullable=False)
    docente_id = Column(Integer, ForeignKey("docentes.id"))

    # Relaciones
    curso = relationship("Curso", back_populates="asignaturas")
    docente = relationship("Docente", back_populates="asignaturas")
    calificaciones = relationship("Calificacion", back_populates="asignatura", cascade="all, delete-orphan")
    asistencias = relationship("Asistencia", back_populates="asignatura", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Asignatura(id={self.id}, nombre='{self.nombre}', curso_id={self.curso_id})>"
