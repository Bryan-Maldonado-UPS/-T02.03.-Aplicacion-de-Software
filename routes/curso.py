from fastapi import APIRouter, Depends, HTTPException
from config.database import SessionLocal
from services.services import CursoService
from schemas.curso import CursoCreate, CursoUpdate, CursoRead
from typing import List

router = APIRouter(prefix="/cursos", tags=["Cursos"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("", response_model=CursoRead, status_code=201)
def crear_curso(cur: CursoCreate, db = Depends(get_db)):
    """Crear un nuevo curso"""
    service = CursoService(db)
    return service.crear_curso(nombre=cur.nombre, nivel=cur.nivel)


@router.get("/{cur_id}", response_model=CursoRead)
def obtener_curso(cur_id: int, db = Depends(get_db)):
    """Obtener un curso por ID"""
    service = CursoService(db)
    cur = service.obtener_curso(cur_id)
    if not cur:
        raise HTTPException(status_code=404, detail="Curso no encontrado")
    return cur


@router.get("", response_model=List[CursoRead])
def listar_cursos(skip: int = 0, limit: int = 10, db = Depends(get_db)):
    """Listar todos los cursos"""
    service = CursoService(db)
    return service.listar_cursos(skip, limit)


@router.put("/{cur_id}", response_model=CursoRead)
def actualizar_curso(cur_id: int, cur: CursoUpdate, db = Depends(get_db)):
    """Actualizar un curso"""
    service = CursoService(db)
    updated = service.actualizar_curso(cur_id, **cur.dict(exclude_unset=True))
    if not updated:
        raise HTTPException(status_code=404, detail="Curso no encontrado")
    return updated


@router.delete("/{cur_id}", status_code=204)
def eliminar_curso(cur_id: int, db = Depends(get_db)):
    """Eliminar un curso"""
    service = CursoService(db)
    success = service.eliminar_curso(cur_id)
    if not success:
        raise HTTPException(status_code=404, detail="Curso no encontrado")
