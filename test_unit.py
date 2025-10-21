import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    """Clase de pruebas unitarias para la calculadora."""

    def setUp(self):
        """Configura una instancia de la calculadora antes de cada prueba."""
        self.calculator = Calculator()

    def test_add(self):
        """Prueba que la suma de dos números sea correcta."""
        self.assertEqual(self.calculator.add(5, 3), 8)
        print("Prueba unitaria de suma: ¡Éxito! ✅")

if __name__ == '__main__':
    unittest.main()