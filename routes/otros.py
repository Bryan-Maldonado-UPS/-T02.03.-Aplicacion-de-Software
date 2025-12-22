"""
Rutas para gestionar Docentes, Cursos, Asignaturas, Matrículas, Calificaciones y Asistencias
"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from config.database import get_db
from services import (
    DocenteService, CursoService, AsignaturaService,
    MatriculaService, CalificacionService, AsistenciaService
)
from schemas import (
    DocenteCreate, DocenteRead,
    CursoCreate, CursoRead,
    AsignaturaCreate, AsignaturaRead,
    MatriculaCreate, MatriculaRead, MatriculaUpdate,
    CalificacionCreate, CalificacionRead, CalificacionUpdate,
    AsistenciaCreate, AsistenciaRead, AsistenciaUpdate
)

# ============================================================================
# DOCENTES
# ============================================================================
docentes_router = APIRouter(prefix="/docentes", tags=["Docentes"])

@docentes_router.post("", response_model=DocenteRead, status_code=status.HTTP_201_CREATED)
def crear_docente(docente: DocenteCreate, db: Session = Depends(get_db)):
    try:
        service = DocenteService(db)
        return service.crear_docente(
            nombre=docente.nombre, apellido=docente.apellido,
            titulo=docente.titulo, correo=docente.correo
        )
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@docentes_router.get("", response_model=list[DocenteRead])
def listar_docentes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    service = DocenteService(db)
    return service.listar_docentes(skip=skip, limit=limit)

@docentes_router.get("/{docente_id}", response_model=DocenteRead)
def obtener_docente(docente_id: int, db: Session = Depends(get_db)):
    service = DocenteService(db)
    docente = service.obtener_docente(docente_id)
    if not docente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Docente no encontrado")
    return docente

@docentes_router.put("/{docente_id}", response_model=DocenteRead)
def actualizar_docente(docente_id: int, docente: DocenteCreate, db: Session = Depends(get_db)):
    try:
        service = DocenteService(db)
        doc = service.actualizar_docente(docente_id, **docente.dict())
        if not doc:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Docente no encontrado")
        return doc
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@docentes_router.delete("/{docente_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_docente(docente_id: int, db: Session = Depends(get_db)):
    service = DocenteService(db)
    if not service.eliminar_docente(docente_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Docente no encontrado")

# ============================================================================
# CURSOS
# ============================================================================
cursos_router = APIRouter(prefix="/cursos", tags=["Cursos"])

@cursos_router.post("", response_model=CursoRead, status_code=status.HTTP_201_CREATED)
def crear_curso(curso: CursoCreate, db: Session = Depends(get_db)):
    service = CursoService(db)
    return service.crear_curso(nombre=curso.nombre, nivel=curso.nivel)

@cursos_router.get("", response_model=list[CursoRead])
def listar_cursos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    service = CursoService(db)
    return service.listar_cursos(skip=skip, limit=limit)

@cursos_router.get("/{curso_id}", response_model=CursoRead)
def obtener_curso(curso_id: int, db: Session = Depends(get_db)):
    service = CursoService(db)
    curso = service.obtener_curso(curso_id)
    if not curso:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso no encontrado")
    return curso

@cursos_router.put("/{curso_id}", response_model=CursoRead)
def actualizar_curso(curso_id: int, curso: CursoCreate, db: Session = Depends(get_db)):
    service = CursoService(db)
    cur = service.actualizar_curso(curso_id, **curso.dict())
    if not cur:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso no encontrado")
    return cur

@cursos_router.delete("/{curso_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_curso(curso_id: int, db: Session = Depends(get_db)):
    service = CursoService(db)
    if not service.eliminar_curso(curso_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso no encontrado")

# ============================================================================
# ASIGNATURAS
# ============================================================================
asignaturas_router = APIRouter(prefix="/asignaturas", tags=["Asignaturas"])

@asignaturas_router.post("", response_model=AsignaturaRead, status_code=status.HTTP_201_CREATED)
def crear_asignatura(asignatura: AsignaturaCreate, db: Session = Depends(get_db)):
    try:
        service = AsignaturaService(db)
        return service.crear_asignatura(
            nombre=asignatura.nombre, descripcion=asignatura.descripcion,
            curso_id=asignatura.curso_id, docente_id=asignatura.docente_id
        )
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@asignaturas_router.get("", response_model=list[AsignaturaRead])
def listar_asignaturas(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    service = AsignaturaService(db)
    return service.listar_asignaturas(skip=skip, limit=limit)

@asignaturas_router.get("/{asignatura_id}", response_model=AsignaturaRead)
def obtener_asignatura(asignatura_id: int, db: Session = Depends(get_db)):
    service = AsignaturaService(db)
    asignatura = service.obtener_asignatura(asignatura_id)
    if not asignatura:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Asignatura no encontrada")
    return asignatura

@asignaturas_router.put("/{asignatura_id}", response_model=AsignaturaRead)
def actualizar_asignatura(asignatura_id: int, asignatura: AsignaturaCreate, db: Session = Depends(get_db)):
    try:
        service = AsignaturaService(db)
        asig = service.actualizar_asignatura(asignatura_id, **asignatura.dict())
        if not asig:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Asignatura no encontrada")
        return asig
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@asignaturas_router.delete("/{asignatura_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_asignatura(asignatura_id: int, db: Session = Depends(get_db)):
    service = AsignaturaService(db)
    if not service.eliminar_asignatura(asignatura_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Asignatura no encontrada")

# ============================================================================
# MATRICULAS
# ============================================================================
matriculas_router = APIRouter(prefix="/matriculas", tags=["Matrículas"])

@matriculas_router.post("", response_model=MatriculaRead, status_code=status.HTTP_201_CREATED)
def crear_matricula(matricula: MatriculaCreate, db: Session = Depends(get_db)):
    try:
        service = MatriculaService(db)
        return service.crear_matricula(
            estudiante_id=matricula.estudiante_id,
            curso_id=matricula.curso_id,
            estado=matricula.estado
        )
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@matriculas_router.get("", response_model=list[MatriculaRead])
def listar_matriculas(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    service = MatriculaService(db)
    return service.listar_matriculas(skip=skip, limit=limit)

@matriculas_router.get("/{matricula_id}", response_model=MatriculaRead)
def obtener_matricula(matricula_id: int, db: Session = Depends(get_db)):
    service = MatriculaService(db)
    matricula = service.obtener_matricula(matricula_id)
    if not matricula:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Matrícula no encontrada")
    return matricula

@matriculas_router.put("/{matricula_id}", response_model=MatriculaRead)
def actualizar_matricula(matricula_id: int, matricula: MatriculaUpdate, db: Session = Depends(get_db)):
    try:
        service = MatriculaService(db)
        mat = service.cambiar_estado(matricula_id, matricula.estado)
        if not mat:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Matrícula no encontrada")
        return mat
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@matriculas_router.delete("/{matricula_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_matricula(matricula_id: int, db: Session = Depends(get_db)):
    service = MatriculaService(db)
    if not service.eliminar_matricula(matricula_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Matrícula no encontrada")

# ============================================================================
# CALIFICACIONES
# ============================================================================
calificaciones_router = APIRouter(prefix="/calificaciones", tags=["Calificaciones"])

@calificaciones_router.post("", response_model=CalificacionRead, status_code=status.HTTP_201_CREATED)
def crear_calificacion(calificacion: CalificacionCreate, db: Session = Depends(get_db)):
    try:
        service = CalificacionService(db)
        return service.crear_calificacion(
            nota=calificacion.nota,
            quimestre=calificacion.quimestre,
            matricula_id=calificacion.matricula_id,
            asignatura_id=calificacion.asignatura_id
        )
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@calificaciones_router.get("", response_model=list[CalificacionRead])
def listar_calificaciones(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    service = CalificacionService(db)
    return service.listar_calificaciones(skip=skip, limit=limit)

@calificaciones_router.get("/{calificacion_id}", response_model=CalificacionRead)
def obtener_calificacion(calificacion_id: int, db: Session = Depends(get_db)):
    service = CalificacionService(db)
    calificacion = service.obtener_calificacion(calificacion_id)
    if not calificacion:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Calificación no encontrada")
    return calificacion

@calificaciones_router.put("/{calificacion_id}", response_model=CalificacionRead)
def actualizar_calificacion(calificacion_id: int, calificacion: CalificacionUpdate, db: Session = Depends(get_db)):
    try:
        service = CalificacionService(db)
        cal = service.actualizar_calificacion(calificacion_id, nota=calificacion.nota)
        if not cal:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Calificación no encontrada")
        return cal
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@calificaciones_router.delete("/{calificacion_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_calificacion(calificacion_id: int, db: Session = Depends(get_db)):
    service = CalificacionService(db)
    if not service.eliminar_calificacion(calificacion_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Calificación no encontrada")

# ============================================================================
# ASISTENCIAS
# ============================================================================
asistencias_router = APIRouter(prefix="/asistencias", tags=["Asistencias"])

@asistencias_router.post("", response_model=AsistenciaRead, status_code=status.HTTP_201_CREATED)
def crear_asistencia(asistencia: AsistenciaCreate, db: Session = Depends(get_db)):
    try:
        service = AsistenciaService(db)
        return service.crear_asistencia(
            estado=asistencia.estado,
            matricula_id=asistencia.matricula_id,
            asignatura_id=asistencia.asignatura_id
        )
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@asistencias_router.get("", response_model=list[AsistenciaRead])
def listar_asistencias(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    service = AsistenciaService(db)
    return service.listar_asistencias(skip=skip, limit=limit)

@asistencias_router.get("/{asistencia_id}", response_model=AsistenciaRead)
def obtener_asistencia(asistencia_id: int, db: Session = Depends(get_db)):
    service = AsistenciaService(db)
    asistencia = service.obtener_asistencia(asistencia_id)
    if not asistencia:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Asistencia no encontrada")
    return asistencia

@asistencias_router.put("/{asistencia_id}", response_model=AsistenciaRead)
def actualizar_asistencia(asistencia_id: int, asistencia: AsistenciaUpdate, db: Session = Depends(get_db)):
    try:
        service = AsistenciaService(db)
        asis = service.actualizar_asistencia(asistencia_id, estado=asistencia.estado)
        if not asis:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Asistencia no encontrada")
        return asis
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@asistencias_router.delete("/{asistencia_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_asistencia(asistencia_id: int, db: Session = Depends(get_db)):
    service = AsistenciaService(db)
    if not service.eliminar_asistencia(asistencia_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Asistencia no encontrada")
