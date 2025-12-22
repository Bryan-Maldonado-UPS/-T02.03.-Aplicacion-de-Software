from fastapi import APIRouter, Depends, HTTPException
from config.database import SessionLocal
from services.services import MatriculaService
from schemas.matricula import MatriculaCreate, MatriculaUpdate, MatriculaRead
from typing import List

router = APIRouter(prefix="/matriculas", tags=["Matrículas"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("", response_model=MatriculaRead, status_code=201)
def crear_matricula(mat: MatriculaCreate, db = Depends(get_db)):
    """Crear una nueva matrícula"""
    service = MatriculaService(db)
    try:
        return service.crear_matricula(
            estudiante_id=mat.estudiante_id,
            curso_id=mat.curso_id,
            estado=mat.estado.value if hasattr(mat.estado, 'value') else mat.estado,
            fecha=mat.fecha
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/{mat_id}", response_model=MatriculaRead)
def obtener_matricula(mat_id: int, db = Depends(get_db)):
    """Obtener una matrícula por ID"""
    service = MatriculaService(db)
    mat = service.obtener_matricula(mat_id)
    if not mat:
        raise HTTPException(status_code=404, detail="Matrícula no encontrada")
    return mat


@router.get("", response_model=List[MatriculaRead])
def listar_matriculas(skip: int = 0, limit: int = 10, db = Depends(get_db)):
    """Listar todas las matrículas"""
    service = MatriculaService(db)
    return service.listar_matriculas(skip, limit)


@router.put("/{mat_id}", response_model=MatriculaRead)
def actualizar_matricula(mat_id: int, mat: MatriculaUpdate, db = Depends(get_db)):
    """Actualizar una matrícula"""
    service = MatriculaService(db)
    try:
        update_dict = mat.dict(exclude_unset=True)
        if 'estado' in update_dict and hasattr(update_dict['estado'], 'value'):
            update_dict['estado'] = update_dict['estado'].value
        updated = service.actualizar_matricula(mat_id, **update_dict)
        if not updated:
            raise HTTPException(status_code=404, detail="Matrícula no encontrada")
        return updated
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/{mat_id}", status_code=204)
def eliminar_matricula(mat_id: int, db = Depends(get_db)):
    """Eliminar una matrícula"""
    service = MatriculaService(db)
    success = service.eliminar_matricula(mat_id)
    if not success:
        raise HTTPException(status_code=404, detail="Matrícula no encontrada")
