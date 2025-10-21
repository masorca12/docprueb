import unittest
from calculator import Calculator

class TestIntegration(unittest.TestCase):
    """Clase de pruebas de integración para la calculadora."""

    def setUp(self):
        """Configura una instancia de la calculadora antes de cada prueba."""
        self.calculator = Calculator()

    def test_chained_operations(self):
        """
        Prueba una secuencia de operaciones: (10 + 5) * 2 / 3 = 10
        """
        sum_result = self.calculator.add(10, 5)
        multiply_result = self.calculator.multiply(sum_result, 2)
        final_result = self.calculator.divide(multiply_result, 3)
        self.assertEqual(final_result, 10)
        print("Prueba de integración de operaciones encadenadas: ¡Éxito! ✅")

if __name__ == '__main__':
    unittest.main()