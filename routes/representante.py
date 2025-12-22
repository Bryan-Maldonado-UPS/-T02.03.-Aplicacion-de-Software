from fastapi import APIRouter, Depends, HTTPException
from config.database import SessionLocal
from services.services import RepresentanteService
from schemas.representante import RepresentanteCreate, RepresentanteUpdate, RepresentanteRead
from typing import List

router = APIRouter(prefix="/representantes", tags=["Representantes"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("", response_model=RepresentanteRead, status_code=201)
def crear_representante(rep: RepresentanteCreate, db = Depends(get_db)):
    """Crear un nuevo representante"""
    service = RepresentanteService(db)
    return service.crear_representante(nombre=rep.nombre, telefono=rep.telefono)


@router.get("/{rep_id}", response_model=RepresentanteRead)
def obtener_representante(rep_id: int, db = Depends(get_db)):
    """Obtener un representante por ID"""
    service = RepresentanteService(db)
    rep = service.obtener_representante(rep_id)
    if not rep:
        raise HTTPException(status_code=404, detail="Representante no encontrado")
    return rep


@router.get("", response_model=List[RepresentanteRead])
def listar_representantes(skip: int = 0, limit: int = 10, db = Depends(get_db)):
    """Listar todos los representantes"""
    service = RepresentanteService(db)
    return service.listar_representantes(skip, limit)


@router.put("/{rep_id}", response_model=RepresentanteRead)
def actualizar_representante(rep_id: int, rep: RepresentanteUpdate, db = Depends(get_db)):
    """Actualizar un representante"""
    service = RepresentanteService(db)
    updated = service.actualizar_representante(rep_id, **rep.dict(exclude_unset=True))
    if not updated:
        raise HTTPException(status_code=404, detail="Representante no encontrado")
    return updated


@router.delete("/{rep_id}", status_code=204)
def eliminar_representante(rep_id: int, db = Depends(get_db)):
    """Eliminar un representante"""
    service = RepresentanteService(db)
    success = service.eliminar_representante(rep_id)
    if not success:
        raise HTTPException(status_code=404, detail="Representante no encontrado")
