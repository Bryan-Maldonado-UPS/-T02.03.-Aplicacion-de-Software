from fastapi import APIRouter, Depends, HTTPException
from config.database import SessionLocal
from services.services import AsistenciaService
from schemas.asistencia import AsistenciaCreate, AsistenciaUpdate, AsistenciaRead
from typing import List

router = APIRouter(prefix="/asistencias", tags=["Asistencias"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("", response_model=AsistenciaRead, status_code=201)
def crear_asistencia(asis: AsistenciaCreate, db = Depends(get_db)):
    """Crear una nueva asistencia"""
    service = AsistenciaService(db)
    try:
        return service.crear_asistencia(
            estado=asis.estado.value if hasattr(asis.estado, 'value') else asis.estado,
            matricula_id=asis.matricula_id,
            asignatura_id=asis.asignatura_id,
            fecha=asis.fecha
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/{asis_id}", response_model=AsistenciaRead)
def obtener_asistencia(asis_id: int, db = Depends(get_db)):
    """Obtener una asistencia por ID"""
    service = AsistenciaService(db)
    asis = service.obtener_asistencia(asis_id)
    if not asis:
        raise HTTPException(status_code=404, detail="Asistencia no encontrada")
    return asis


@router.get("", response_model=List[AsistenciaRead])
def listar_asistencias(skip: int = 0, limit: int = 10, db = Depends(get_db)):
    """Listar todas las asistencias"""
    service = AsistenciaService(db)
    return service.listar_asistencias(skip, limit)


@router.put("/{asis_id}", response_model=AsistenciaRead)
def actualizar_asistencia(asis_id: int, asis: AsistenciaUpdate, db = Depends(get_db)):
    """Actualizar una asistencia"""
    service = AsistenciaService(db)
    try:
        update_dict = asis.dict(exclude_unset=True)
        if 'estado' in update_dict and hasattr(update_dict['estado'], 'value'):
            update_dict['estado'] = update_dict['estado'].value
        updated = service.actualizar_asistencia(asis_id, **update_dict)
        if not updated:
            raise HTTPException(status_code=404, detail="Asistencia no encontrada")
        return updated
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/{asis_id}", status_code=204)
def eliminar_asistencia(asis_id: int, db = Depends(get_db)):
    """Eliminar una asistencia"""
    service = AsistenciaService(db)
    success = service.eliminar_asistencia(asis_id)
    if not success:
        raise HTTPException(status_code=404, detail="Asistencia no encontrada")
