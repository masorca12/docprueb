import tkinter as tk

class CalculatorApp:
    """
    Una calculadora con una interfaz gráfica simple construida con Tkinter.
    """
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")
        self.root.geometry("400x500") # Tamaño de la ventana

        # Variable para almacenar la expresión matemática en la pantalla
        self.expression = ""

        # Pantalla de la calculadora
        self.display_var = tk.StringVar()
        display = tk.Entry(self.root, textvariable=self.display_var, font=('Arial', 24), bd=10, insertwidth=2, width=14, borderwidth=4, justify='right')
        display.grid(row=0, column=0, columnspan=4)

        # Creación de los botones
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ]

        for (text, row, col) in buttons:
            # Usamos una función lambda para pasar el valor del botón correctamente
            button = tk.Button(self.root, text=text, padx=35, pady=20, font=('Arial', 18),
                               command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, sticky="nsew")

        # Botón de limpiar (Clear)
        clear_button = tk.Button(self.root, text='C', padx=35, pady=20, font=('Arial', 18), command=self.clear_display)
        clear_button.grid(row=5, column=0, columnspan=4, sticky="nsew")

        # Configurar el peso de las filas y columnas para que se expandan
        for i in range(5):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)

    def on_button_click(self, char):
        """Maneja el evento de clic en un botón."""
        if char == '=':
            self.calculate()
        else:
            self.expression += str(char)
            self.update_display(self.expression)

    def calculate(self):
        """Calcula la expresión y muestra el resultado."""
        try:
            # 'eval' es una forma simple de evaluar una cadena como una expresión de Python.
            # ¡Cuidado! No es seguro usarlo con entradas de usuarios no confiables.
            result = str(eval(self.expression))
            self.update_display(result)
            self.expression = result # Permite continuar operando con el resultado
        except (SyntaxError, ZeroDivisionError):
            self.update_display("Error")
            self.expression = ""

    def clear_display(self):
        """Limpia la pantalla y la expresión."""
        self.expression = ""
        self.update_display("")

    def update_display(self, text):
        """Actualiza el texto en la pantalla."""
        self.display_var.set(text)

if __name__ == "__main__":
    main_window = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()