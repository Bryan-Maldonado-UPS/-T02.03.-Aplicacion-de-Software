"""
Servicios con lógica de negocio
Los servicios utilizan repositorios y contienen validaciones
"""
from typing import Optional, List
from datetime import date
from sqlalchemy.orm import Session
from repositories.repositories import (
    RepresentanteRepository, EstudianteRepository, DocenteRepository,
    CursoRepository, AsignaturaRepository, MatriculaRepository,
    AsistenciaRepository, CalificacionRepository
)
from models import EstadoMatricula, EstadoAsistencia


class RepresentanteService:
    """Servicio para Representantes con lógica de negocio"""
    
    def __init__(self, db: Session):
        self.repo = RepresentanteRepository(db)
        self.db = db

    def crear_representante(self, nombre: str, telefono: str):
        """
        Crea un nuevo representante.
        
        Validaciones:
        - Nombre no vacío
        - Teléfono no vacío
        """
        if not nombre or not nombre.strip():
            raise ValueError("El nombre no puede estar vacío")
        if not telefono or not telefono.strip():
            raise ValueError("El teléfono no puede estar vacío")
        
        return self.repo.create({
            "nombre": nombre.strip(),
            "telefono": telefono.strip()
        })

    def obtener_representante(self, id: int):
        """Obtiene un representante por ID"""
        rep = self.repo.read(id)
        if not rep:
            raise ValueError(f"Representante con ID {id} no encontrado")
        return rep

    def listar_representantes(self, skip: int = 0, limit: int = 100):
        """Lista todos los representantes"""
        return self.repo.read_all(skip, limit)

    def actualizar_representante(self, id: int, nombre: str = None, telefono: str = None):
        """Actualiza un representante"""
        if not self.repo.read(id):
            raise ValueError(f"Representante con ID {id} no encontrado")
        
        datos = {}
        if nombre:
            datos["nombre"] = nombre.strip()
        if telefono:
            datos["telefono"] = telefono.strip()
        
        if not datos:
            raise ValueError("Debe proporcionar al menos un campo para actualizar")
        
        return self.repo.update(id, datos)

    def eliminar_representante(self, id: int):
        """Elimina un representante"""
        if not self.repo.delete(id):
            raise ValueError(f"Representante con ID {id} no encontrado")
        return True


class EstudianteService:
    """Servicio para Estudiantes con lógica de negocio"""
    
    def __init__(self, db: Session):
        self.repo = EstudianteRepository(db)
        self.rep_repo = RepresentanteRepository(db)
        self.db = db

    def crear_estudiante(self, nombre: str, apellido: str, cedula: str, 
                         fecha_nacimiento: date, correo: str = None, representante_id: int = None):
        """
        Crea un nuevo estudiante.
        
        Validaciones:
        - Cédula única
        - Cédula formato válido (20 caracteres)
        - Representante existe (si se proporciona)
        - Edad mínima (debe ser > 5 años)
        """
        if self.repo.get_by_cedula(cedula):
            raise ValueError(f"Ya existe un estudiante con cédula {cedula}")
        
        if not cedula or len(cedula) > 20:
            raise ValueError("Cédula inválida (máx 20 caracteres)")
        
        if representante_id:
            if not self.rep_repo.read(representante_id):
                raise ValueError(f"Representante con ID {representante_id} no existe")
        
        # Validar edad mínima
        edad = (date.today() - fecha_nacimiento).days // 365
        if edad < 5:
            raise ValueError("El estudiante debe tener al menos 5 años de edad")
        
        return self.repo.create({
            "nombre": nombre.strip(),
            "apellido": apellido.strip(),
            "cedula": cedula,
            "fecha_nacimiento": fecha_nacimiento,
            "correo": correo,
            "representante_id": representante_id
        })

    def obtener_estudiante(self, id: int):
        """Obtiene un estudiante por ID"""
        est = self.repo.read(id)
        if not est:
            raise ValueError(f"Estudiante con ID {id} no encontrado")
        return est

    def obtener_por_cedula(self, cedula: str):
        """Obtiene un estudiante por cédula"""
        est = self.repo.get_by_cedula(cedula)
        if not est:
            raise ValueError(f"Estudiante con cédula {cedula} no encontrado")
        return est

    def listar_estudiantes(self, skip: int = 0, limit: int = 100):
        """Lista todos los estudiantes"""
        return self.repo.read_all(skip, limit)

    def actualizar_estudiante(self, id: int, **kwargs):
        """Actualiza un estudiante"""
        if not self.repo.read(id):
            raise ValueError(f"Estudiante con ID {id} no encontrado")
        
        # Si cambia cédula, validar que no exista
        if "cedula" in kwargs:
            existente = self.repo.get_by_cedula(kwargs["cedula"])
            if existente and existente.id != id:
                raise ValueError(f"Ya existe un estudiante con cédula {kwargs['cedula']}")
        
        return self.repo.update(id, kwargs)

    def eliminar_estudiante(self, id: int):
        """Elimina un estudiante"""
        if not self.repo.delete(id):
            raise ValueError(f"Estudiante con ID {id} no encontrado")
        return True


