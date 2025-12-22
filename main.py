from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config.database import test_connection
from routes import api_router

# Crear la aplicación FastAPI
app = FastAPI(
    title="Sistema de Gestión Educativa",
    description="API REST para gestionar una unidad educativa con validaciones completas",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

# Agregar CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir el router principal
app.include_router(api_router)


@app.get("/")
def read_root():
    """
    Endpoint raíz de la API
    """
    return {
        "mensaje": "Bienvenido al Sistema de Gestión Educativa",
        "versión": "1.0.0",
        "estado": "Producción",
        "documentación": "/docs",
        "redoc": "/redoc"
    }


@app.get("/health")
def health_check():
    """
    Endpoint para verificar la salud del servidor y la conexión a la base de datos
    """
    success, message = test_connection()
    return {
        "servidor": "activo",
        "base_datos": "conectada" if success else "desconectada",
        "detalles": message,
        "endpoints_disponibles": {
            "representantes": "/api/v1/representantes",
            "estudiantes": "/api/v1/estudiantes",
            "docentes": "/api/v1/docentes",
            "cursos": "/api/v1/cursos",
            "asignaturas": "/api/v1/asignaturas",
            "matriculas": "/api/v1/matriculas",
            "calificaciones": "/api/v1/calificaciones",
            "asistencias": "/api/v1/asistencias"
        }
    }


if __name__ == "__main__":
    import uvicorn
    
    # Ejecutar el servidor
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        reload=True
    )
