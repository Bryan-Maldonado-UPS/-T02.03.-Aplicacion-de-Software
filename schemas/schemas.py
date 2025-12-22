"""
Schemas Pydantic para validación de entrada y salida
"""
from pydantic import BaseModel, Field, EmailStr, field_validator
from datetime import date, datetime
from typing import Optional
from enum import Enum

# ============================================================================
# ENUMS
# ============================================================================

class EstadoMatriculaEnum(str, Enum):
    REGISTRADO = "REGISTRADO"
    MATRICULADO = "MATRICULADO"
    ACTIVO = "ACTIVO"
    SUSPENDIDO = "SUSPENDIDO"
    RETIRADO = "RETIRADO"
    GRADUADO = "GRADUADO"


class EstadoAsistenciaEnum(str, Enum):
    PRESENTE = "PRESENTE"
    AUSENTE = "AUSENTE"
    ATRASO = "ATRASO"
    JUSTIFICADO = "JUSTIFICADO"


# ============================================================================
# REPRESENTANTE SCHEMAS
# ============================================================================

class RepresentanteCreate(BaseModel):
    """Schema para crear representante"""
    nombre: str = Field(..., min_length=1, max_length=100, description="Nombre del representante")
    telefono: str = Field(..., min_length=5, max_length=20, description="Teléfono del representante")

    @field_validator('nombre')
    @classmethod
    def nombre_no_vacio(cls, v):
        if not v or not v.strip():
            raise ValueError('El nombre no puede estar vacío')
        return v.strip()


class RepresentanteRead(RepresentanteCreate):
    """Schema para leer representante"""
    id: int = Field(..., description="ID del representante")

    class Config:
        from_attributes = True


# ============================================================================
# DOCENTE SCHEMAS
# ============================================================================

class DocenteCreate(BaseModel):
    """Schema para crear docente"""
    nombre: str = Field(..., min_length=1, max_length=100, description="Nombre del docente")
    apellido: str = Field(..., min_length=1, max_length=100, description="Apellido del docente")
    titulo: Optional[str] = Field(None, max_length=100, description="Título profesional")
    correo: EmailStr = Field(..., description="Correo electrónico del docente")


class DocenteRead(DocenteCreate):
    """Schema para leer docente"""
    id: int = Field(..., description="ID del docente")

    class Config:
        from_attributes = True


# ============================================================================
# CURSO SCHEMAS
# ============================================================================

class CursoCreate(BaseModel):
    """Schema para crear curso"""
    nombre: str = Field(..., min_length=1, max_length=50, description="Nombre del curso")
    nivel: str = Field(..., min_length=1, max_length=50, description="Nivel del curso")


class CursoRead(CursoCreate):
    """Schema para leer curso"""
    id: int = Field(..., description="ID del curso")

    class Config:
        from_attributes = True


# ============================================================================
# ASIGNATURA SCHEMAS
# ============================================================================

class AsignaturaCreate(BaseModel):
    """Schema para crear asignatura"""
    nombre: str = Field(..., min_length=1, max_length=100, description="Nombre de la asignatura")
    descripcion: Optional[str] = Field(None, description="Descripción de la asignatura")
    curso_id: int = Field(..., gt=0, description="ID del curso")
    docente_id: Optional[int] = Field(None, gt=0, description="ID del docente")


class AsignaturaRead(AsignaturaCreate):
    """Schema para leer asignatura"""
    id: int = Field(..., description="ID de la asignatura")

    class Config:
        from_attributes = True


# ============================================================================
# ESTUDIANTE SCHEMAS
# ============================================================================

class EstudianteCreate(BaseModel):
    """Schema para crear estudiante"""
    nombre: str = Field(..., min_length=1, max_length=100, description="Nombre del estudiante")
    apellido: str = Field(..., min_length=1, max_length=100, description="Apellido del estudiante")
    cedula: str = Field(..., min_length=5, max_length=20, description="Cédula única del estudiante")
    fecha_nacimiento: date = Field(..., description="Fecha de nacimiento (YYYY-MM-DD)")
    correo: Optional[EmailStr] = Field(None, description="Correo del estudiante")
    representante_id: int = Field(..., gt=0, description="ID del representante")

    @field_validator('cedula')
    @classmethod
    def cedula_no_vacio(cls, v):
        if not v or not v.strip():
            raise ValueError('La cédula no puede estar vacía')
        return v.strip()


