import unittest
import tkinter as tk
from calculator import CalculatorApp

class TestIntegrationCalculatorGUI(unittest.TestCase):
    """
    Prueba de integración que simula un flujo de usuario completo.
    """

    def setUp(self):
        self.root = tk.Tk()
        self.app = CalculatorApp(self.root)

    def tearDown(self):
        self.root.destroy()

    def test_chained_addition_and_multiplication(self):
        """
        ID: IT-GUI-001
        Simula los clics del usuario para la operación: 5 + 3 * 2 = 16
        (El resultado esperado es 11.0, pero la app permite continuar con la
        operación sobre el resultado, asi que probaremos 5+3=8, y 8*2=16)
        """
        # Simula: Usuario presiona '5', '+', '3', '='
        print("\nSimulando clics para '5 + 3 = 8'")
        self.app.on_button_click('5')
        self.app.on_button_click('+')
        self.app.on_button_click('3')
        self.app.on_button_click('=') # Llama a calculate()
        self.assertEqual(self.app.display_var.get(), "8", "El resultado de 5+3 debe ser 8")

        # La app guarda el resultado '8' en self.expression para continuar
        print("Simulando clics para 'resultado (8) * 2 = 16'")
        self.app.on_button_click('*')
        self.app.on_button_click('2')
        self.app.on_button_click('=') # Llama a calculate() de nuevo
        self.assertEqual(self.app.display_var.get(), "16", "El resultado de 8*2 debe ser 16")
        print("\n✅ Prueba de Integración (Operaciones encadenadas): ¡Éxito!")

# Para ejecutar: python -m unittest test_integration_gui.py