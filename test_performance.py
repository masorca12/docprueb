import time
import tkinter as tk
from calculator import CalculatorApp

def run_performance_test():
    """
    Mide el rendimiento del método calculate() de la app.
    """
    # 1. Preparamos el entorno de la prueba
    root = tk.Tk()
    app = CalculatorApp(root)

    # 2. Definimos la carga de trabajo
    expression_to_test = "123.456 * 789.012"
    num_repetitions = 100_000

    print(f"\n🚀 Ejecutando prueba de rendimiento...")
    print(f"Operación: '{expression_to_test}' repetida {num_repetitions:,} veces.")

    # 3. Ejecutamos y medimos el tiempo
    start_time = time.perf_counter()

    for _ in range(num_repetitions):
        app.expression = expression_to_test
        app.calculate()

    end_time = time.perf_counter()
    total_time = end_time - start_time

    # 4. Calculamos y mostramos los resultados
    average_time_ms = (total_time / num_repetitions) * 1000 # Convertir a milisegundos

    print(f"\nResultados:")
    print(f"  - Tiempo total: {total_time:.4f} segundos.")
    print(f"  - Tiempo promedio por cálculo: {average_time_ms:.6f} milisegundos.")

    # Limpiamos la ventana de Tkinter
    root.destroy()

if __name__ == "__main__":
    run_performance_test()