from fastapi import APIRouter, Depends, HTTPException
from config.database import SessionLocal
from services.services import CalificacionService
from schemas.calificacion import CalificacionCreate, CalificacionUpdate, CalificacionRead
from typing import List

router = APIRouter(prefix="/calificaciones", tags=["Calificaciones"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("", response_model=CalificacionRead, status_code=201)
def crear_calificacion(cal: CalificacionCreate, db = Depends(get_db)):
    """Crear una nueva calificación"""
    service = CalificacionService(db)
    try:
        return service.crear_calificacion(
            nota=cal.nota,
            quimestre=cal.quimestre,
            matricula_id=cal.matricula_id,
            asignatura_id=cal.asignatura_id
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/{cal_id}", response_model=CalificacionRead)
def obtener_calificacion(cal_id: int, db = Depends(get_db)):
    """Obtener una calificación por ID"""
    service = CalificacionService(db)
    cal = service.obtener_calificacion(cal_id)
    if not cal:
        raise HTTPException(status_code=404, detail="Calificación no encontrada")
    return cal


@router.get("", response_model=List[CalificacionRead])
def listar_calificaciones(skip: int = 0, limit: int = 10, db = Depends(get_db)):
    """Listar todas las calificaciones"""
    service = CalificacionService(db)
    return service.listar_calificaciones(skip, limit)


@router.put("/{cal_id}", response_model=CalificacionRead)
def actualizar_calificacion(cal_id: int, cal: CalificacionUpdate, db = Depends(get_db)):
    """Actualizar una calificación"""
    service = CalificacionService(db)
    try:
        updated = service.actualizar_calificacion(cal_id, **cal.dict(exclude_unset=True))
        if not updated:
            raise HTTPException(status_code=404, detail="Calificación no encontrada")
        return updated
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/{cal_id}", status_code=204)
def eliminar_calificacion(cal_id: int, db = Depends(get_db)):
    """Eliminar una calificación"""
    service = CalificacionService(db)
    success = service.eliminar_calificacion(cal_id)
    if not success:
        raise HTTPException(status_code=404, detail="Calificación no encontrada")
