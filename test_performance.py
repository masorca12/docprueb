import timeit

# Código a ejecutar para la prueba
setup_code = "from calculator import Calculator; calculator = Calculator()"
statement_code = "calculator.multiply(150, 25)"

# Número de repeticiones
repetitions = 1000000

# Medición del tiempo
total_time = timeit.timeit(stmt=statement_code, setup=setup_code, number=repetitions)
average_time_ns = (total_time / repetitions) * 1e9  # Convertir a nanosegundos

print(f"Prueba de rendimiento: Multiplicación 📈")
print(f"Tiempo total para {repetitions} multiplicaciones: {total_time:.4f} segundos.")
print(f"Tiempo promedio por operación: {average_time_ns:.2f} nanosegundos.")