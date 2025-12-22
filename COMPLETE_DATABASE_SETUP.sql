-- ============================================================================
-- SCRIPT COMPLETO PARA CREAR LA BASE DE DATOS "UNIDAD_EDUCATIVA"
-- Ejecutar directamente en PG Admin
-- ============================================================================

-- 1. CREAR LA BASE DE DATOS
CREATE DATABASE unidad_educativa
    WITH
    ENCODING = 'UTF8'
    LC_COLLATE = 'en_US.UTF-8'
    LC_CTYPE = 'en_US.UTF-8';

-- Conectarse a la base de datos (en PG Admin, seleccionar la BD primero)
-- \c unidad_educativa

-- ============================================================================
-- 2. CREAR TIPOS ENUM (MAYÚSCULAS)
-- ============================================================================
CREATE TYPE estado_matricula AS ENUM ('REGISTRADO', 'MATRICULADO', 'ACTIVO', 'SUSPENDIDO', 'RETIRADO', 'GRADUADO');
CREATE TYPE estado_asistencia AS ENUM ('PRESENTE', 'AUSENTE', 'ATRASO', 'JUSTIFICADO');

-- ============================================================================
-- 3. TABLA REPRESENTANTE
-- ============================================================================
CREATE TABLE representantes (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    telefono VARCHAR(20) NOT NULL
);

-- ============================================================================
-- 4. TABLA ESTUDIANTE
-- ============================================================================
CREATE TABLE estudiantes (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    cedula VARCHAR(20) UNIQUE NOT NULL,
    fecha_nacimiento DATE NOT NULL,
    correo VARCHAR(100),
    representante_id INT,
    CONSTRAINT fk_estudiante_representante FOREIGN KEY (representante_id) 
        REFERENCES representantes(id)
);

-- ============================================================================
-- 5. TABLA DOCENTE
-- ============================================================================
CREATE TABLE docentes (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    titulo VARCHAR(100),
    correo VARCHAR(100) UNIQUE NOT NULL
);

-- ============================================================================
-- 6. TABLA CURSO
-- ============================================================================
CREATE TABLE cursos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    nivel VARCHAR(50) NOT NULL
);

-- ============================================================================
-- 7. TABLA ASIGNATURA
-- ============================================================================
CREATE TABLE asignaturas (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    curso_id INT NOT NULL,
    docente_id INT,
    CONSTRAINT fk_asignatura_curso FOREIGN KEY (curso_id) REFERENCES cursos(id),
    CONSTRAINT fk_asignatura_docente FOREIGN KEY (docente_id) REFERENCES docentes(id)
);

-- ============================================================================
-- 8. TABLA MATRICULA
-- ============================================================================
CREATE TABLE matriculas (
    id SERIAL PRIMARY KEY,
    fecha DATE NOT NULL DEFAULT CURRENT_DATE,
    estudiante_id INT NOT NULL,
    curso_id INT NOT NULL,
    estado estado_matricula DEFAULT 'REGISTRADO',
    CONSTRAINT fk_matricula_estudiante FOREIGN KEY (estudiante_id) REFERENCES estudiantes(id),
    CONSTRAINT fk_matricula_curso FOREIGN KEY (curso_id) REFERENCES cursos(id)
);

-- ============================================================================
-- 9. TABLA CALIFICACION
-- ============================================================================
CREATE TABLE calificaciones (
    id SERIAL PRIMARY KEY,
    nota FLOAT NOT NULL CHECK (nota >= 0 AND nota <= 10),
    quimestre INT NOT NULL,
    matricula_id INT NOT NULL,
    asignatura_id INT NOT NULL,
    CONSTRAINT fk_calificacion_matricula FOREIGN KEY (matricula_id) REFERENCES matriculas(id),
    CONSTRAINT fk_calificacion_asignatura FOREIGN KEY (asignatura_id) REFERENCES asignaturas(id)
);

-- ============================================================================
-- 10. TABLA ASISTENCIA
-- ============================================================================
CREATE TABLE asistencias (
    id SERIAL PRIMARY KEY,
    fecha DATE NOT NULL DEFAULT CURRENT_DATE,
    estado estado_asistencia NOT NULL,
    matricula_id INT NOT NULL,
    asignatura_id INT NOT NULL,
    CONSTRAINT fk_asistencia_matricula FOREIGN KEY (matricula_id) REFERENCES matriculas(id),
    CONSTRAINT fk_asistencia_asignatura FOREIGN KEY (asignatura_id) REFERENCES asignaturas(id)
);

