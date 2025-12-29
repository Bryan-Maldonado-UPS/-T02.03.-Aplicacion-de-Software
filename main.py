from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from config.database import test_connection
from routes import api_router
from typing import List
import sys
import io
from utils import calcular_promedio


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

# --- ENDPOINTS DE PRUEBAS Y COBERTURA (Requisito 7.2 y 7.3.2) ---

@app.post("/calcular-promedio", tags=["Pruebas Unitarias"])
def api_calcular_promedio(notas: List[float]):
    """Endpoint para calcular el promedio enviando una lista de notas (Lógica de Negocio)."""
    resultado = calcular_promedio(notas)
    return {
        "notas_recibidas": notas,
        "promedio_calculado": resultado
    }

@app.get("/ejecutar-pruebas", response_class=HTMLResponse, tags=["Pruebas Unitarias"])
def api_run_tests():
    """
    Ejecuta las pruebas unitarias y de cobertura.
    
    Herramientas utilizadas:
    - **Doctest, Unittest, Pytest**: Ejecución de pruebas.
    - **Mockito**: Simulación de dependencias (Mocks).
    - **Coverage**: Análisis de cobertura (Requisito > 60%).
    """
    import pytest
    # Capturar la salida estándar (stdout)
    buffer = io.StringIO()
    sys.stdout = buffer
    
    # Ejecutar pytest: -v (verbose), --cov (cobertura), -s (permitir captura de stdout)
    # Se asume que .coveragerc ya está configurado en el directorio raíz
    pytest.main(["-v", "--cov", "--cov-report=term-missing", "--doctest-modules", "--ignore=routes", "-s"])
    
    # Restaurar stdout y devolver contenido
    sys.stdout = sys.__stdout__
    output = buffer.getvalue()
    
    # Analizar el resultado para determinar el color del encabezado
    header_color = "#4ec9b0" # Color por defecto
    status_title = "Reporte de Ejecución de Pruebas"
    
    if "FAIL Required test coverage" in output:
        header_color = "#ff5555" # Rojo si falla la cobertura
        status_title = "⚠️ FALLO: Cobertura menor al 60%"
    elif "Required test coverage" in output and "reached" in output:
        header_color = "#50fa7b" # Verde si pasa
        status_title = "✅ ÉXITO: Cobertura superior al 60%"

    return f"""
    <html>
        <head>
            <title>Reporte de Pruebas</title>
            <style>
                body {{ background-color: #1e1e1e; color: #d4d4d4; font-family: 'Consolas', 'Monaco', monospace; padding: 20px; }}
                pre {{ white-space: pre-wrap; background-color: #2d2d2d; padding: 15px; border-radius: 5px; border: 1px solid #444; }}
                h1 {{ color: {header_color}; border-bottom: 1px solid #444; padding-bottom: 10px; }}
                .subtitle {{ color: #888; margin-bottom: 20px; font-size: 0.9em; }}
            </style>
        </head>
        <body>
            <h1>{status_title}</h1>
            <div class="subtitle">Herramientas: Doctest, Unittest, Pytest, Coverage, Mockito</div>
            <pre>{output}</pre>
        </body>
    </html>
    """


if __name__ == "__main__":
    import uvicorn
    
    # Ejecutar el servidor
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        reload=True
    )
