"""
Script de prueba de Servicios y Validaciones
Demuestra la lógica de negocio en acción
"""
from datetime import date
from config.database import SessionLocal
from services import (
    EstudianteService, MatriculaService, CalificacionService,
    DocenteService, CursoService
)

def demostrar_validaciones():
    """Demuestra las validaciones de los servicios"""
    
    print("=" * 80)
    print("DEMOSTRACIÓN DE VALIDACIONES - LÓGICA DE NEGOCIO")
    print("=" * 80)
    print()
    
    db = SessionLocal()
    
    # ==================== PRUEBA 1: Validar cédula duplicada ====================
    print("1️⃣  PRUEBA: Cédula duplicada")
    print("-" * 80)
    est_service = EstudianteService(db)
    try:
        # Intentar crear con cédula existente
        estudiante = est_service.crear_estudiante(
            nombre="Fake",
            apellido="Student",
            cedula="1001234567",  # Ya existe
            fecha_nacimiento=date(2010, 1, 1),
            representante_id=1
        )
        print("✗ ERROR: Debería haber rechazado cédula duplicada")
    except ValueError as e:
        print(f"✓ Validación correcta: {e}")
    print()
    
    # ==================== PRUEBA 2: Validar edad mínima ====================
    print("2️⃣  PRUEBA: Edad mínima (menor de 5 años)")
    print("-" * 80)
    try:
        # Crear con fecha muy reciente
        estudiante = est_service.crear_estudiante(
            nombre="Bebé",
            apellido="Pequeño",
            cedula="9999999999",
            fecha_nacimiento=date.today(),  # Acaba de nacer
            representante_id=1
        )
        print("✗ ERROR: Debería haber rechazado edad mínima")
    except ValueError as e:
        print(f"✓ Validación correcta: {e}")
    print()
    
    # ==================== PRUEBA 3: Validar nota fuera de rango ====================
    print("3️⃣  PRUEBA: Calificación fuera de rango (nota > 10)")
    print("-" * 80)
    cal_service = CalificacionService(db)
    try:
        # Intentar crear calificación con nota > 10
        calificacion = cal_service.crear_calificacion(
            nota=15.0,  # Mayor a 10
            quimestre=1,
            matricula_id=1,
            asignatura_id=1
        )
        print("✗ ERROR: Debería haber rechazado nota > 10")
    except ValueError as e:
        print(f"✓ Validación correcta: {e}")
    print()
    
    # ==================== PRUEBA 4: Validar nota negativa ====================
    print("4️⃣  PRUEBA: Calificación negativa (nota < 0)")
    print("-" * 80)
    try:
        calificacion = cal_service.crear_calificacion(
            nota=-5.0,  # Negativa
            quimestre=1,
            matricula_id=1,
            asignatura_id=1
        )
        print("✗ ERROR: Debería haber rechazado nota < 0")
    except ValueError as e:
        print(f"✓ Validación correcta: {e}")
    print()
    
    # ==================== PRUEBA 5: Validar quimestre fuera de rango ====================
    print("5️⃣  PRUEBA: Quimestre inválido (quimestre > 3)")
    print("-" * 80)
    try:
        calificacion = cal_service.crear_calificacion(
            nota=8.5,
            quimestre=4,  # Solo 1-3 válidos
            matricula_id=1,
            asignatura_id=1
        )
        print("✗ ERROR: Debería haber rechazado quimestre 4")
    except ValueError as e:
        print(f"✓ Validación correcta: {e}")
    print()
    
    # ==================== PRUEBA 6: Validar matrícula duplicada ====================
    print("6️⃣  PRUEBA: Matrícula duplicada (estudiante ya en curso)")
    print("-" * 80)
    mat_service = MatriculaService(db)
    try:
        # Intentar matricular en un curso donde ya está
        matricula = mat_service.crear_matricula(
            estudiante_id=1,
            curso_id=1  # Ya está matriculado
        )
        print("✗ ERROR: Debería haber rechazado matrícula duplicada")
    except ValueError as e:
        print(f"✓ Validación correcta: {e}")
    print()
    
    # ==================== PRUEBA 7: Validar correo duplicado en docente ====================
    print("7️⃣  PRUEBA: Correo de docente duplicado")
    print("-" * 80)
    doc_service = DocenteService(db)
    try:
        # Intentar crear docente con correo existente
        docente = doc_service.crear_docente(
            nombre="Juan",
            apellido="Fake",
            correo="david.acosta@escuela.edu",  # Ya existe
            titulo="Licenciado en Algo"
        )
        print("✗ ERROR: Debería haber rechazado correo duplicado")
    except ValueError as e:
        print(f"✓ Validación correcta: {e}")
    print()
    
    # ==================== PRUEBA 8: Validar referencia a entidad inexistente ====================
    print("8️⃣  PRUEBA: Referencia a representante inexistente")
    print("-" * 80)
    try:
        # Crear estudiante con representante que no existe
        estudiante = est_service.crear_estudiante(
            nombre="Test",
            apellido="User",
            cedula="8888888888",
            fecha_nacimiento=date(2010, 1, 1),
            representante_id=9999  # No existe
        )
        print("✗ ERROR: Debería haber rechazado representante inexistente")
    except ValueError as e:
        print(f"✓ Validación correcta: {e}")
    print()
    
    # ==================== PRUEBA 9: Validar nota válida ====================
    print("9️⃣  PRUEBA: Crear calificación válida (nota = 8.5)")
    print("-" * 80)
    try:
        calificacion = cal_service.crear_calificacion(
            nota=8.5,
            quimestre=1,
            matricula_id=1,
            asignatura_id=1
        )
        print(f"✓ Calificación creada exitosamente")
        print(f"  - ID: {calificacion.id}")
        print(f"  - Nota: {calificacion.nota}")
        print(f"  - Quimestre: {calificacion.quimestre}")
        
        # Limpiar (eliminar la calificación creada)
        cal_service.eliminar_calificacion(calificacion.id)
        print(f"✓ Calificación eliminada para limpiar la prueba")
    except Exception as e:
        print(f"✗ Error: {e}")
    print()
    
    # ==================== PRUEBA 10: Listar estudiantes ====================
    print("🔟 PRUEBA: Listar y contar registros")
    print("-" * 80)
    try:
        estudiantes = est_service.listar_estudiantes(limit=5)
        print(f"✓ Primeros 5 estudiantes:")
        for est in estudiantes:
            print(f"  - {est.id}: {est.nombre} {est.apellido} (Cédula: {est.cedula})")
        
        total = est_service.repo.count()
        print(f"✓ Total de estudiantes en la BD: {total}")
    except Exception as e:
        print(f"✗ Error: {e}")
    print()
    
    db.close()
    
    print("=" * 80)
    print("✅ DEMOSTRACIÓN COMPLETADA")
    print("=" * 80)

if __name__ == "__main__":
    demostrar_validaciones()