-- ============================================================================
-- DATOS DE PRUEBA (20 REGISTROS POR TABLA)
-- ============================================================================

-- Insertar Representantes (20 registros)
INSERT INTO representantes (nombre, telefono) VALUES
('Carlos García', '+593-2-2123456'),
('María López', '+593-9-98765432'),
('Juan Pérez', '+593-2-2234567'),
('Ana Rodríguez', '+593-9-98876543'),
('Pedro Martínez', '+593-2-2345678'),
('Rosa Flores', '+593-9-98987654'),
('Luis Sánchez', '+593-2-2456789'),
('Carmen Díaz', '+593-9-99098765'),
('Diego Torres', '+593-2-2567890'),
('Elena Morales', '+593-9-99109876'),
('Roberto Acosta', '+593-2-2678901'),
('Sofía Ruiz', '+593-9-99210987'),
('Andrés Gómez', '+593-2-2789012'),
('Gabriela Castro', '+593-9-99321098'),
('Fernando Vargas', '+593-2-2890123'),
('Valentina Silva', '+593-9-99432109'),
('Mateo Rojas', '+593-2-2901234'),
('Martina Fuentes', '+593-9-99543210'),
('Sergio Navarro', '+593-2-2012345'),
('Catalina Ponce', '+593-9-99654321');

-- Insertar Docentes (20 registros)
INSERT INTO docentes (nombre, apellido, titulo, correo) VALUES
('David', 'Acosta', 'Licenciado en Educación Matemática', 'david.acosta@escuela.edu'),
('Patricia', 'Benítez', 'Ingeniera en Sistemas', 'patricia.benitez@escuela.edu'),
('Marcos', 'Cabrera', 'Licenciado en Lengua Española', 'marcos.cabrera@escuela.edu'),
('Lorena', 'Delgado', 'Bióloga', 'lorena.delgado@escuela.edu'),
('Gustavo', 'Espinoza', 'Licenciado en Historia', 'gustavo.espinoza@escuela.edu'),
('Claudia', 'Fernández', 'Física', 'claudia.fernandez@escuela.edu'),
('Jorge', 'González', 'Licenciado en Educación Física', 'jorge.gonzalez@escuela.edu'),
('Beatriz', 'Hernández', 'Química', 'beatriz.hernandez@escuela.edu'),
('Alberto', 'Iglesias', 'Licenciado en Artes', 'alberto.iglesias@escuela.edu'),
('Verónica', 'Jiménez', 'Educadora Inicial', 'veronica.jimenez@escuela.edu'),
('Héctor', 'Keller', 'Licenciado en Inglés', 'hector.keller@escuela.edu'),
('Irene', 'López', 'Trabajadora Social', 'irene.lopez@escuela.edu'),
('Manuel', 'Montoya', 'Contador Público', 'manuel.montoya@escuela.edu'),
('Natalia', 'Navarro', 'Psicóloga', 'natalia.navarro@escuela.edu'),
('Oscar', 'Ortiz', 'Licenciado en Informática', 'oscar.ortiz@escuela.edu'),
('Priscila', 'Padrón', 'Bibliotecaria', 'priscila.padron@escuela.edu'),
('Raúl', 'Quintero', 'Ingeniero Civil', 'raul.quintero@escuela.edu'),
('Sandra', 'Ramírez', 'Nutricionista', 'sandra.ramirez@escuela.edu'),
('Tomás', 'Salas', 'Licenciado en Geografía', 'tomas.salas@escuela.edu'),
('Úrsula', 'Torres', 'Musicóloga', 'ursula.torres@escuela.edu');

-- Insertar Cursos (20 registros)
INSERT INTO cursos (nombre, nivel) VALUES
('Primero A', 'Primero'),
('Primero B', 'Primero'),
('Segundo A', 'Segundo'),
('Segundo B', 'Segundo'),
('Tercero A', 'Tercero'),
('Tercero B', 'Tercero'),
('Cuarto A', 'Cuarto'),
('Cuarto B', 'Cuarto'),
('Quinto A', 'Quinto'),
('Quinto B', 'Quinto'),
('Sexto A', 'Sexto'),
('Sexto B', 'Sexto'),
('Séptimo A', 'Séptimo'),
('Séptimo B', 'Séptimo'),
('Octavo A', 'Octavo'),
('Octavo B', 'Octavo'),
('Noveno A', 'Noveno'),
('Noveno B', 'Noveno'),
('Décimo A', 'Décimo'),
('Décimo B', 'Décimo');

