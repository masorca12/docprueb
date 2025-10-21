# 📄 Documentación del Proyecto: Calculadora con GUI en Python

Este documento detalla la estructura, funcionamiento y pruebas del proyecto de calculadora con interfaz gráfica desarrollada en Python utilizando la biblioteca Tkinter.

---

## 📝 Descripción del Proyecto

El proyecto consiste en una aplicación de escritorio de una calculadora simple. La interfaz gráfica de usuario (GUI) permite a los usuarios realizar operaciones aritméticas básicas (`+`, `-`, `*`, `/`) haciendo clic en los botones.

**Funcionalidades clave:**
* **Interfaz visual**: Ventana con una pantalla para mostrar números y botones para la entrada de datos.
* **Operaciones básicas**: Realiza sumas, restas, multiplicaciones y divisiones.
* **Operaciones encadenadas**: Permite usar el resultado de una operación como el primer operando de la siguiente.
* **Manejo de errores**: Muestra "Error" en pantalla para operaciones inválidas, como la división por cero.
* **Botón de limpieza**: Un botón 'C' para reiniciar el estado de la calculadora.



---

## 📁 Estructura de Archivos

El proyecto está organizado en los siguientes archivos:

* **`calculator_app.py`**:
    * **Descripción**: Contiene el código fuente principal de la aplicación. Define la clase `CalculatorApp` que construye y gestiona la interfaz gráfica y la lógica de cálculo.
    * **Rol**: Es el archivo ejecutable para iniciar la calculadora.

* **`test_unit_gui.py`**:
    * **Descripción**: Contiene la **prueba unitaria** del proyecto. Utiliza el framework `unittest` para verificar una funcionalidad aislada y específica.
    * **Rol**: Asegura que el comportamiento del botón 'Limpiar' (C) funcione como se espera.

* **`test_integration_gui.py`**:
    * **Descripción**: Contiene la **prueba de integración**. Simula un flujo completo de acciones del usuario para verificar que múltiples componentes de la aplicación interactúan correctamente.
    * **Rol**: Valida una secuencia de operaciones encadenadas (ej. `5 + 3`, seguido de `* 2`).

* **`test_performance_gui.py`**:
    * **Descripción**: Contiene la **prueba de rendimiento**. Es un script que mide la eficiencia de la lógica de cálculo bajo una carga de trabajo intensiva.
    * **Rol**: Proporciona métricas sobre la velocidad del método `calculate()` al ejecutarlo miles de veces.

---

## 🚀 Guía de Ejecución

Para interactuar con el proyecto, sigue estos pasos desde tu terminal.

### 1. Ejecutar la Aplicación Principal

Para abrir y usar la calculadora, ejecuta el siguiente comando:
```sh
python calculator_app.py