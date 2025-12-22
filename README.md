## Distribución de tareas por integrante:
| Integrante | Rol Técnico | 
| :--- | :--- |
| *Kevin Barreno* | • *Infraestructura:* Dockerización del entorno (Dockerfile, docker-compose) y configuración de la base de datos.<br>• *Core:* Desarrollo del BaseRepository (Patrón Repositorio Genérico) y el módulo de *Representantes*. |
| *Bryan Maldonado* | • *Lógica de Personas:* Implementación de reglas de negocio críticas en services.py (ej. validación de edad mínima en Estudiantes).<br>• *Seguridad de Datos:* Validaciones de unicidad y formato en el módulo de *Docentes*. |
| *Alejandro Montesdeoca* | • *Estructura Académica:* Modelado y desarrollo de los módulos *Cursos* y *Asignaturas.<br>• **Integridad de Datos:* Implementación de relaciones complejas (Foreign Keys) para vincular la carga académica. |
| *Francisco Ocaña* | • *Procesos Transaccionales:* Desarrollo del núcleo del negocio: *Matrículas, **Calificaciones* y *Asistencias.<br>• **Reglas de Dominio:* Control de estados (Enums) y validaciones de rango en notas (0-10). |
| *Bryan Romero* | • *Quality Assurance:* Desarrollo de scripts de pruebas unitarias (test_services.py) cubriendo escenarios de éxito y error.
