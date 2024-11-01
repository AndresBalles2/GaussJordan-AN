import customtkinter as ctk
from tkinter import messagebox
from gauss_jordan import GaussJordan

class InterfazGaussJordan:
    def __init__(self, ventana):
        # Inicialización de la ventana principal
        self.ventana = ventana
        self.ventana.title("Gauss-Jordan 3x3")
        self.ventana.geometry("1100x600")

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        self.gauss_jordan = GaussJordan()

        # Creación de la vista de pestañas
        self.tab_view = ctk.CTkTabview(self.ventana)
        self.tab_view.pack(padx=20, pady=20, fill="both", expand=True)

        # Pestaña principal para la interfaz de cálculo
        self.tab_calculo = self.tab_view.add("Cálculo Gauss-Jordan")
        self.crear_interfaz_calculo()

        # Pestaña para el Manual de Usuario
        self.tab_manual = self.tab_view.add("Manual de Usuario")
        self.crear_manual_usuario()

    def crear_interfaz_calculo(self):
        # Crea el marco y la interfaz de cálculo
        self.frame = ctk.CTkFrame(self.tab_calculo)
        self.frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Configuración de entradas y etiquetas
        self.entradas = []
        labels_texto = [
            ["Digite el valor de x1", "Digite el valor de y1", "Digite el valor de z1", "Digite el resultado 1"],
            ["Digite el valor de x2", "Digite el valor de y2", "Digite el valor de z2", "Digite el resultado 2"],
            ["Digite el valor de x3", "Digite el valor de y3", "Digite el valor de z3", "Digite el resultado 3"]
        ]

        for i in range(3):
            fila = []
            for j in range(4):
                entrada = ctk.CTkEntry(self.frame, width=80, height=40, font=("Helvetica", 16), justify="center")
                entrada.grid(row=i, column=j * 2, padx=10, pady=10)
                etiqueta = ctk.CTkLabel(self.frame, text=labels_texto[i][j], font=("Helvetica", 14))
                etiqueta.grid(row=i, column=j * 2 + 1, padx=10, pady=10)
                fila.append(entrada)
            self.entradas.append(fila)

        # Botón para resolver
        self.boton_resolver = ctk.CTkButton(self.frame, text="Resolver", command=self.resolver)
        self.boton_resolver.grid(row=3, column=0, columnspan=5, pady=20)

        # Botón para limpiar la matriz y el cuadro de resultados
        self.boton_limpiar = ctk.CTkButton(self.frame, text="Limpiar", command=self.limpiar)
        self.boton_limpiar.grid(row=3, column=4, columnspan=3, pady=20)

        # Cuadro de texto para mostrar resultados
        self.resultado_texto = ctk.CTkTextbox(self.frame, height=200, width=650)
        self.resultado_texto.grid(row=4, column=0, columnspan=8, padx=10, pady=10)

    def crear_manual_usuario(self):
        # Crear cuadro de texto con barra de desplazamiento
        self.texto_manual = ctk.CTkTextbox(self.tab_manual, height=450, width=1000)
        self.texto_manual.pack(padx=20, pady=20, fill="both", expand=True)

        # Contenido del Manual de Usuario
        manual_texto = """
Manual de Usuario: Método de Eliminación Gauss-Jordan

Introducción:
Este programa utiliza el método de eliminación Gauss-Jordan para resolver sistemas de ecuaciones lineales de 3x3. 
El método de eliminación Gauss-Jordan convierte una matriz de coeficientes en una matriz identidad para resolver las 
variables de manera directa.

Instrucciones de Uso:
1. En la pestaña de "Cálculo Gauss-Jordan", ingrese los valores en las celdas correspondientes:
   - Las columnas x, y, z corresponden a los coeficientes de cada variable.
   - La última columna es el resultado de cada ecuación.
2. Una vez ingresados los datos, presione el botón "Resolver".
3. Los pasos y la solución aparecerán en el cuadro de texto inferior.

Qué puede hacer este programa:
- Resolver sistemas lineales de 3x3.
- Mostrar los pasos de cálculo.
- Gestionar errores de entrada y advertir sobre números grandes o divisiones por cero.

Limitaciones:
- Solo acepta matrices 3x3.
- No soporta sistemas inconsistentes o dependientes donde el determinante es 0.

Acerca del Método:
El método Gauss-Jordan es útil para resolver sistemas lineales mediante una serie de operaciones en filas 
hasta obtener una matriz identidad. Se utiliza frecuentemente en álgebra lineal para encontrar soluciones exactas.

Recomendaciones:
- Asegúrese de ingresar solo valores numéricos.
- Evite usar valores extremadamente grandes para prevenir errores de cálculo.

Puede regresar a la pestaña de "Cálculo Gauss-Jordan" para realizar cálculos adicionales.
"""
        # Insertar el texto en el cuadro de texto
        self.texto_manual.insert("1.0", manual_texto)
        self.texto_manual.configure(state="disabled")  # Desactivar edición

    def resolver(self):
        # Método para resolver el sistema de ecuaciones
        try:
            matriz = [[float(entrada.get()) for entrada in fila] for fila in self.entradas]
            solucion, pasos = self.gauss_jordan.resolver(matriz)

            # Mostrar pasos y solución en el cuadro de texto
            self.resultado_texto.delete(1.0, "end")
            self.resultado_texto.insert("end", "Pasos de resolución:\n\n")
            for i, paso in enumerate(pasos):
                self.resultado_texto.insert("end", f"Paso {i + 1}:\n{paso}\n\n")

            # Mostrar la solución final
            self.resultado_texto.insert("end", "Solución:\n")
            self.resultado_texto.insert("end", f"x = {solucion[0][3]:.4f}\n")
            self.resultado_texto.insert("end", f"y = {solucion[1][3]:.4f}\n")
            self.resultado_texto.insert("end", f"z = {solucion[2][3]:.4f}\n")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese números válidos en todas las celdas.")
        except ZeroDivisionError:
            messagebox.showerror("Error", "Error: No se puede dividir por cero.")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {str(e)}")

    def limpiar(self):
        # Limpia todas las entradas de la matriz
        for fila in self.entradas:
            for entrada in fila:
                entrada.delete(0, "end")

        # Limpia el cuadro de texto de resultados
        self.resultado_texto.delete(1.0, "end")
