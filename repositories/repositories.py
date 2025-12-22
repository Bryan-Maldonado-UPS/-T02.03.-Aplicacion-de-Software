"""
Repositorios para todas las entidades
CRUD básico sin lógica de negocio
"""
from typing import Optional, List
from sqlalchemy.orm import Session
from repositories.base import BaseRepository
from models import (
    Representante, Estudiante, Docente, Curso, Asignatura,
    Matricula, Asistencia, Calificacion
)


class RepresentanteRepository(BaseRepository[Representante]):
    """Repositorio para Representantes"""
    
    def __init__(self, db: Session):
        super().__init__(db, Representante)

    def get_by_telefono(self, telefono: str) -> Optional[Representante]:
        """Busca representante por teléfono"""
        return self.db.query(Representante).filter(
            Representante.telefono == telefono
        ).first()


class EstudianteRepository(BaseRepository[Estudiante]):
    """Repositorio para Estudiantes"""
    
    def __init__(self, db: Session):
        super().__init__(db, Estudiante)

    def get_by_cedula(self, cedula: str) -> Optional[Estudiante]:
        """Busca estudiante por cédula (ÚNICA)"""
        return self.db.query(Estudiante).filter(
            Estudiante.cedula == cedula
        ).first()

    def get_by_correo(self, correo: str) -> Optional[Estudiante]:
        """Busca estudiante por correo"""
        return self.db.query(Estudiante).filter(
            Estudiante.correo == correo
        ).first()

    def get_by_representante(self, representante_id: int) -> List[Estudiante]:
        """Obtiene todos los estudiantes de un representante"""
        return self.db.query(Estudiante).filter(
            Estudiante.representante_id == representante_id
        ).all()


class DocenteRepository(BaseRepository[Docente]):
    """Repositorio para Docentes"""
    
    def __init__(self, db: Session):
        super().__init__(db, Docente)

    def get_by_correo(self, correo: str) -> Optional[Docente]:
        """Busca docente por correo (ÚNICA)"""
        return self.db.query(Docente).filter(
            Docente.correo == correo
        ).first()


class CursoRepository(BaseRepository[Curso]):
    """Repositorio para Cursos"""
    
    def __init__(self, db: Session):
        super().__init__(db, Curso)

    def get_by_nombre(self, nombre: str) -> Optional[Curso]:
        """Busca curso por nombre"""
        return self.db.query(Curso).filter(
            Curso.nombre == nombre
        ).first()

    def get_by_nivel(self, nivel: str) -> List[Curso]:
        """Obtiene todos los cursos de un nivel"""
        return self.db.query(Curso).filter(
            Curso.nivel == nivel
        ).all()


class AsignaturaRepository(BaseRepository[Asignatura]):
    """Repositorio para Asignaturas"""
    
    def __init__(self, db: Session):
        super().__init__(db, Asignatura)

    def get_by_curso(self, curso_id: int) -> List[Asignatura]:
        """Obtiene todas las asignaturas de un curso"""
        return self.db.query(Asignatura).filter(
            Asignatura.curso_id == curso_id
        ).all()

    def get_by_docente(self, docente_id: int) -> List[Asignatura]:
        """Obtiene todas las asignaturas de un docente"""
        return self.db.query(Asignatura).filter(
            Asignatura.docente_id == docente_id
        ).all()


class MatriculaRepository(BaseRepository[Matricula]):
    """Repositorio para Matrículas"""
    
    def __init__(self, db: Session):
        super().__init__(db, Matricula)

    def get_by_estudiante(self, estudiante_id: int) -> List[Matricula]:
        """Obtiene todas las matrículas de un estudiante"""
        return self.db.query(Matricula).filter(
            Matricula.estudiante_id == estudiante_id
        ).all()

    def get_by_curso(self, curso_id: int) -> List[Matricula]:
        """Obtiene todas las matrículas de un curso"""
        return self.db.query(Matricula).filter(
            Matricula.curso_id == curso_id
        ).all()

    def get_by_estado(self, estado: str) -> List[Matricula]:
        """Obtiene matrículas por estado"""
        return self.db.query(Matricula).filter(
            Matricula.estado == estado
        ).all()

    def get_estudiante_en_curso(self, estudiante_id: int, curso_id: int) -> Optional[Matricula]:
        """Busca si un estudiante está matriculado en un curso"""
        return self.db.query(Matricula).filter(
            Matricula.estudiante_id == estudiante_id,
            Matricula.curso_id == curso_id
        ).first()


class AsistenciaRepository(BaseRepository[Asistencia]):
    """Repositorio para Asistencias"""
    
    def __init__(self, db: Session):
        super().__init__(db, Asistencia)

    def get_by_matricula(self, matricula_id: int) -> List[Asistencia]:
        """Obtiene todas las asistencias de una matrícula"""
        return self.db.query(Asistencia).filter(
            Asistencia.matricula_id == matricula_id
        ).all()

    def get_by_asignatura(self, asignatura_id: int) -> List[Asistencia]:
        """Obtiene todas las asistencias de una asignatura"""
        return self.db.query(Asistencia).filter(
            Asistencia.asignatura_id == asignatura_id
        ).all()

    def get_by_estado(self, estado: str) -> List[Asistencia]:
        """Obtiene asistencias por estado"""
        return self.db.query(Asistencia).filter(
            Asistencia.estado == estado
        ).all()


class CalificacionRepository(BaseRepository[Calificacion]):
    """Repositorio para Calificaciones"""
    
    def __init__(self, db: Session):
        super().__init__(db, Calificacion)

    def get_by_matricula(self, matricula_id: int) -> List[Calificacion]:
        """Obtiene todas las calificaciones de una matrícula"""
        return self.db.query(Calificacion).filter(
            Calificacion.matricula_id == matricula_id
        ).all()

    def get_by_asignatura(self, asignatura_id: int) -> List[Calificacion]:
        """Obtiene todas las calificaciones de una asignatura"""
        return self.db.query(Calificacion).filter(
            Calificacion.asignatura_id == asignatura_id
        ).all()

    def get_by_quimestre(self, quimestre: int) -> List[Calificacion]:
        """Obtiene calificaciones de un quimestre"""
        return self.db.query(Calificacion).filter(
            Calificacion.quimestre == quimestre
        ).all()

    def get_promedio_estudiante(self, matricula_id: int) -> float:
        """Calcula el promedio de calificaciones de un estudiante"""
        from sqlalchemy import func
        result = self.db.query(func.avg(Calificacion.nota)).filter(
            Calificacion.matricula_id == matricula_id
        ).scalar()
        return float(result) if result else 0.0
