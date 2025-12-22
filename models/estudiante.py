"""
Modelo de Estudiante
"""
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base


class Estudiante(Base):
    """
    Modelo para la tabla estudiantes.
    Representa a los alumnos de la institución educativa.
    """
    __tablename__ = "estudiantes"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    cedula = Column(String(20), unique=True, nullable=False, index=True)
    fecha_nacimiento = Column(Date, nullable=False)
    correo = Column(String(100))
    representante_id = Column(Integer, ForeignKey("representantes.id"))

    # Relaciones
    representante = relationship("Representante", foreign_keys=[representante_id])
    matriculas = relationship("Matricula", back_populates="estudiante", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Estudiante(id={self.id}, nombre='{self.nombre} {self.apellido}', cedula='{self.cedula}')>"
