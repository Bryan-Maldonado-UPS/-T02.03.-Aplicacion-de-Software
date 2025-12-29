class BaseDatosNotas:
    """Clase simulada para conexión a base de datos."""
    def obtener_notas(self, estudiante_id):
        # Simulación de llamada a BD
        pass

def calcular_promedio(notas):
    """
    Calcula el promedio de una lista de notas.
    
    Requisito 7.3.2: Uso de Doctest.
    
    >>> calcular_promedio([10, 20, 30])
    20.0
    >>> calcular_promedio([5, 5, 5, 5])
    5.0
    >>> calcular_promedio([])
    0.0
    """
    if not notas:
        return 0.0
    return sum(notas) / len(notas)