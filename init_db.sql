-- 1. Limpieza inicial (Opcional: borra tablas si ya existían para evitar errores al recrear)
DROP TABLE IF EXISTS asistencias;
DROP TABLE IF EXISTS calificaciones;
DROP TABLE IF EXISTS matriculas;
DROP TABLE IF EXISTS asignaturas;
DROP TABLE IF EXISTS cursos;
DROP TABLE IF EXISTS docentes;
DROP TABLE IF EXISTS estudiantes;
DROP TABLE IF EXISTS representantes;
DROP TYPE IF EXISTS estado_matricula;
DROP TYPE IF EXISTS estado_asistencia;

-- 2. Crear Tipos de Datos (ENUMs) para los estados
-- Basado en tu diagrama de estados
CREATE TYPE estado_matricula AS ENUM ('REGISTRADO', 'MATRICULADO', 'ACTIVO', 'SUSPENDIDO', 'RETIRADO', 'GRADUADO');
CREATE TYPE estado_asistencia AS ENUM ('PRESENTE', 'AUSENTE', 'ATRASO', 'JUSTIFICADO');

-- 3. Tabla Representante
CREATE TABLE representantes (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    telefono VARCHAR(20) NOT NULL
);

-- 4. Tabla Estudiante
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

-- 5. Tabla Docente
CREATE TABLE docentes (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    titulo VARCHAR(100),
    correo VARCHAR(100) UNIQUE NOT NULL
);

-- 6. Tabla Curso
CREATE TABLE cursos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    nivel VARCHAR(50) NOT NULL
);

-- 7. Tabla Asignatura
CREATE TABLE asignaturas (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    curso_id INT NOT NULL,
    docente_id INT,
    CONSTRAINT fk_asignatura_curso FOREIGN KEY (curso_id) REFERENCES cursos(id),
    CONSTRAINT fk_asignatura_docente FOREIGN KEY (docente_id) REFERENCES docentes(id)
);

-- 8. Tabla Matricula
CREATE TABLE matriculas (
    id SERIAL PRIMARY KEY,
    fecha DATE NOT NULL DEFAULT CURRENT_DATE,
    estudiante_id INT NOT NULL,
    curso_id INT NOT NULL,
    estado estado_matricula DEFAULT 'REGISTRADO', 
    CONSTRAINT fk_matricula_estudiante FOREIGN KEY (estudiante_id) REFERENCES estudiantes(id),
    CONSTRAINT fk_matricula_curso FOREIGN KEY (curso_id) REFERENCES cursos(id)
);

-- 9. Tabla Calificacion
CREATE TABLE calificaciones (
    id SERIAL PRIMARY KEY,
    nota FLOAT NOT NULL CHECK (nota >= 0 AND nota <= 10),
    quimestre INT NOT NULL,
    matricula_id INT NOT NULL,
    asignatura_id INT NOT NULL,
    CONSTRAINT fk_calificacion_matricula FOREIGN KEY (matricula_id) REFERENCES matriculas(id),
    CONSTRAINT fk_calificacion_asignatura FOREIGN KEY (asignatura_id) REFERENCES asignaturas(id)
);

-- 10. Tabla Asistencia
CREATE TABLE asistencias (
    id SERIAL PRIMARY KEY,
    fecha DATE NOT NULL DEFAULT CURRENT_DATE,
    estado estado_asistencia NOT NULL,
    matricula_id INT NOT NULL,
    asignatura_id INT NOT NULL,
    CONSTRAINT fk_asistencia_matricula FOREIGN KEY (matricula_id) REFERENCES matriculas(id),
    CONSTRAINT fk_asistencia_asignatura FOREIGN KEY (asignatura_id) REFERENCES asignaturas(id)
);
