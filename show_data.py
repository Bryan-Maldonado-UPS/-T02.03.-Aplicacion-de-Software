"""
Script para consultar y mostrar datos de la base de datos
"""
import psycopg2
from psycopg2.extras import RealDictCursor
import json

def get_connection():
    """Crear conexión a la base de datos"""
    try:
        conn = psycopg2.connect(
            host="localhost",
            user="postgres",
            password="abcd.1234",
            database="unidad_educativa",
            port=5432
        )
        return conn
    except Exception as e:
        print(f"Error de conexión: {e}")
        return None

def show_sample_data():
    """Mostrar datos de muestra de cada tabla"""
    conn = get_connection()
    if not conn:
        return
    
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    
    tables_queries = {
        "Representantes": "SELECT id, nombre, telefono FROM representantes LIMIT 3",
        "Estudiantes": "SELECT id, nombre, apellido, cedula FROM estudiantes LIMIT 3",
        "Docentes": "SELECT id, nombre, apellido, titulo FROM docentes LIMIT 3",
        "Cursos": "SELECT id, nombre, nivel FROM cursos LIMIT 3",
        "Asignaturas": "SELECT id, nombre, descripcion FROM asignaturas LIMIT 3",
        "Matrículas": "SELECT id, estudiante_id, curso_id, estado FROM matriculas LIMIT 3",
        "Calificaciones": "SELECT id, nota, quimestre, matricula_id FROM calificaciones LIMIT 3",
        "Asistencias": "SELECT id, fecha, estado, matricula_id FROM asistencias LIMIT 3"
    }
    
    print("=" * 80)
    print("DATOS DE MUESTRA DE LA BASE DE DATOS")
    print("=" * 80)
    
    for table_name, query in tables_queries.items():
        print(f"\n📊 {table_name}:")
        print("-" * 80)
        
        cursor.execute(query)
        rows = cursor.fetchall()
        
        if rows:
            # Mostrar encabezados
            headers = list(rows[0].keys())
            print("  " + " | ".join(f"{h:20}" for h in headers))
            print("  " + "-" * 77)
            
            # Mostrar datos
            for row in rows:
                values = [str(row[h])[:20] for h in headers]
                print("  " + " | ".join(f"{v:20}" for v in values))
        else:
            print("  No hay datos")
    
    # Mostrar estadísticas
    print("\n" + "=" * 80)
    print("ESTADÍSTICAS GENERALES")
    print("=" * 80)
    
    stats_query = """
    SELECT 
        (SELECT COUNT(*) FROM representantes) as representantes,
        (SELECT COUNT(*) FROM estudiantes) as estudiantes,
        (SELECT COUNT(*) FROM docentes) as docentes,
        (SELECT COUNT(*) FROM cursos) as cursos,
        (SELECT COUNT(*) FROM asignaturas) as asignaturas,
        (SELECT COUNT(*) FROM matriculas) as matriculas,
        (SELECT COUNT(*) FROM calificaciones) as calificaciones,
        (SELECT COUNT(*) FROM asistencias) as asistencias
    """
    
    cursor.execute(stats_query)
    stats = cursor.fetchone()
    
    print("\n✓ Total de registros por tabla:")
    for key, value in stats.items():
        print(f"  • {key:20}: {value}")
    
    cursor.close()
    conn.close()
    print("\n" + "=" * 80)

if __name__ == "__main__":
    show_sample_data()
