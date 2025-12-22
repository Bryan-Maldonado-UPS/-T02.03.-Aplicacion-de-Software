"""
Modelo de Matrícula
"""
from sqlalchemy import Column, Integer, Date, ForeignKey, Enum
from sqlalchemy.orm import relationship
from datetime import date
from config.database import Base
from models.enums import EstadoMatricula


class Matricula(Base):
    """
    Modelo para la tabla matriculas.
    Representa la inscripción de un estudiante en un curso.
    """
    __tablename__ = "matriculas"

    id = Column(Integer, primary_key=True, index=True)
    fecha = Column(Date, default=date.today, nullable=False)
    estudiante_id = Column(Integer, ForeignKey("estudiantes.id"), nullable=False)
    curso_id = Column(Integer, ForeignKey("cursos.id"), nullable=False)
    estado = Column(
        Enum(EstadoMatricula),
        default=EstadoMatricula.REGISTRADO,
        nullable=False
    )

    # Relaciones
    estudiante = relationship("Estudiante", back_populates="matriculas")
    curso = relationship("Curso", back_populates="matriculas")
    calificaciones = relationship("Calificacion", back_populates="matricula", cascade="all, delete-orphan")
    asistencias = relationship("Asistencia", back_populates="matricula", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Matricula(id={self.id}, estudiante_id={self.estudiante_id}, curso_id={self.curso_id}, estado='{self.estado}')>"
