from fastapi import APIRouter, Depends, HTTPException
from config.database import SessionLocal
from services.services import AsignaturaService
from schemas.asignatura import AsignaturaCreate, AsignaturaUpdate, AsignaturaRead
from typing import List

router = APIRouter(prefix="/asignaturas", tags=["Asignaturas"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("", response_model=AsignaturaRead, status_code=201)
def crear_asignatura(asig: AsignaturaCreate, db = Depends(get_db)):
    """Crear una nueva asignatura"""
    service = AsignaturaService(db)
    return service.crear_asignatura(
        nombre=asig.nombre,
        descripcion=asig.descripcion,
        curso_id=asig.curso_id,
        docente_id=asig.docente_id
    )


@router.get("/{asig_id}", response_model=AsignaturaRead)
def obtener_asignatura(asig_id: int, db = Depends(get_db)):
    """Obtener una asignatura por ID"""
    service = AsignaturaService(db)
    asig = service.obtener_asignatura(asig_id)
    if not asig:
        raise HTTPException(status_code=404, detail="Asignatura no encontrada")
    return asig


@router.get("", response_model=List[AsignaturaRead])
def listar_asignaturas(skip: int = 0, limit: int = 10, db = Depends(get_db)):
    """Listar todas las asignaturas"""
    service = AsignaturaService(db)
    return service.listar_asignaturas(skip, limit)


@router.put("/{asig_id}", response_model=AsignaturaRead)
def actualizar_asignatura(asig_id: int, asig: AsignaturaUpdate, db = Depends(get_db)):
    """Actualizar una asignatura"""
    service = AsignaturaService(db)
    updated = service.actualizar_asignatura(asig_id, **asig.dict(exclude_unset=True))
    if not updated:
        raise HTTPException(status_code=404, detail="Asignatura no encontrada")
    return updated


@router.delete("/{asig_id}", status_code=204)
def eliminar_asignatura(asig_id: int, db = Depends(get_db)):
    """Eliminar una asignatura"""
    service = AsignaturaService(db)
    success = service.eliminar_asignatura(asig_id)
    if not success:
        raise HTTPException(status_code=404, detail="Asignatura no encontrada")
