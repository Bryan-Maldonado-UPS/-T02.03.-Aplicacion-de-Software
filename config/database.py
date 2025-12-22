from sqlalchemy import create_engine, text
from sqlalchemy.orm import declarative_base, sessionmaker
from typing import Generator
import os

# Configuración de la conexión a PostgreSQL local
# Usar variable de entorno si existe, sino usar la BD local
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:abcd.1234@host.docker.internal:5432/unidad_educativa"
)

# Crear el motor de la base de datos
engine = create_engine(
    DATABASE_URL,
    echo=True,  # Mostrar las sentencias SQL generadas (desactivar en producción)
    pool_size=10,
    max_overflow=20,
)

# Crear la sesión
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

# Base para los modelos
Base = declarative_base()


def get_db() -> Generator:
    """
    Generador que proporciona una sesión de base de datos
    para inyectar en las rutas de FastAPI
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def test_connection():
    """
    Función para probar la conexión a la base de datos
    """
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        return True, "Conexión a la base de datos exitosa"
    except Exception as e:
        return False, f"Error en la conexión: {str(e)}"
