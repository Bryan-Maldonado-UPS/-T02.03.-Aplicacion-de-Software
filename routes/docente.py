from fastapi import APIRouter, Depends, HTTPException
from config.database import SessionLocal
from services.services import DocenteService
from schemas.docente import DocenteCreate, DocenteUpdate, DocenteRead
from typing import List

router = APIRouter(prefix="/docentes", tags=["Docentes"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("", response_model=DocenteRead, status_code=201)
def crear_docente(doc: DocenteCreate, db = Depends(get_db)):
    """Crear un nuevo docente"""
    service = DocenteService(db)
    try:
        return service.crear_docente(
            nombre=doc.nombre,
            apellido=doc.apellido,
            titulo=doc.titulo,
            correo=doc.correo
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/{doc_id}", response_model=DocenteRead)
def obtener_docente(doc_id: int, db = Depends(get_db)):
    """Obtener un docente por ID"""
    service = DocenteService(db)
    doc = service.obtener_docente(doc_id)
    if not doc:
        raise HTTPException(status_code=404, detail="Docente no encontrado")
    return doc


@router.get("", response_model=List[DocenteRead])
def listar_docentes(skip: int = 0, limit: int = 10, db = Depends(get_db)):
    """Listar todos los docentes"""
    service = DocenteService(db)
    return service.listar_docentes(skip, limit)


@router.put("/{doc_id}", response_model=DocenteRead)
def actualizar_docente(doc_id: int, doc: DocenteUpdate, db = Depends(get_db)):
    """Actualizar un docente"""
    service = DocenteService(db)
    try:
        updated = service.actualizar_docente(doc_id, **doc.dict(exclude_unset=True))
        if not updated:
            raise HTTPException(status_code=404, detail="Docente no encontrado")
        return updated
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/{doc_id}", status_code=204)
def eliminar_docente(doc_id: int, db = Depends(get_db)):
    """Eliminar un docente"""
    service = DocenteService(db)
    success = service.eliminar_docente(doc_id)
    if not success:
        raise HTTPException(status_code=404, detail="Docente no encontrado")
