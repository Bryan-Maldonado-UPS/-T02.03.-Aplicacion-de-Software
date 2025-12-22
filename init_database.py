"""
Script para crear la base de datos y ejecutar el schema SQL
"""
import psycopg2
from psycopg2 import sql

def create_database():
    """
    Crear la base de datos 'unidad_educativa'
    """
    # Conexión a PostgreSQL (base de datos por defecto)
    conn = psycopg2.connect(
        host="localhost",
        user="postgres",
        password="abcd.1234",
        port=5432
    )
    conn.autocommit = True
    cursor = conn.cursor()
    
    try:
        # Verificar si la base de datos ya existe
        cursor.execute("SELECT 1 FROM pg_database WHERE datname = 'unidad_educativa'")
        if cursor.fetchone():
            print("✓ Base de datos 'unidad_educativa' ya existe")
        else:
            cursor.execute("CREATE DATABASE unidad_educativa")
            print("✓ Base de datos 'unidad_educativa' creada exitosamente")
    except Exception as e:
        print(f"✗ Error al crear base de datos: {e}")
    finally:
        cursor.close()
        conn.close()


def execute_schema():
    """
    Ejecutar el script SQL para crear tablas
    """
    try:
        conn = psycopg2.connect(
            host="localhost",
            user="postgres",
            password="abcd.1234",
            port=5432,
            database="unidad_educativa"
        )
        cursor = conn.cursor()
        
        # Leer y ejecutar el script SQL
        with open("init_db.sql", "r") as f:
            sql_script = f.read()
        
        cursor.execute(sql_script)
        conn.commit()
        print("✓ Script SQL ejecutado exitosamente")
        print("✓ Todas las tablas y tipos han sido creados")
        
    except Exception as e:
        print(f"✗ Error al ejecutar script SQL: {e}")
    finally:
        cursor.close()
        conn.close()


if __name__ == "__main__":
    print("=== Inicializando Base de Datos ===\n")
    print("1. Creando base de datos...")
    create_database()
    print("\n2. Ejecutando schema SQL...")
    execute_schema()
    print("\n=== Proceso completado ===")
