"""
Script para validar los datos insertados en la BD local
"""
import psycopg2
from psycopg2.extras import RealDictCursor

def validate_seed_data():
    """Validar datos de prueba insertados"""
    
    # Conexión a la BD local
    try:
        conn = psycopg2.connect(
            host="host.docker.internal",
            user="postgres",
            password="abcd.1234",
            database="unidad_educativa",
            port=5432
        )
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        print("✓ Conectado a la base de datos local\n")
        
    except Exception as e:
        print(f"✗ Error de conexión: {e}")
        return
    
    try:
        # Validar conteos
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
        
        print("=" * 70)
        print("VALIDACIÓN DE DATOS INSERTADOS")
        print("=" * 70)
        print("\n📊 Total de registros por tabla:\n")
        
        all_ok = True
        for table_name, count in stats.items():
            status = "✓" if count == 20 else "✗"
            print(f"  {status} {table_name:20} : {count:3d} registros")
            if count != 20:
                all_ok = False
        
        print()
        
        # Mostrar algunas muestras
        print("=" * 70)
        print("MUESTRAS DE DATOS")
        print("=" * 70)
        
        print("\n👥 Primeros 3 Estudiantes:")
        cursor.execute("SELECT id, nombre, apellido, cedula FROM estudiantes ORDER BY id LIMIT 3")
        for row in cursor.fetchall():
            print(f"   {row['id']} - {row['nombre']} {row['apellido']} ({row['cedula']})")
        
        print("\n🏫 Primeros 3 Docentes:")
        cursor.execute("SELECT id, nombre, apellido, titulo FROM docentes ORDER BY id LIMIT 3")
        for row in cursor.fetchall():
            print(f"   {row['id']} - {row['nombre']} {row['apellido']} ({row['titulo']})")
        
        print("\n📚 Primeros 3 Cursos:")
        cursor.execute("SELECT id, nombre, nivel FROM cursos ORDER BY id LIMIT 3")
        for row in cursor.fetchall():
            print(f"   {row['id']} - {row['nombre']} ({row['nivel']})")
        
        print("\n📋 Primeros 3 Matrículas:")
        cursor.execute("SELECT m.id, e.nombre, c.nombre as curso, m.estado FROM matriculas m JOIN estudiantes e ON m.estudiante_id = e.id JOIN cursos c ON m.curso_id = c.id ORDER BY m.id LIMIT 3")
        for row in cursor.fetchall():
            print(f"   {row['id']} - {row['nombre']} en {row['curso']} ({row['estado']})")
        
        print("\n")
        print("=" * 70)
        if all_ok:
            print("✅ VALIDACIÓN EXITOSA: Todos los datos han sido insertados correctamente")
        else:
            print("⚠️  VALIDACIÓN PARCIAL: Algunos registros no coinciden con el esperado")
        print("=" * 70)
        
    except Exception as e:
        print(f"✗ Error durante la validación: {e}")
    
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    validate_seed_data()
