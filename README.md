## Distribución de tareas por integrante:
| Integrante | Rol Técnico | 
| :--- | :--- |
| *Kevin Barreno* | • *Infraestructura:* Dockerización del entorno (Dockerfile, docker-compose) y configuración de la base de datos.<br>• *Core:* Desarrollo del BaseRepository (Patrón Repositorio Genérico) y el módulo de *Representantes*. |
| *Bryan Maldonado* | • *Lógica de Personas:* Implementación de reglas de negocio críticas en services.py (ej. validación de edad mínima en Estudiantes).<br>• *Seguridad de Datos:* Validaciones de unicidad y formato en el módulo de *Docentes*. |
| *Alejandro Montesdeoca* | • *Estructura Académica:* Modelado y desarrollo de los módulos *Cursos* y *Asignaturas.<br>• **Integridad de Datos:* Implementación de relaciones complejas (Foreign Keys) para vincular la carga académica. |
| *Francisco Ocaña* | • *Procesos Transaccionales:* Desarrollo del núcleo del negocio: *Matrículas, **Calificaciones* y *Asistencias.<br>• **Reglas de Dominio:* Control de estados (Enums) y validaciones de rango en notas (0-10). |
| *Bryan Romero* | • *Quality Assurance:* Desarrollo de scripts de pruebas unitarias (test_services.py) cubriendo escenarios de éxito y error.

## Tarea T02.04
| Integrante       | Resumen de actividades realizadas                                                                                                                                                                                                                                                                          |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| *Bryan Maldonado* | Se encargó de la configuración del entorno de pruebas, instalando y configurando los frameworks requeridos para Python. Además, estableció el análisis de cobertura de código, asegurando que el proyecto cumpla con el mínimo del 60% de cobertura en los métodos |
| *Alejandro Montesdeoca* | Implementó y optimizó la lógica de negocio del sistema, incorporando pruebas integradas mediante Doctest para validar el comportamiento de los métodos principales. Realizó mejoras en el código para incrementar la cobertura de pruebas |
| *Kevin Barreno*| Desarrolló pruebas unitarias estructuradas utilizando Unittest y Pytest, validando de forma aislada las funciones y módulos del software desarrollado en la Tarea 02.03, garantizando la correcta funcionalidad del sistema.  |
| *Francisco Ocaña* | Implementó la simulación de dependencias externas mediante Mockito, permitiendo evaluar los componentes del sistema sin acoplamiento a recursos reales. Asimismo, colaboró en la validación de los resultados de cobertura |
| *Bryan Romero* | Integró la ejecución completa de las pruebas unitarias dentro del flujo del proyecto y realizó la validación final del sistema, verificando que todas las pruebas se ejecuten correctamente y que se cumpla el uso de los frameworks establecidos en los requisito |
