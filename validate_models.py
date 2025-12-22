"""
Script de validación de modelos SQLAlchemy
Muestra la estructura de los modelos y sus relaciones
"""
from config.database import Base, SessionLocal
from models import (
    Representante, Estudiante, Docente, Curso, Asignatura,
    Matricula, Asistencia, Calificacion,
    EstadoMatricula, EstadoAsistencia
)
from sqlalchemy import inspect

def show_model_info():
    """Mostrar información detallada de los modelos"""
    
    print("=" * 80)
    print("INFORMACIÓN DE MODELOS SQLALCHEMY")
    print("=" * 80)
    print()
    
    models = [
        Representante,
        Estudiante,
        Docente,
        Curso,
        Asignatura,
        Matricula,
        Asistencia,
        Calificacion,
    ]
    
    for model in models:
        print(f"📋 Modelo: {model.__name__}")
        print(f"   Tabla: {model.__tablename__}")
        print(f"   Columnas:")
        
        mapper = inspect(model)
        for column in mapper.columns:
            col_type = str(column.type)
            nullable = "✓" if column.nullable else "✗"
            pk = "PK" if column.primary_key else ""
            fk = ""
            
            # Detectar claves foráneas
            if column.foreign_keys:
                fk = f"FK: {list(column.foreign_keys)[0].target_fullname}"
            
            print(f"      • {column.name:20} ({col_type:15}) {nullable:1} {pk:3} {fk}")
        
        # Mostrar relaciones
        if mapper.relationships:
            print(f"   Relaciones:")
            for rel in mapper.relationships:
                direction = "→" if rel.direction.name == "MANYTOONE" else "←"
                print(f"      {direction} {rel.key}: {rel.mapper.class_.__name__}")
        
        print()
    
    # Mostrar enumeraciones
    print("=" * 80)
    print("ENUMERACIONES")
    print("=" * 80)
    print()
    
    print("📌 EstadoMatricula:")
    for state in EstadoMatricula:
        print(f"   • {state.value}")
    
    print()
    print("📌 EstadoAsistencia:")
    for state in EstadoAsistencia:
        print(f"   • {state.value}")
    
    print()
    
    # Validar conexión a BD
    print("=" * 80)
    print("VALIDACIÓN DE CONEXIÓN A BASE DE DATOS")
    print("=" * 80)
    print()
    
    try:
        db = SessionLocal()
        
        # Contar registros en cada tabla
        counts = {
            "Representantes": db.query(Representante).count(),
            "Estudiantes": db.query(Estudiante).count(),
            "Docentes": db.query(Docente).count(),
            "Cursos": db.query(Curso).count(),
            "Asignaturas": db.query(Asignatura).count(),
            "Matrículas": db.query(Matricula).count(),
            "Asistencias": db.query(Asistencia).count(),
            "Calificaciones": db.query(Calificacion).count(),
        }
        
        print("✓ Conexión exitosa. Conteo de registros:\n")
        for table, count in counts.items():
            status = "✓" if count > 0 else "⚠"
            print(f"   {status} {table:20}: {count:3d} registros")
        
        db.close()
        
    except Exception as e:
        print(f"✗ Error en conexión: {e}")
    
    print()
    print("=" * 80)

if __name__ == "__main__":
    show_model_info()