-- Insertar Estudiantes (20 registros)
INSERT INTO estudiantes (nombre, apellido, cedula, fecha_nacimiento, correo, representante_id) VALUES
('Juan', 'Rodríguez', '1001234567', '2015-03-21', 'juan.rodriguez@estudiante.edu', 1),
('María', 'García', '1001234568', '2014-07-15', 'maria.garcia@estudiante.edu', 2),
('Carlos', 'López', '1001234569', '2016-01-10', 'carlos.lopez@estudiante.edu', 3),
('Ana', 'Martínez', '1001234570', '2015-05-22', 'ana.martinez@estudiante.edu', 4),
('Luis', 'Pérez', '1001234571', '2014-09-18', 'luis.perez@estudiante.edu', 5),
('Rosa', 'Sánchez', '1001234572', '2015-11-30', 'rosa.sanchez@estudiante.edu', 6),
('Pedro', 'Flores', '1001234573', '2016-02-14', 'pedro.flores@estudiante.edu', 7),
('Carmen', 'Torres', '1001234574', '2015-08-25', 'carmen.torres@estudiante.edu', 8),
('Diego', 'Díaz', '1001234575', '2014-12-03', 'diego.diaz@estudiante.edu', 9),
('Elena', 'Morales', '1001234576', '2015-04-19', 'elena.morales@estudiante.edu', 10),
('Roberto', 'Acosta', '1001234577', '2016-06-11', 'roberto.acosta@estudiante.edu', 11),
('Sofía', 'Ruiz', '1001234578', '2015-10-08', 'sofia.ruiz@estudiante.edu', 12),
('Andrés', 'Gómez', '1001234579', '2014-02-27', 'andres.gomez@estudiante.edu', 13),
('Gabriela', 'Castro', '1001234580', '2015-09-13', 'gabriela.castro@estudiante.edu', 14),
('Fernando', 'Vargas', '1001234581', '2016-03-05', 'fernando.vargas@estudiante.edu', 15),
('Valentina', 'Silva', '1001234582', '2015-07-20', 'valentina.silva@estudiante.edu', 16),
('Mateo', 'Rojas', '1001234583', '2014-11-09', 'mateo.rojas@estudiante.edu', 17),
('Martina', 'Fuentes', '1001234584', '2015-01-31', 'martina.fuentes@estudiante.edu', 18),
('Sergio', 'Navarro', '1001234585', '2016-05-16', 'sergio.navarro@estudiante.edu', 19),
('Catalina', 'Ponce', '1001234586', '2015-12-24', 'catalina.ponce@estudiante.edu', 20);

-- Insertar Asignaturas (20 registros)
INSERT INTO asignaturas (nombre, descripcion, curso_id, docente_id) VALUES
('Matemática', 'Curso de matemática básica', 1, 1),
('Lengua Española', 'Curso de lenguaje y comunicación', 1, 3),
('Ciencias Naturales', 'Estudio de biología y química', 2, 4),
('Historia', 'Historia del Ecuador y mundo', 2, 5),
('Educación Física', 'Actividades físicas y deporte', 3, 7),
('Artes', 'Expresión artística', 3, 9),
('Inglés', 'Idioma inglés básico', 4, 11),
('Informática', 'Computación e internet', 4, 15),
('Geografía', 'Geografía mundial', 5, 19),
('Música', 'Teoría y práctica musical', 5, 20),
('Física', 'Mecánica y energía', 6, 6),
('Química', 'Reacciones químicas', 6, 8),
('Biología', 'Estructura de organismos', 7, 4),
('Educación Cívica', 'Derechos y deberes', 7, 2),
('Literatura', 'Análisis de obras literarias', 8, 3),
('Psicología', 'Desarrollo psicológico', 8, 14),
('Economía', 'Principios económicos', 9, 13),
('Nutrición', 'Alimentación saludable', 9, 18),
('Filosofía', 'Pensamiento crítico', 10, 12),
('Religión', 'Educación religiosa', 10, 16);

