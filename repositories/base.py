"""
BaseRepository - Clase base para todos los repositorios
Implementa métodos CRUD genéricos
"""
from typing import TypeVar, Generic, List, Optional, Type
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

T = TypeVar('T')


class BaseRepository(Generic[T]):
    """
    Clase base que proporciona métodos CRUD genéricos para cualquier modelo.
    """

    def __init__(self, db: Session, model: Type[T]):
        """
        Inicializa el repositorio con una sesión de BD y un modelo.
        
        Args:
            db: Sesión de SQLAlchemy
            model: Clase del modelo (ej: Estudiante, Docente)
        """
        self.db = db
        self.model = model

    def create(self, obj_in: dict) -> T:
        """
        Crea un nuevo registro en la BD.
        
        Args:
            obj_in: Diccionario con los datos
            
        Returns:
            Objeto creado
            
        Raises:
            SQLAlchemyError: Si hay error en la BD
        """
        try:
            db_obj = self.model(**obj_in)
            self.db.add(db_obj)
            self.db.commit()
            self.db.refresh(db_obj)
            return db_obj
        except SQLAlchemyError as e:
            self.db.rollback()
            raise Exception(f"Error al crear {self.model.__name__}: {str(e)}")

    def read(self, id: int) -> Optional[T]:
        """
        Obtiene un registro por ID.
        
        Args:
            id: ID del registro
            
        Returns:
            Objeto encontrado o None
        """
        return self.db.query(self.model).filter(self.model.id == id).first()

    def read_all(self, skip: int = 0, limit: int = 100) -> List[T]:
        """
        Obtiene todos los registros con paginación.
        
        Args:
            skip: Registros a saltar
            limit: Límite de registros a traer
            
        Returns:
            Lista de objetos
        """
        return self.db.query(self.model).offset(skip).limit(limit).all()

    def update(self, id: int, obj_in: dict) -> Optional[T]:
        """
        Actualiza un registro existente.
        
        Args:
            id: ID del registro
            obj_in: Diccionario con nuevos datos
            
        Returns:
            Objeto actualizado o None si no existe
        """
        try:
            db_obj = self.read(id)
            if not db_obj:
                return None
            
            for key, value in obj_in.items():
                setattr(db_obj, key, value)
            
            self.db.commit()
            self.db.refresh(db_obj)
            return db_obj
        except SQLAlchemyError as e:
            self.db.rollback()
            raise Exception(f"Error al actualizar {self.model.__name__}: {str(e)}")

    def delete(self, id: int) -> bool:
        """
        Elimina un registro.
        
        Args:
            id: ID del registro
            
        Returns:
            True si se eliminó, False si no existe
        """
        try:
            db_obj = self.read(id)
            if not db_obj:
                return False
            
            self.db.delete(db_obj)
            self.db.commit()
            return True
        except SQLAlchemyError as e:
            self.db.rollback()
            raise Exception(f"Error al eliminar {self.model.__name__}: {str(e)}")

    def count(self) -> int:
        """
        Cuenta el total de registros.
        
        Returns:
            Número de registros
        """
        return self.db.query(self.model).count()
