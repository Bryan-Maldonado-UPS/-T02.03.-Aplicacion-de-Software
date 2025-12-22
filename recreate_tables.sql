-- Crear tipos ENUM nuevos con mayúsculas
CREATE TYPE estado_matricula AS ENUM ('REGISTRADO', 'MATRICULADO', 'ACTIVO', 'SUSPENDIDO', 'RETIRADO', 'GRADUADO');
CREATE TYPE estado_asistencia AS ENUM ('PRESENTE', 'AUSENTE', 'ATRASO', 'JUSTIFICADO');

-- Crear tabla Matricula
CREATE TABLE matriculas (
    id SERIAL PRIMARY KEY,
    fecha DATE NOT NULL DEFAULT CURRENT_DATE,
    estudiante_id INT NOT NULL,
    curso_id INT NOT NULL,
    estado estado_matricula DEFAULT 'REGISTRADO',
    CONSTRAINT fk_matricula_estudiante FOREIGN KEY (estudiante_id) REFERENCES estudiantes(id),
    CONSTRAINT fk_matricula_curso FOREIGN KEY (curso_id) REFERENCES cursos(id)
);

-- Crear tabla Calificacion
CREATE TABLE calificaciones (
    id SERIAL PRIMARY KEY,
    nota FLOAT NOT NULL CHECK (nota >= 0 AND nota <= 10),
    quimestre INT NOT NULL,
    matricula_id INT NOT NULL,
    asignatura_id INT NOT NULL,
    CONSTRAINT fk_calificacion_matricula FOREIGN KEY (matricula_id) REFERENCES matriculas(id),
    CONSTRAINT fk_calificacion_asignatura FOREIGN KEY (asignatura_id) REFERENCES asignaturas(id)
);

-- Crear tabla Asistencia
CREATE TABLE asistencias (
    id SERIAL PRIMARY KEY,
    fecha DATE NOT NULL DEFAULT CURRENT_DATE,
    estado estado_asistencia NOT NULL,
    matricula_id INT NOT NULL,
    asignatura_id INT NOT NULL,
    CONSTRAINT fk_asistencia_matricula FOREIGN KEY (matricula_id) REFERENCES matriculas(id),
    CONSTRAINT fk_asistencia_asignatura FOREIGN KEY (asignatura_id) REFERENCES asignaturas(id)
);
