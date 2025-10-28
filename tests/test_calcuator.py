# tests/test_calculator.py
import pytest
from unittest.mock import MagicMock
# Asegúrate de que Python pueda encontrar tu módulo en la carpeta src
import sys
sys.path.insert(0, './src')
from calculator_app import CalculatorApp

# Usamos un "fixture" de pytest para crear una instancia de la app para cada prueba
@pytest.fixture
def app():
    """Crea una instancia de la app sin iniciar la GUI de Tkinter."""
    # Mockeamos (simulamos) la ventana principal de Tkinter
    mock_root = MagicMock()
    calculator = CalculatorApp(mock_root)
    return calculator

def test_suma(app):
    """Prueba una suma simple."""
    app.expression = "5+3"
    app.calculate()
    assert app.expression == "8.0" # eval() a menudo devuelve flotantes

def test_resta(app):
    """Prueba una resta."""
    app.expression = "10-2"
    app.calculate()
    assert app.expression == "8.0"

def test_multiplicacion(app):
    """Prueba una multiplicación."""
    app.expression = "4*5"
    app.calculate()
    assert app.expression == "20.0"

def test_division(app):
    """Prueba una división válida."""
    app.expression = "10/2"
    app.calculate()
    assert app.expression == "5.0"

def test_division_por_cero(app):
    """Prueba el manejo del error de división por cero."""
    app.expression = "5/0"
    app.calculate()
    # Verificamos que la pantalla muestre "Error"
    app.display_var.set.assert_called_with("Error")
    assert app.expression == ""

def test_error_sintaxis(app):
    """Prueba el manejo de una expresión inválida."""
    app.expression = "5++2"
    app.calculate()
    app.display_var.set.assert_called_with("Error")
    assert app.expression == ""