import unittest
import pytest
from mockito import when, mock, verify, unstub
from utils import calcular_promedio, BaseDatosNotas


# Requisito 7.3.2: Implementación con Unittest
class TestCalculoPromedioUnittest(unittest.TestCase):
    def test_promedio_simple(self):
        self.assertEqual(calcular_promedio([10, 10]), 10.0)

    def test_lista_vacia(self):
        self.assertEqual(calcular_promedio([]), 0.0)

    def test_instancia_clase_base(self):
        # Instanciamos la clase real para asegurar cobertura de líneas de definición
        bd = BaseDatosNotas()
        assert bd.obtener_notas(1) is None

# Requisito 7.3.2: Implementación con Pytest
def test_promedio_valores_mixtos():
    assert calcular_promedio([0, 10]) == 5.0

def test_promedio_flotantes():
    assert abs(calcular_promedio([3.3, 3.3]) - 3.3) < 0.01

# Requisito 7.3.2: Implementación con Mockito
def test_interaccion_bd_con_mockito():
    # 1. Crear el Mock
    bd_mock = mock(BaseDatosNotas)
    
    # 2. Configurar el comportamiento (Stubbing)
    # Cuando se llame a obtener_notas(1), retornar [8, 9, 10]
    when(bd_mock).obtener_notas(1).thenReturn([8, 9, 10])
    
    # 3. Ejecutar la lógica usando el mock
    notas = bd_mock.obtener_notas(1)
    promedio = calcular_promedio(notas)
    
    # 4. Verificaciones (Asserts y Verify)
    assert promedio == 9.0
    
    # Verificar que el método fue llamado exactamente una vez con el argumento 1
    verify(bd_mock, times=1).obtener_notas(1)
    
    # Limpieza de mocks
    unstub()

if __name__ == '__main__':
    # Permite ejecutar este archivo directamente con python
    unittest.main()