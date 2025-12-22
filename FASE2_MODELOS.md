"""
FASE 2: MODELOS SQLALCHEMY - RESUMEN
====================================

Este documento describe los modelos SQLAlchemy creados para la aplicación.
"""

# ESTRUCTURA DE MODELOS CREADOS
# ==============================

# 1. ENUMERACIONES (models/enums.py)
# ===================================
"""
EstadoMatricula:
  - Registrado: Estado inicial cuando se registra
  - Matriculado: Después de confirmar matrícula
  - Activo: Estudiante activo en el curso
  - Suspendido: Temporalmente suspendido
  - Retirado: Retirado del curso
  - Graduado: Completó el curso

EstadoAsistencia:
  - Presente: Asistió
  - Ausente: No asistió
  - Atraso: Llegó tarde
  - Justificado: Falta justificada
"""

# 2. MODELOS BASE
# ===============

"""
Representante (models/representante.py)
├─ id: Integer (PK)
├─ nombre: String(100) - Requerido
├─ telefono: String(20) - Requerido
└─ Relaciones:
   └─ estudiantes: 1→N (cascade delete)

Docente (models/docente.py)
├─ id: Integer (PK)
├─ nombre: String(100) - Requerido
├─ apellido: String(100) - Requerido
├─ titulo: String(100) - Opcional
├─ correo: String(100) - Requerido, Único
└─ Relaciones:
   └─ asignaturas: 1→N (cascade delete)

Curso (models/curso.py)
├─ id: Integer (PK)
├─ nombre: String(50) - Requerido
├─ nivel: String(50) - Requerido
└─ Relaciones:
   ├─ asignaturas: 1→N (cascade delete)
   └─ matriculas: 1→N (cascade delete)
"""

# 3. MODELOS CON RELACIONES
# ==========================

"""
Estudiante (models/estudiante.py)
├─ id: Integer (PK)
├─ nombre: String(100) - Requerido
├─ apellido: String(100) - Requerido
├─ cedula: String(20) - Requerido, Único
├─ fecha_nacimiento: Date - Requerido
├─ correo: String(100) - Opcional
├─ representante_id: Integer (FK → representantes.id)
└─ Relaciones:
   ├─ representante: N→1 (Representante)
   └─ matriculas: 1→N (cascade delete)

Asignatura (models/asignatura.py)
├─ id: Integer (PK)
├─ nombre: String(100) - Requerido
├─ descripcion: Text - Opcional
├─ curso_id: Integer (FK → cursos.id) - Requerido
├─ docente_id: Integer (FK → docentes.id) - Opcional
└─ Relaciones:
   ├─ curso: N→1 (Curso)
   ├─ docente: N→1 (Docente)
   ├─ calificaciones: 1→N (cascade delete)
   └─ asistencias: 1→N (cascade delete)

Matricula (models/matricula.py) ⭐ CON ENUM
├─ id: Integer (PK)
├─ fecha: Date - Requerido (default: hoy)
├─ estudiante_id: Integer (FK → estudiantes.id) - Requerido
├─ curso_id: Integer (FK → cursos.id) - Requerido
├─ estado: Enum(EstadoMatricula) - Default: REGISTRADO
└─ Relaciones:
   ├─ estudiante: N→1 (Estudiante)
   ├─ curso: N→1 (Curso)
   ├─ calificaciones: 1→N (cascade delete)
   └─ asistencias: 1→N (cascade delete)

Calificacion (models/calificacion.py)
├─ id: Integer (PK)
├─ nota: Float - Requerido (rango 0-10)
├─ quimestre: Integer - Requerido
├─ matricula_id: Integer (FK → matriculas.id) - Requerido
├─ asignatura_id: Integer (FK → asignaturas.id) - Requerido
└─ Relaciones:
   ├─ matricula: N→1 (Matricula)
   └─ asignatura: N→1 (Asignatura)

Asistencia (models/asistencia.py) ⭐ CON ENUM
├─ id: Integer (PK)
├─ fecha: Date - Requerido (default: hoy)
├─ estado: Enum(EstadoAsistencia) - Requerido
├─ matricula_id: Integer (FK → matriculas.id) - Requerido
├─ asignatura_id: Integer (FK → asignaturas.id) - Requerido
└─ Relaciones:
   ├─ matricula: N→1 (Matricula)
   └─ asignatura: N→1 (Asignatura)
"""

# DIAGRAMA DE RELACIONES
# ======================

"""
                ┌─────────────────┐
                │  Representante  │
                └────────┬────────┘
                         │ 1:N
                         │
                    ┌────▼────────┐
                    │ Estudiante  │
                    └────┬────────┘
                         │ 1:N
                    ┌────▼─────────┐
                    │  Matricula   │◄──── Enum(EstadoMatricula)
                    └────┬────┬────┘
                    ┌────┘    └────┐
                    │              │ 1:N
               1:N  │              │
            ┌──────┴────┐      ┌───▼──────────────┐
            │  Docente  │      │ Asistencia ◄────┤ Enum(EstadoAsistencia)
            └──────┬────┘      └───┬──────────────┘
                   │ 1:N           │ N:1
                   │         ┌─────▼─────────┐
            ┌──────▼────────┐│ Asignatura    │
            │  Docente      ││               │
            └──────────┬────┘└─────┬─────────┘
                       │ 1:N       │ N:1
                       │    ┌──────▼──────┐
                       │    │   Curso     │
                       │    └──────┬──────┘
                       │           │ 1:N
                   ┌───▼───────────▼────┐
                   │  Calificacion      │
                   └────────────────────┘
"""

# VALIDACIONES Y CONSTRAINTS
# ==========================

"""
✓ Cedula: ÚNICA por estudiante
✓ Correo Docente: ÚNICO por docente
✓ Nota (Calificación): 0-10
✓ Estados: Enumerados (no texto libre)
✓ Fechas: Defaults a fecha actual
✓ Foreign Keys: Con cascade delete para integridad referencial
✓ NOT NULL: Aplicados en campos requeridos
"""

# ARCHIVOS CREADOS
# ================

"""
models/
├── __init__.py           # Importa todos los modelos
├── enums.py             # Enumeraciones
├── representante.py     # Modelo Representante
├── estudiante.py        # Modelo Estudiante
├── docente.py           # Modelo Docente
├── curso.py             # Modelo Curso
├── asignatura.py        # Modelo Asignatura
├── matricula.py         # Modelo Matricula (con Enum)
├── asistencia.py        # Modelo Asistencia (con Enum)
└── calificacion.py      # Modelo Calificacion
"""

# USO EN CÓDIGO
# =============

"""
# Importar todos los modelos
from models import *

# O importar específicos
from models import Estudiante, Matricula, EstadoMatricula
from config.database import SessionLocal

# Usar en queries
db = SessionLocal()

# Crear un estudiante
estudiante = Estudiante(
    nombre="Juan",
    apellido="Pérez",
    cedula="1001234567",
    fecha_nacimiento=date(2010, 5, 15),
    representante_id=1
)
db.add(estudiante)

# Consultar matrículas activas
activas = db.query(Matricula).filter(
    Matricula.estado == EstadoMatricula.ACTIVO
).all()

# Relacionar datos
estudiante = db.query(Estudiante).first()
print(estudiante.nombre)  # Acceso a nombre
print(estudiante.representante.nombre)  # Acceso a representante

db.close()
"""
