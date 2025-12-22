from fastapi import APIRouter, Depends, HTTPException
from config.database import SessionLocal
from services.services import EstudianteService
from schemas.estudiante import EstudianteCreate, EstudianteUpdate, EstudianteRead
from typing import List

router = APIRouter(prefix="/estudiantes", tags=["Estudiantes"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("", response_model=EstudianteRead, status_code=201)
def crear_estudiante(est: EstudianteCreate, db = Depends(get_db)):
    """Crear un nuevo estudiante"""
    service = EstudianteService(db)
    try:
        return service.crear_estudiante(
            nombre=est.nombre,
            apellido=est.apellido,
            cedula=est.cedula,
            fecha_nacimiento=est.fecha_nacimiento,
            correo=est.correo,
            representante_id=est.representante_id
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/{est_id}", response_model=EstudianteRead)
def obtener_estudiante(est_id: int, db = Depends(get_db)):
    """Obtener un estudiante por ID"""
    service = EstudianteService(db)
    est = service.obtener_estudiante(est_id)
    if not est:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")
    return est


@router.get("", response_model=List[EstudianteRead])
def listar_estudiantes(skip: int = 0, limit: int = 10, db = Depends(get_db)):
    """Listar todos los estudiantes"""
    service = EstudianteService(db)
    return service.listar_estudiantes(skip, limit)


@router.put("/{est_id}", response_model=EstudianteRead)
def actualizar_estudiante(est_id: int, est: EstudianteUpdate, db = Depends(get_db)):
    """Actualizar un estudiante"""
    service = EstudianteService(db)
    try:
        updated = service.actualizar_estudiante(est_id, **est.dict(exclude_unset=True))
        if not updated:
            raise HTTPException(status_code=404, detail="Estudiante no encontrado")
        return updated
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/{est_id}", status_code=204)
def eliminar_estudiante(est_id: int, db = Depends(get_db)):
    """Eliminar un estudiante"""
    service = EstudianteService(db)
    success = service.eliminar_estudiante(est_id)
    if not success:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")