class DocenteService:
    """Servicio para Docentes con lógica de negocio"""
    
    def __init__(self, db: Session):
        self.repo = DocenteRepository(db)
        self.db = db

    def crear_docente(self, nombre: str, apellido: str, correo: str, titulo: str = None):
        """
        Crea un nuevo docente.
        
        Validaciones:
        - Correo único
        - Correo formato válido
        """
        if self.repo.get_by_correo(correo):
            raise ValueError(f"Ya existe un docente con correo {correo}")
        
        if not self._validar_correo(correo):
            raise ValueError("Correo inválido")
        
        return self.repo.create({
            "nombre": nombre.strip(),
            "apellido": apellido.strip(),
            "correo": correo.lower(),
            "titulo": titulo
        })

    def obtener_docente(self, id: int):
        """Obtiene un docente por ID"""
        doc = self.repo.read(id)
        if not doc:
            raise ValueError(f"Docente con ID {id} no encontrado")
        return doc

    def listar_docentes(self, skip: int = 0, limit: int = 100):
        """Lista todos los docentes"""
        return self.repo.read_all(skip, limit)

    def actualizar_docente(self, id: int, **kwargs):
        """Actualiza un docente"""
        if not self.repo.read(id):
            raise ValueError(f"Docente con ID {id} no encontrado")
        
        if "correo" in kwargs:
            existente = self.repo.get_by_correo(kwargs["correo"])
            if existente and existente.id != id:
                raise ValueError(f"Ya existe un docente con correo {kwargs['correo']}")
        
        return self.repo.update(id, kwargs)

    def eliminar_docente(self, id: int):
        """Elimina un docente"""
        if not self.repo.delete(id):
            raise ValueError(f"Docente con ID {id} no encontrado")
        return True

    @staticmethod
    def _validar_correo(correo: str) -> bool:
        """Valida formato de correo básico"""
        return "@" in correo and "." in correo


class CursoService:
    """Servicio para Cursos"""
    
    def __init__(self, db: Session):
        self.repo = CursoRepository(db)
        self.db = db

    def crear_curso(self, nombre: str, nivel: str):
        """Crea un nuevo curso"""
        return self.repo.create({
            "nombre": nombre.strip(),
            "nivel": nivel.strip()
        })

    def obtener_curso(self, id: int):
        """Obtiene un curso por ID"""
        curso = self.repo.read(id)
        if not curso:
            raise ValueError(f"Curso con ID {id} no encontrado")
        return curso

    def listar_cursos(self, skip: int = 0, limit: int = 100):
        """Lista todos los cursos"""
        return self.repo.read_all(skip, limit)

    def actualizar_curso(self, id: int, **kwargs):
        """Actualiza un curso"""
        if not self.repo.read(id):
            raise ValueError(f"Curso con ID {id} no encontrado")
        return self.repo.update(id, kwargs)

    def eliminar_curso(self, id: int):
        """Elimina un curso"""
        if not self.repo.delete(id):
            raise ValueError(f"Curso con ID {id} no encontrado")
        return True


