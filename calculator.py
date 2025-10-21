class Calculator:
    """Una clase de calculadora simple."""

    def add(self, a, b):
        """Suma dos números."""
        return a + b

    def subtract(self, a, b):
        """Resta dos números."""
        return a - b

    def multiply(self, a, b):
        """Multiplica dos números."""
        return a * b

    def divide(self, a, b):
        """Divide dos números. Lanza un error si se divide por cero."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b