Documentación de Pruebas
A continuación se detalla el propósito de cada prueba implementada.

✅ Prueba Unitaria: test_clear_display_action
ID: UT-GUI-001

Objetivo: Verificar que la acción del botón 'C' (método clear_display) reinicia el estado de la calculadora de manera correcta y aislada.

Pasos Simulados:

Se establece un estado inicial en la calculadora (ej. la pantalla muestra "123+456").

Se invoca el método clear_display().

Resultado Esperado:

La variable interna self.expression debe ser una cadena vacía ("").

El texto visible en la pantalla (self.display_var) debe estar vacío.

🔗 Prueba de Integración: test_chained_addition_and_multiplication
ID: IT-GUI-001

Objetivo: Asegurar que los componentes de la GUI (botones, pantalla y lógica de cálculo) interactúan correctamente para completar un flujo de operaciones encadenadas.

Pasos Simulados:

Simular clics para la operación 5 + 3 =.

Verificar que la pantalla muestre 8.

Simular clics para continuar la operación * 2 =.

Resultado Esperado:

Después de la primera secuencia, la pantalla debe mostrar 8.

Al final del flujo, la pantalla debe mostrar el resultado final 16.

📈 Prueba de Rendimiento: run_performance_test
ID: PT-GUI-001

Objetivo: Medir la eficiencia del motor de cálculo (calculate()) para identificar posibles cuellos de botella y establecer una métrica de rendimiento base.

Metodología:

Se define una operación de cálculo (ej. "123.456 * 789.012").

Esta operación se ejecuta en un bucle un gran número de veces (ej. 100,000 repeticiones).

Se mide el tiempo total de ejecución.

Resultado Esperado:

El script no valida un "éxito" o "fracaso", sino que imprime en la consola el tiempo total y el tiempo promedio por operación. Esta métrica es útil para comparar el rendimiento antes y después de realizar cambios en el código.