class AsignaturaService:
    """Servicio para Asignaturas"""
    
    def __init__(self, db: Session):
        self.repo = AsignaturaRepository(db)
        self.curso_repo = CursoRepository(db)
        self.docente_repo = DocenteRepository(db)
        self.db = db

    def crear_asignatura(self, nombre: str, curso_id: int, descripcion: str = None, docente_id: int = None):
        """
        Crea una nueva asignatura.
        
        Validaciones:
        - Curso existe
        - Docente existe (si se proporciona)
        """
        if not self.curso_repo.read(curso_id):
            raise ValueError(f"Curso con ID {curso_id} no existe")
        
        if docente_id and not self.docente_repo.read(docente_id):
            raise ValueError(f"Docente con ID {docente_id} no existe")
        
        return self.repo.create({
            "nombre": nombre.strip(),
            "descripcion": descripcion,
            "curso_id": curso_id,
            "docente_id": docente_id
        })

    def obtener_asignatura(self, id: int):
        """Obtiene una asignatura por ID"""
        asig = self.repo.read(id)
        if not asig:
            raise ValueError(f"Asignatura con ID {id} no encontrada")
        return asig

    def listar_asignaturas(self, skip: int = 0, limit: int = 100):
        """Lista todas las asignaturas"""
        return self.repo.read_all(skip, limit)

    def obtener_por_curso(self, curso_id: int):
        """Obtiene asignaturas de un curso"""
        return self.repo.get_by_curso(curso_id)

    def actualizar_asignatura(self, id: int, **kwargs):
        """Actualiza una asignatura"""
        if not self.repo.read(id):
            raise ValueError(f"Asignatura con ID {id} no encontrada")
        return self.repo.update(id, kwargs)

    def eliminar_asignatura(self, id: int):
        """Elimina una asignatura"""
        if not self.repo.delete(id):
            raise ValueError(f"Asignatura con ID {id} no encontrada")
        return True


class MatriculaService:
    """Servicio para Matrículas con lógica de negocio"""
    
    def __init__(self, db: Session):
        self.repo = MatriculaRepository(db)
        self.est_repo = EstudianteRepository(db)
        self.curso_repo = CursoRepository(db)
        self.db = db

    def crear_matricula(self, estudiante_id: int, curso_id: int, fecha: date = None, estado: str = None):
        """
        Crea una nueva matrícula.
        
        Validaciones:
        - Estudiante existe
        - Curso existe
        - Estudiante no está duplicado en el curso
        """
        if not self.est_repo.read(estudiante_id):
            raise ValueError(f"Estudiante con ID {estudiante_id} no existe")
        
        if not self.curso_repo.read(curso_id):
            raise ValueError(f"Curso con ID {curso_id} no existe")
        
        # Validar no duplicar matricula
        duplicada = self.repo.get_estudiante_en_curso(estudiante_id, curso_id)
        if duplicada:
            raise ValueError(f"Estudiante ya está matriculado en este curso")
        
        return self.repo.create({
            "estudiante_id": estudiante_id,
            "curso_id": curso_id,
            "fecha": fecha or date.today(),
            "estado": estado or EstadoMatricula.REGISTRADO
        })

    def obtener_matricula(self, id: int):
        """Obtiene una matrícula por ID"""
        mat = self.repo.read(id)
        if not mat:
            raise ValueError(f"Matrícula con ID {id} no encontrada")
        return mat

    def listar_matriculas(self, skip: int = 0, limit: int = 100):
        """Lista todas las matrículas"""
        return self.repo.read_all(skip, limit)

    def obtener_por_estudiante(self, estudiante_id: int):
        """Obtiene matrículas de un estudiante"""
        return self.repo.get_by_estudiante(estudiante_id)

    def cambiar_estado(self, matricula_id: int, nuevo_estado: str):
        """Cambia el estado de una matrícula con validación"""
        if nuevo_estado not in [e.value for e in EstadoMatricula]:
            raise ValueError(f"Estado inválido: {nuevo_estado}")
        
        return self.repo.update(matricula_id, {"estado": nuevo_estado})

    def actualizar_matricula(self, id: int, **kwargs):
        """Actualiza una matrícula"""
        if not self.repo.read(id):
            raise ValueError(f"Matrícula con ID {id} no encontrada")
        return self.repo.update(id, kwargs)

    def eliminar_matricula(self, id: int):
        """Elimina una matrícula"""
        if not self.repo.delete(id):
            raise ValueError(f"Matrícula con ID {id} no encontrada")
        return True


