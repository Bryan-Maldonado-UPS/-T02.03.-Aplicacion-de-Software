"""
Modelo de Asistencia
"""
from sqlalchemy import Column, Integer, Date, ForeignKey, Enum
from sqlalchemy.orm import relationship
from datetime import date
from config.database import Base
from models.enums import EstadoAsistencia


class Asistencia(Base):
    """
    Modelo para la tabla asistencias.
    Representa el registro de asistencia de un estudiante en una asignatura.
    """
    __tablename__ = "asistencias"

    id = Column(Integer, primary_key=True, index=True)
    fecha = Column(Date, default=date.today, nullable=False)
    estado = Column(Enum(EstadoAsistencia), nullable=False)
    matricula_id = Column(Integer, ForeignKey("matriculas.id"), nullable=False)
    asignatura_id = Column(Integer, ForeignKey("asignaturas.id"), nullable=False)

    # Relaciones
    matricula = relationship("Matricula", back_populates="asistencias")
    asignatura = relationship("Asignatura", back_populates="asistencias")

    def __repr__(self):
        return f"<Asistencia(id={self.id}, fecha='{self.fecha}', estado='{self.estado}', matricula_id={self.matricula_id})>"
