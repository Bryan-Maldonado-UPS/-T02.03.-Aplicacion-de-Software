"""
Script para insertar 20 registros de prueba en cada tabla de la BD local
"""
import psycopg2
from psycopg2.extras import execute_values

def insert_seed_data():
    """Insertar datos de prueba en todas las tablas"""
    
    # Conexión a la BD local
    try:
        conn = psycopg2.connect(
            host="host.docker.internal",
            user="postgres",
            password="abcd.1234",
            database="unidad_educativa",
            port=5432
        )
        cursor = conn.cursor()
        print("✓ Conectado a la base de datos local")
        
    except Exception as e:
        print(f"✗ Error de conexión: {e}")
        return
    
    try:
        # 1. Insertar Representantes (20 registros)
        representantes_data = [
            ('Carlos García López', '0987654321'),
            ('María Rodríguez Pérez', '0987654322'),
            ('Juan Martínez Silva', '0987654323'),
            ('Rosa López García', '0987654324'),
            ('Pedro Sánchez Ruiz', '0987654325'),
            ('Ana Fernández García', '0987654326'),
            ('Luis González Martínez', '0987654327'),
            ('Isabel Ramírez López', '0987654328'),
            ('Fernando Torres García', '0987654329'),
            ('Sofía Díaz Pérez', '0987654330'),
            ('Raúl Moreno López', '0987654331'),
            ('Carolina Jiménez Silva', '0987654332'),
            ('Javier Romero García', '0987654333'),
            ('Daniela Castillo López', '0987654334'),
            ('Miguel Herrera Martínez', '0987654335'),
            ('Valeria Campos García', '0987654336'),
            ('Roberto Navarro Pérez', '0987654337'),
            ('Alejandra Vega López', '0987654338'),
            ('Andrés Mejía Silva', '0987654339'),
            ('Gabriela Reyes García', '0987654340'),
        ]
        cursor.execute("DELETE FROM representantes")
        execute_values(cursor, "INSERT INTO representantes (nombre, telefono) VALUES %s", representantes_data)
        print("✓ 20 Representantes insertados")
        
        # 2. Insertar Estudiantes (20 registros)
        estudiantes_data = [
            ('Juan', 'Pérez', '1001234567', '2010-05-15', 'juan.perez@escuela.edu', 1),
            ('María', 'García', '1001234568', '2010-08-22', 'maria.garcia@escuela.edu', 2),
            ('Carlos', 'López', '1001234569', '2010-03-10', 'carlos.lopez@escuela.edu', 3),
            ('Rosa', 'Martínez', '1001234570', '2010-11-05', 'rosa.martinez@escuela.edu', 4),
            ('Pedro', 'Rodríguez', '1001234571', '2010-07-18', 'pedro.rodriguez@escuela.edu', 5),
            ('Ana', 'Sánchez', '1001234572', '2010-09-30', 'ana.sanchez@escuela.edu', 6),
            ('Luis', 'Fernández', '1001234573', '2010-02-12', 'luis.fernandez@escuela.edu', 7),
            ('Isabel', 'González', '1001234574', '2010-06-25', 'isabel.gonzalez@escuela.edu', 8),
            ('Fernando', 'Torres', '1001234575', '2010-10-14', 'fernando.torres@escuela.edu', 9),
            ('Sofía', 'Díaz', '1001234576', '2010-04-08', 'sofia.diaz@escuela.edu', 10),
            ('Raúl', 'Moreno', '1001234577', '2010-12-20', 'raul.moreno@escuela.edu', 11),
            ('Carolina', 'Jiménez', '1001234578', '2010-01-03', 'carolina.jimenez@escuela.edu', 12),
            ('Javier', 'Romero', '1001234579', '2010-08-17', 'javier.romero@escuela.edu', 13),
            ('Daniela', 'Castillo', '1001234580', '2010-05-29', 'daniela.castillo@escuela.edu', 14),
            ('Miguel', 'Herrera', '1001234581', '2010-09-11', 'miguel.herrera@escuela.edu', 15),
            ('Valeria', 'Campos', '1001234582', '2010-03-27', 'valeria.campos@escuela.edu', 16),
            ('Roberto', 'Navarro', '1001234583', '2010-07-09', 'roberto.navarro@escuela.edu', 17),
            ('Alejandra', 'Vega', '1001234584', '2010-11-16', 'alejandra.vega@escuela.edu', 18),
            ('Andrés', 'Mejía', '1001234585', '2010-06-02', 'andres.mejia@escuela.edu', 19),
            ('Gabriela', 'Reyes', '1001234586', '2010-10-23', 'gabriela.reyes@escuela.edu', 20),
        ]
        cursor.execute("DELETE FROM estudiantes")
        execute_values(cursor, "INSERT INTO estudiantes (nombre, apellido, cedula, fecha_nacimiento, correo, representante_id) VALUES %s", estudiantes_data)
        print("✓ 20 Estudiantes insertados")
        
        # 3. Insertar Docentes (20 registros)
        docentes_data = [
            ('David', 'Acosta', 'Licenciado en Matemáticas', 'david.acosta@escuela.edu'),
            ('Elena', 'Blanco', 'Licenciada en Lengua', 'elena.blanco@escuela.edu'),
            ('Gonzalo', 'Campos', 'Licenciado en Física', 'gonzalo.campos@escuela.edu'),
            ('Hilda', 'Delgado', 'Licenciada en Química', 'hilda.delgado@escuela.edu'),
            ('Iván', 'Espinoza', 'Licenciado en Biología', 'ivan.espinoza@escuela.edu'),
            ('Juana', 'Fuentes', 'Licenciada en Historia', 'juana.fuentes@escuela.edu'),
            ('Karina', 'Gómez', 'Licenciada en Geografía', 'karina.gomez@escuela.edu'),
            ('Leonardo', 'Hernández', 'Licenciado en Informática', 'leonardo.hernandez@escuela.edu'),
            ('Mariana', 'Iglesias', 'Licenciada en Educación Física', 'mariana.iglesias@escuela.edu'),
            ('Nicolás', 'Jiménez', 'Licenciado en Artes', 'nicolas.jimenez@escuela.edu'),
            ('Oriana', 'Kemp', 'Licenciada en Inglés', 'oriana.kemp@escuela.edu'),
            ('Paulo', 'López', 'Licenciado en Filosofía', 'paulo.lopez@escuela.edu'),
            ('Quique', 'Morales', 'Licenciado en Música', 'quique.morales@escuela.edu'),
            ('Roxana', 'Niño', 'Licenciada en Sociales', 'roxana.nino@escuela.edu'),
            ('Sergio', 'Orozco', 'Licenciado en Tecnología', 'sergio.orozco@escuela.edu'),
            ('Tamara', 'Padilla', 'Licenciada en Psicología', 'tamara.padilla@escuela.edu'),
            ('Ulises', 'Quintero', 'Licenciado en Contabilidad', 'ulises.quintero@escuela.edu'),
            ('Verónica', 'Ríos', 'Licenciada en Administración', 'veronica.rios@escuela.edu'),
            ('Wilmer', 'Salas', 'Licenciado en Estadística', 'wilmer.salas@escuela.edu'),
            ('Ximena', 'Torres', 'Licenciada en Economía', 'ximena.torres@escuela.edu'),
        ]
        cursor.execute("DELETE FROM docentes")
        execute_values(cursor, "INSERT INTO docentes (nombre, apellido, titulo, correo) VALUES %s", docentes_data)
        print("✓ 20 Docentes insertados")
        
        # 4. Insertar Cursos (20 registros)
        cursos_data = [
            ('1A', 'Primero Básico'),
            ('1B', 'Primero Básico'),
            ('2A', 'Segundo Básico'),
            ('2B', 'Segundo Básico'),
            ('3A', 'Tercero Básico'),
            ('3B', 'Tercero Básico'),
            ('4A', 'Cuarto Básico'),
            ('4B', 'Cuarto Básico'),
            ('5A', 'Quinto Básico'),
            ('5B', 'Quinto Básico'),
            ('6A', 'Sexto Básico'),
            ('6B', 'Sexto Básico'),
            ('7A', 'Séptimo Básico'),
            ('7B', 'Séptimo Básico'),
            ('8A', 'Octavo Básico'),
            ('8B', 'Octavo Básico'),
            ('1M', 'Primero Medio'),
            ('2M', 'Segundo Medio'),
            ('3M', 'Tercero Medio'),
            ('4M', 'Cuarto Medio'),
        ]
        cursor.execute("DELETE FROM cursos")
        execute_values(cursor, "INSERT INTO cursos (nombre, nivel) VALUES %s", cursos_data)
        print("✓ 20 Cursos insertados")
        
        # 5. Insertar Asignaturas (20 registros)
        asignaturas_data = [
            ('Matemáticas', 'Estudio de números, álgebra y geometría', 1, 1),
            ('Lengua y Literatura', 'Lectura, escritura y comprensión de textos', 2, 2),
            ('Ciencias Naturales', 'Biología, física y química', 3, 3),
            ('Historia y Geografía', 'Historia universal y geografía física', 4, 6),
            ('Educación Física', 'Deporte y desarrollo físico', 5, 9),
            ('Artes Plásticas', 'Pintura, escultura y dibujo', 6, 10),
            ('Inglés', 'Aprendizaje del idioma inglés', 7, 11),
            ('Religión', 'Estudio de valores y ética', 8, 12),
            ('Tecnología', 'Introducción a la informática', 9, 15),
            ('Música', 'Teoría y práctica musical', 10, 13),
            ('Química', 'Estudio de elementos y reacciones químicas', 11, 4),
            ('Biología', 'Estudio de organismos vivos', 12, 5),
            ('Física', 'Mecánica, energía y ondas', 13, 3),
            ('Filosofía', 'Pensamiento crítico y ética', 14, 12),
            ('Sociología', 'Estudio de la sociedad', 15, 14),
            ('Economía', 'Principios económicos básicos', 16, 20),
            ('Estadística', 'Análisis de datos', 17, 19),
            ('Contabilidad', 'Registros y cuentas financieras', 18, 17),
            ('Administración', 'Gestión empresarial', 19, 18),
            ('Educación Cívica', 'Derechos y deberes ciudadanos', 20, 6),
        ]
        cursor.execute("DELETE FROM asignaturas")
        execute_values(cursor, "INSERT INTO asignaturas (nombre, descripcion, curso_id, docente_id) VALUES %s", asignaturas_data)
        print("✓ 20 Asignaturas insertadas")
        
        # 6. Insertar Matrículas (20 registros)
        matriculas_data = [
            ('2024-01-15', 1, 1, 'Activo'),
            ('2024-01-15', 2, 2, 'Activo'),
            ('2024-01-15', 3, 3, 'Activo'),
            ('2024-01-15', 4, 4, 'Activo'),
            ('2024-01-15', 5, 5, 'Activo'),
            ('2024-01-15', 6, 6, 'Activo'),
            ('2024-01-15', 7, 7, 'Activo'),
            ('2024-01-15', 8, 8, 'Activo'),
            ('2024-01-15', 9, 9, 'Activo'),
            ('2024-01-15', 10, 10, 'Activo'),
            ('2024-01-15', 11, 11, 'Activo'),
            ('2024-01-15', 12, 12, 'Activo'),
            ('2024-01-15', 13, 13, 'Activo'),
            ('2024-01-15', 14, 14, 'Activo'),
            ('2024-01-15', 15, 15, 'Activo'),
            ('2024-01-15', 16, 16, 'Activo'),
            ('2024-01-15', 17, 17, 'Matriculado'),
            ('2024-01-15', 18, 18, 'Matriculado'),
            ('2024-01-15', 19, 19, 'Registrado'),
            ('2024-01-15', 20, 20, 'Registrado'),
        ]
        cursor.execute("DELETE FROM matriculas")
        execute_values(cursor, "INSERT INTO matriculas (fecha, estudiante_id, curso_id, estado) VALUES %s", matriculas_data)
        print("✓ 20 Matrículas insertadas")
        
        # 7. Insertar Calificaciones (20 registros)
        calificaciones_data = [
            (8.5, 1, 1, 1),
            (9.0, 1, 2, 2),
            (7.5, 1, 3, 3),
            (8.0, 1, 4, 4),
            (9.5, 1, 5, 5),
            (8.2, 1, 6, 6),
            (7.8, 1, 7, 7),
            (9.3, 1, 8, 8),
            (8.7, 1, 9, 9),
            (8.9, 1, 10, 10),
            (7.6, 1, 11, 11),
            (8.4, 1, 12, 12),
            (9.1, 1, 13, 13),
            (8.3, 1, 14, 14),
            (7.9, 1, 15, 15),
            (8.6, 1, 16, 16),
            (9.2, 1, 17, 17),
            (8.1, 1, 18, 18),
            (7.7, 1, 19, 19),
            (8.8, 1, 20, 20),
        ]
        cursor.execute("DELETE FROM calificaciones")
        execute_values(cursor, "INSERT INTO calificaciones (nota, quimestre, matricula_id, asignatura_id) VALUES %s", calificaciones_data)
        print("✓ 20 Calificaciones insertadas")
        
        # 8. Insertar Asistencias (20 registros)
        asistencias_data = [
            ('2024-12-15', 'Presente', 1, 1),
            ('2024-12-15', 'Presente', 2, 2),
            ('2024-12-15', 'Presente', 3, 3),
            ('2024-12-15', 'Ausente', 4, 4),
            ('2024-12-15', 'Presente', 5, 5),
            ('2024-12-15', 'Atraso', 6, 6),
            ('2024-12-15', 'Presente', 7, 7),
            ('2024-12-15', 'Justificado', 8, 8),
            ('2024-12-15', 'Presente', 9, 9),
            ('2024-12-15', 'Presente', 10, 10),
            ('2024-12-15', 'Ausente', 11, 11),
            ('2024-12-15', 'Presente', 12, 12),
            ('2024-12-15', 'Atraso', 13, 13),
            ('2024-12-15', 'Presente', 14, 14),
            ('2024-12-15', 'Justificado', 15, 15),
            ('2024-12-15', 'Presente', 16, 16),
            ('2024-12-15', 'Presente', 17, 17),
            ('2024-12-15', 'Presente', 18, 18),
            ('2024-12-15', 'Ausente', 19, 19),
            ('2024-12-15', 'Presente', 20, 20),
        ]
        cursor.execute("DELETE FROM asistencias")
        execute_values(cursor, "INSERT INTO asistencias (fecha, estado, matricula_id, asignatura_id) VALUES %s", asistencias_data)
        print("✓ 20 Asistencias insertadas")
        
        conn.commit()
        print("\n✅ Todos los datos de prueba han sido insertados exitosamente")
        
    except Exception as e:
        conn.rollback()
        print(f"✗ Error durante la inserción: {e}")
    
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    print("=" * 60)
    print("INSERTANDO DATOS DE PRUEBA EN LA BASE DE DATOS LOCAL")
    print("=" * 60)
    print()
    insert_seed_data()
    print()
    print("=" * 60)