-- Insertar Matrículas (20 registros)
INSERT INTO matriculas (fecha, estudiante_id, curso_id, estado) VALUES
('2024-01-15', 1, 1, 'ACTIVO'),
('2024-01-15', 2, 2, 'ACTIVO'),
('2024-01-15', 3, 3, 'ACTIVO'),
('2024-01-15', 4, 4, 'ACTIVO'),
('2024-01-15', 5, 5, 'ACTIVO'),
('2024-01-15', 6, 6, 'ACTIVO'),
('2024-01-15', 7, 7, 'ACTIVO'),
('2024-01-15', 8, 8, 'ACTIVO'),
('2024-01-15', 9, 9, 'ACTIVO'),
('2024-01-15', 10, 10, 'ACTIVO'),
('2024-01-15', 11, 11, 'ACTIVO'),
('2024-01-15', 12, 12, 'ACTIVO'),
('2024-01-15', 13, 13, 'ACTIVO'),
('2024-01-15', 14, 14, 'ACTIVO'),
('2024-01-15', 15, 15, 'ACTIVO'),
('2024-01-15', 16, 16, 'ACTIVO'),
('2024-01-15', 17, 17, 'MATRICULADO'),
('2024-01-15', 18, 18, 'MATRICULADO'),
('2024-01-15', 19, 19, 'REGISTRADO'),
('2024-01-15', 20, 20, 'REGISTRADO');

-- Insertar Calificaciones (20 registros)
INSERT INTO calificaciones (nota, quimestre, matricula_id, asignatura_id) VALUES
(8.5, 1, 1, 1),
(9.0, 1, 2, 2),
(7.5, 1, 3, 3),
(8.0, 1, 4, 4),
(9.5, 1, 5, 5),
(7.0, 1, 6, 6),
(8.5, 1, 7, 7),
(9.0, 1, 8, 8),
(7.5, 1, 9, 9),
(8.0, 1, 10, 10),
(9.5, 2, 11, 11),
(7.0, 2, 12, 12),
(8.5, 2, 13, 13),
(9.0, 2, 14, 14),
(7.5, 2, 15, 15),
(8.0, 2, 16, 16),
(9.5, 3, 17, 17),
(7.0, 3, 18, 18),
(8.5, 3, 19, 19),
(9.0, 3, 20, 20);

-- Insertar Asistencias (20 registros)
INSERT INTO asistencias (fecha, estado, matricula_id, asignatura_id) VALUES
('2024-12-15', 'PRESENTE', 1, 1),
('2024-12-15', 'PRESENTE', 2, 2),
('2024-12-15', 'PRESENTE', 3, 3),
('2024-12-15', 'AUSENTE', 4, 4),
('2024-12-15', 'PRESENTE', 5, 5),
('2024-12-15', 'ATRASO', 6, 6),
('2024-12-15', 'PRESENTE', 7, 7),
('2024-12-15', 'JUSTIFICADO', 8, 8),
('2024-12-15', 'PRESENTE', 9, 9),
('2024-12-15', 'PRESENTE', 10, 10),
('2024-12-15', 'AUSENTE', 11, 11),
('2024-12-15', 'PRESENTE', 12, 12),
('2024-12-15', 'ATRASO', 13, 13),
('2024-12-15', 'PRESENTE', 14, 14),
('2024-12-15', 'JUSTIFICADO', 15, 15),
('2024-12-15', 'PRESENTE', 16, 16),
('2024-12-15', 'PRESENTE', 17, 17),
('2024-12-15', 'PRESENTE', 18, 18),
('2024-12-15', 'AUSENTE', 19, 19),
('2024-12-15', 'PRESENTE', 20, 20);

-- ============================================================================
-- VERIFICACIÓN
-- ============================================================================
SELECT 'Representantes: ' || COUNT(*) FROM representantes;
SELECT 'Docentes: ' || COUNT(*) FROM docentes;
SELECT 'Cursos: ' || COUNT(*) FROM cursos;
SELECT 'Estudiantes: ' || COUNT(*) FROM estudiantes;
SELECT 'Asignaturas: ' || COUNT(*) FROM asignaturas;
SELECT 'Matrículas: ' || COUNT(*) FROM matriculas;
SELECT 'Calificaciones: ' || COUNT(*) FROM calificaciones;
SELECT 'Asistencias: ' || COUNT(*) FROM asistencias;
