"""
Rutas para gestionar Estudiantes
"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from config.database import get_db
from services import EstudianteService
from schemas import EstudianteCreate, EstudianteRead, EstudianteUpdate

router = APIRouter(
    prefix="/estudiantes",
    tags=["Estudiantes"],
    responses={404: {"description": "No encontrado"}},
)


@router.post(
    "",
    response_model=EstudianteRead,
    status_code=status.HTTP_201_CREATED,
    summary="Crear nuevo estudiante",
    description="Crea un nuevo estudiante con validación de edad (mínimo 5 años) y cédula única"
)
def crear_estudiante(
    estudiante: EstudianteCreate,
    db: Session = Depends(get_db)
):
    """Crear un nuevo estudiante"""
    try:
        service = EstudianteService(db)
        return service.crear_estudiante(
            nombre=estudiante.nombre,
            apellido=estudiante.apellido,
            cedula=estudiante.cedula,
            fecha_nacimiento=estudiante.fecha_nacimiento,
            correo=estudiante.correo,
            representante_id=estudiante.representante_id
        )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al crear estudiante: {str(e)}"
        )


@router.get(
    "",
    response_model=list[EstudianteRead],
    summary="Listar estudiantes",
    description="Obtiene la lista de todos los estudiantes"
)
def listar_estudiantes(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    """Listar todos los estudiantes"""
    try:
        service = EstudianteService(db)
        return service.listar_estudiantes(skip=skip, limit=limit)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al listar estudiantes: {str(e)}"
        )


@router.get(
    "/{estudiante_id}",
    response_model=EstudianteRead,
    summary="Obtener estudiante por ID",
    description="Obtiene un estudiante específico"
)
def obtener_estudiante(
    estudiante_id: int,
    db: Session = Depends(get_db)
):
    """Obtener estudiante por ID"""
    try:
        service = EstudianteService(db)
        estudiante = service.obtener_estudiante(estudiante_id)
        if not estudiante:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Estudiante con ID {estudiante_id} no encontrado"
            )
        return estudiante
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al obtener estudiante: {str(e)}"
        )


@router.get(
    "/cedula/{cedula}",
    response_model=EstudianteRead,
    summary="Obtener estudiante por cédula",
    description="Busca un estudiante por su cédula"
)
def obtener_por_cedula(
    cedula: str,
    db: Session = Depends(get_db)
):
    """Obtener estudiante por cédula"""
    try:
        service = EstudianteService(db)
        estudiante = service.obtener_por_cedula(cedula)
        if not estudiante:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Estudiante con cédula {cedula} no encontrado"
            )
        return estudiante
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al obtener estudiante: {str(e)}"
        )


@router.put(
    "/{estudiante_id}",
    response_model=EstudianteRead,
    summary="Actualizar estudiante",
    description="Actualiza los datos de un estudiante"
)
def actualizar_estudiante(
    estudiante_id: int,
    estudiante: EstudianteUpdate,
    db: Session = Depends(get_db)
):
    """Actualizar estudiante"""
    try:
        service = EstudianteService(db)
        est = service.actualizar_estudiante(
            estudiante_id,
            nombre=estudiante.nombre,
            apellido=estudiante.apellido,
            correo=estudiante.correo
        )
        if not est:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Estudiante con ID {estudiante_id} no encontrado"
            )
        return est
    except HTTPException:
        raise
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al actualizar estudiante: {str(e)}"
        )


@router.delete(
    "/{estudiante_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Eliminar estudiante",
    description="Elimina un estudiante del sistema"
)
def eliminar_estudiante(
    estudiante_id: int,
    db: Session = Depends(get_db)
):
    """Eliminar estudiante"""
    try:
        service = EstudianteService(db)
        if not service.eliminar_estudiante(estudiante_id):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Estudiante con ID {estudiante_id} no encontrado"
            )
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al eliminar estudiante: {str(e)}"
        )
