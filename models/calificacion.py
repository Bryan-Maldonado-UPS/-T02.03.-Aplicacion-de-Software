"""
Modelo de Calificación
"""
from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base


class Calificacion(Base):
    """
    Modelo para la tabla calificaciones.
    Representa las calificaciones de un estudiante en una asignatura.
    """
    __tablename__ = "calificaciones"

    id = Column(Integer, primary_key=True, index=True)
    nota = Column(Float, nullable=False)  # Rango 0-10
    quimestre = Column(Integer, nullable=False)
    matricula_id = Column(Integer, ForeignKey("matriculas.id"), nullable=False)
    asignatura_id = Column(Integer, ForeignKey("asignaturas.id"), nullable=False)

    # Relaciones
    matricula = relationship("Matricula", back_populates="calificaciones")
    asignatura = relationship("Asignatura", back_populates="calificaciones")

    def __repr__(self):
        return f"<Calificacion(id={self.id}, nota={self.nota}, quimestre={self.quimestre}, matricula_id={self.matricula_id})>"
