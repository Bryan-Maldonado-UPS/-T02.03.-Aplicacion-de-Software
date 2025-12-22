"""
Rutas para gestionar Representantes
"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from config.database import get_db
from services import RepresentanteService
from schemas import RepresentanteCreate, RepresentanteRead

router = APIRouter(
    prefix="/representantes",
    tags=["Representantes"],
    responses={404: {"description": "No encontrado"}},
)


@router.post(
    "",
    response_model=RepresentanteRead,
    status_code=status.HTTP_201_CREATED,
    summary="Crear nuevo representante",
    description="Crea un nuevo representante en el sistema"
)
def crear_representante(
    representante: RepresentanteCreate,
    db: Session = Depends(get_db)
):
    """Crear un nuevo representante"""
    try:
        service = RepresentanteService(db)
        return service.crear_representante(
            nombre=representante.nombre,
            telefono=representante.telefono
        )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al crear representante: {str(e)}"
        )


@router.get(
    "",
    response_model=list[RepresentanteRead],
    summary="Listar representantes",
    description="Obtiene la lista de todos los representantes"
)
def listar_representantes(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    """Listar todos los representantes"""
    try:
        service = RepresentanteService(db)
        return service.listar_representantes(skip=skip, limit=limit)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al listar representantes: {str(e)}"
        )


@router.get(
    "/{representante_id}",
    response_model=RepresentanteRead,
    summary="Obtener representante por ID",
    description="Obtiene un representante específico"
)
def obtener_representante(
    representante_id: int,
    db: Session = Depends(get_db)
):
    """Obtener representante por ID"""
    try:
        service = RepresentanteService(db)
        representante = service.obtener_representante(representante_id)
        if not representante:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Representante con ID {representante_id} no encontrado"
            )
        return representante
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al obtener representante: {str(e)}"
        )


@router.put(
    "/{representante_id}",
    response_model=RepresentanteRead,
    summary="Actualizar representante",
    description="Actualiza los datos de un representante"
)
def actualizar_representante(
    representante_id: int,
    representante: RepresentanteCreate,
    db: Session = Depends(get_db)
):
    """Actualizar representante"""
    try:
        service = RepresentanteService(db)
        rep = service.actualizar_representante(
            representante_id,
            nombre=representante.nombre,
            telefono=representante.telefono
        )
        if not rep:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Representante con ID {representante_id} no encontrado"
            )
        return rep
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
            detail=f"Error al actualizar representante: {str(e)}"
        )


@router.delete(
    "/{representante_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Eliminar representante",
    description="Elimina un representante del sistema"
)
def eliminar_representante(
    representante_id: int,
    db: Session = Depends(get_db)
):
    """Eliminar representante"""
    try:
        service = RepresentanteService(db)
        if not service.eliminar_representante(representante_id):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Representante con ID {representante_id} no encontrado"
            )
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al eliminar representante: {str(e)}"
        )