class CalificacionService:
    """Servicio para Calificaciones con validaciones"""
    
    def __init__(self, db: Session):
        self.repo = CalificacionRepository(db)
        self.mat_repo = MatriculaRepository(db)
        self.asig_repo = AsignaturaRepository(db)
        self.db = db

    def crear_calificacion(self, nota: float, quimestre: int, matricula_id: int, asignatura_id: int):
        """
        Crea una nueva calificación.
        
        Validaciones:
        - Nota entre 0 y 10
        - Quimestre válido (1-3)
        - Matrícula existe
        - Asignatura existe
        """
        if not (0 <= nota <= 10):
            raise ValueError("La nota debe estar entre 0 y 10")
        
        if not (1 <= quimestre <= 3):
            raise ValueError("El quimestre debe estar entre 1 y 3")
        
        if not self.mat_repo.read(matricula_id):
            raise ValueError(f"Matrícula con ID {matricula_id} no existe")
        
        if not self.asig_repo.read(asignatura_id):
            raise ValueError(f"Asignatura con ID {asignatura_id} no existe")
        
        return self.repo.create({
            "nota": nota,
            "quimestre": quimestre,
            "matricula_id": matricula_id,
            "asignatura_id": asignatura_id
        })

    def obtener_calificacion(self, id: int):
        """Obtiene una calificación por ID"""
        cal = self.repo.read(id)
        if not cal:
            raise ValueError(f"Calificación con ID {id} no encontrada")
        return cal

    def listar_calificaciones(self, skip: int = 0, limit: int = 100):
        """Lista todas las calificaciones"""
        return self.repo.read_all(skip, limit)

    def obtener_por_matricula(self, matricula_id: int):
        """Obtiene calificaciones de una matrícula"""
        return self.repo.get_by_matricula(matricula_id)

    def obtener_promedio(self, matricula_id: int) -> float:
        """Calcula promedio de un estudiante"""
        return self.repo.get_promedio_estudiante(matricula_id)

    def actualizar_calificacion(self, id: int, nota: float = None, **kwargs):
        """Actualiza una calificación"""
        if not self.repo.read(id):
            raise ValueError(f"Calificación con ID {id} no encontrada")
        
        if nota is not None:
            if not (0 <= nota <= 10):
                raise ValueError("La nota debe estar entre 0 y 10")
            kwargs["nota"] = nota
        
        return self.repo.update(id, kwargs)

    def eliminar_calificacion(self, id: int):
        """Elimina una calificación"""
        if not self.repo.delete(id):
            raise ValueError(f"Calificación con ID {id} no encontrada")
        return True


class AsistenciaService:
    """Servicio para Asistencias con validaciones"""
    
    def __init__(self, db: Session):
        self.repo = AsistenciaRepository(db)
        self.mat_repo = MatriculaRepository(db)
        self.asig_repo = AsignaturaRepository(db)
        self.db = db

    def crear_asistencia(self, estado: str, matricula_id: int, asignatura_id: int, fecha: date = None):
        """
        Crea un registro de asistencia.
        
        Validaciones:
        - Estado válido (enum)
        - Matrícula existe
        - Asignatura existe
        """
        if estado not in [e.value for e in EstadoAsistencia]:
            raise ValueError(f"Estado inválido: {estado}")
        
        if not self.mat_repo.read(matricula_id):
            raise ValueError(f"Matrícula con ID {matricula_id} no existe")
        
        if not self.asig_repo.read(asignatura_id):
            raise ValueError(f"Asignatura con ID {asignatura_id} no existe")
        
        return self.repo.create({
            "estado": estado,
            "matricula_id": matricula_id,
            "asignatura_id": asignatura_id,
            "fecha": fecha or date.today()
        })

    def obtener_asistencia(self, id: int):
        """Obtiene un registro de asistencia"""
        asi = self.repo.read(id)
        if not asi:
            raise ValueError(f"Asistencia con ID {id} no encontrada")
        return asi

    def listar_asistencias(self, skip: int = 0, limit: int = 100):
        """Lista todas las asistencias"""
        return self.repo.read_all(skip, limit)

    def obtener_por_matricula(self, matricula_id: int):
        """Obtiene asistencias de una matrícula"""
        return self.repo.get_by_matricula(matricula_id)

    def actualizar_asistencia(self, id: int, estado: str = None, **kwargs):
        """Actualiza una asistencia"""
        if not self.repo.read(id):
            raise ValueError(f"Asistencia con ID {id} no encontrada")
        
        if estado is not None:
            if estado not in [e.value for e in EstadoAsistencia]:
                raise ValueError(f"Estado inválido: {estado}")
            kwargs["estado"] = estado
        
        return self.repo.update(id, kwargs)

    def eliminar_asistencia(self, id: int):
        """Elimina un registro de asistencia"""
        if not self.repo.delete(id):
            raise ValueError(f"Asistencia con ID {id} no encontrada")
        return True
