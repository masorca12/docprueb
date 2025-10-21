import unittest
import tkinter as tk
from unittest.mock import Mock
from calculator import CalculatorApp

class TestCalculatorGUI(unittest.TestCase):
    """Clase de pruebas automatizadas para la interfaz de la calculadora."""

    def setUp(self):
        """
        Configura el entorno de prueba antes de cada test.
        Crea una instancia de la aplicación en una ventana virtual.
        """
        self.root = tk.Tk()
        # Ocultamos la ventana para que no aparezca durante las pruebas
        self.app = CalculatorApp(self.root)
        # Actualizamos la interfaz para asegurar que todos los widgets estén creados
        self.root.update()

    def tearDown(self):
        """
        Limpia el entorno después de cada prueba.
        Destruye la ventana de la aplicación.
        """
        self.root.destroy()

    def test_sum_operation(self):
        """
        Prueba una operación de suma simulando clics en los botones.
        Verifica que la pantalla muestre el resultado correcto.
        """
        print("\nEjecutando prueba de suma en GUI...")

        # 1. Simular clic en el botón '5'
        self.app.on_button_click('5')
        self.assertEqual(self.app.display_var.get(), "5")
        print("Clic '5' -> Pantalla muestra '5'")

        # 2. Simular clic en el botón '+'
        self.app.on_button_click('+')
        self.assertEqual(self.app.display_var.get(), "5+")
        print("Clic '+' -> Pantalla muestra '5+'")
        
        # 3. Simular clic en el botón '3'
        self.app.on_button_click('3')
        self.assertEqual(self.app.display_var.get(), "5+3")
        print("Clic '3' -> Pantalla muestra '5+3'")
        
        # 4. Simular clic en el botón '='
        self.app.on_button_click('=')
        self.assertEqual(self.app.display_var.get(), "8.0")
        print("Clic '=' -> Pantalla muestra '8.0'. ¡Prueba exitosa! ✅")

    def test_clear_button(self):
        """
        Prueba que el botón 'C' limpie la pantalla correctamente.
        """
        print("\nEjecutando prueba del botón Limpiar (C)...")
        
        # 1. Ingresar una expresión
        self.app.on_button_click('1')
        self.app.on_button_click('2')
        self.app.on_button_click('*')
        self.app.on_button_click('3')
        self.assertEqual(self.app.display_var.get(), "12*3")
        print("Ingresado '12*3'")
        
        # 2. Simular clic en el botón 'C'
        self.app.clear_display()
        self.assertEqual(self.app.display_var.get(), "")
        print("Clic 'C' -> Pantalla vacía. ¡Prueba exitosa! ✅")

if __name__ == '__main__':
    unittest.main()