class EstudianteRead(EstudianteCreate):
    """Schema para leer estudiante"""
    id: int = Field(..., description="ID del estudiante")

    class Config:
        from_attributes = True


class EstudianteUpdate(BaseModel):
    """Schema para actualizar estudiante"""
    nombre: Optional[str] = Field(None, min_length=1, max_length=100)
    apellido: Optional[str] = Field(None, min_length=1, max_length=100)
    correo: Optional[EmailStr] = None

    class Config:
        from_attributes = True


# ============================================================================
# MATRICULA SCHEMAS
# ============================================================================

class MatriculaCreate(BaseModel):
    """Schema para crear matrícula"""
    fecha: Optional[date] = Field(default_factory=date.today, description="Fecha de matrícula")
    estudiante_id: int = Field(..., gt=0, description="ID del estudiante")
    curso_id: int = Field(..., gt=0, description="ID del curso")
    estado: EstadoMatriculaEnum = Field(EstadoMatriculaEnum.REGISTRADO, description="Estado de la matrícula")


class MatriculaRead(MatriculaCreate):
    """Schema para leer matrícula"""
    id: int = Field(..., description="ID de la matrícula")

    class Config:
        from_attributes = True


class MatriculaUpdate(BaseModel):
    """Schema para actualizar estado de matrícula"""
    estado: EstadoMatriculaEnum = Field(..., description="Nuevo estado de la matrícula")

    class Config:
        from_attributes = True


# ============================================================================
# CALIFICACION SCHEMAS
# ============================================================================

class CalificacionCreate(BaseModel):
    """Schema para crear calificación"""
    nota: float = Field(..., ge=0, le=10, description="Nota (0-10)")
    quimestre: int = Field(..., ge=1, le=3, description="Quimestre (1-3)")
    matricula_id: int = Field(..., gt=0, description="ID de la matrícula")
    asignatura_id: int = Field(..., gt=0, description="ID de la asignatura")


class CalificacionRead(CalificacionCreate):
    """Schema para leer calificación"""
    id: int = Field(..., description="ID de la calificación")

    class Config:
        from_attributes = True


class CalificacionUpdate(BaseModel):
    """Schema para actualizar calificación"""
    nota: float = Field(..., ge=0, le=10, description="Nueva nota (0-10)")

    class Config:
        from_attributes = True


# ============================================================================
# ASISTENCIA SCHEMAS
# ============================================================================

class AsistenciaCreate(BaseModel):
    """Schema para crear registro de asistencia"""
    fecha: Optional[date] = Field(default_factory=date.today, description="Fecha de asistencia")
    estado: EstadoAsistenciaEnum = Field(..., description="Estado de asistencia")
    matricula_id: int = Field(..., gt=0, description="ID de la matrícula")
    asignatura_id: int = Field(..., gt=0, description="ID de la asignatura")


class AsistenciaRead(AsistenciaCreate):
    """Schema para leer asistencia"""
    id: int = Field(..., description="ID del registro de asistencia")

    class Config:
        from_attributes = True


class AsistenciaUpdate(BaseModel):
    """Schema para actualizar asistencia"""
    estado: EstadoAsistenciaEnum = Field(..., description="Nuevo estado de asistencia")

    class Config:
        from_attributes = True


# ============================================================================
# RESPONSE SCHEMAS
# ============================================================================

class ErrorResponse(BaseModel):
    """Schema para respuestas de error"""
    detail: str = Field(..., description="Descripción del error")
    status_code: int = Field(..., description="Código HTTP del error")


class SuccessResponse(BaseModel):
    """Schema para respuestas exitosas"""
    message: str = Field(..., description="Mensaje de éxito")
    data: Optional[dict] = Field(None, description="Datos de la respuesta")
