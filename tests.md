# Documentación de Pruebas: Proyecto Calculadora

Este documento describe las pruebas implementadas para asegurar la calidad y el correcto funcionamiento de la calculadora en Python.

## 1. Pruebas Unitarias

Las pruebas unitarias se centran en verificar el funcionamiento de los componentes individuales (métodos) de la clase `Calculator`.

### Caso de Prueba: `test_add`

* **ID:** UT-001
* **Componente:** Método `add(a, b)`
* **Descripción:** Esta prueba verifica que la suma de dos números enteros positivos produce el resultado esperado.
* **Pasos de Ejecución:**
    1.  Crear una instancia de la clase `Calculator`.
    2.  Llamar al método `add` con los argumentos `5` y `3`.
* **Resultado Esperado:** El método debe devolver el valor `8`.
* **Estado:** Implementado y exitoso. ✅

## 2. Pruebas de Integración

Las pruebas de integración evalúan cómo interactúan diferentes partes del sistema. En este caso, se prueba la ejecución secuencial de varias operaciones.

### Caso de Prueba: `test_chained_operations`

* **ID:** IT-001
* **Componentes:** Métodos `add`, `multiply`, `divide`.
* **Descripción:** Se prueba una secuencia de operaciones matemáticas para asegurar que el resultado de una operación se pasa correctamente como entrada a la siguiente.
* **Pasos de Ejecución:**
    1.  Sumar `10 + 5`.
    2.  Multiplicar el resultado (`15`) por `2`.
    3.  Dividir el resultado (`30`) entre `3`.
* **Resultado Esperado:** El resultado final de la cadena de operaciones debe ser `10`.
* **Estado:** Implementado y exitoso. ✅

## 3. Pruebas de Rendimiento

Estas pruebas miden la eficiencia y la capacidad de respuesta de la aplicación bajo una carga de trabajo específica.

### Caso de Prueba: `performance_test_multiply`

* **ID:** PT-001
* **Componente:** Método `multiply(a, b)`
* **Descripción:** Medir el tiempo promedio que toma ejecutar la operación de multiplicación un millón de veces para evaluar su eficiencia.
* **Métrica Clave:** Tiempo de ejecución por operación.
* **Pasos de Ejecución:**
    1.  Configurar un entorno de prueba con la clase `Calculator`.
    2.  Ejecutar el método `multiply(150, 25)` en un bucle de `1,000,000` de veces.
    3.  Calcular el tiempo total y el tiempo promedio por operación.
* **Resultado Esperado:** El tiempo de ejecución promedio por operación debe ser bajo (generalmente en el rango de nanosegundos en hardware moderno), lo que indica que la función no tiene cuellos de botella significativos.
* **Estado:** Propuesta definida. 📈