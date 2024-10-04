import customtkinter as ctk  # Importa la biblioteca customtkinter para crear la interfaz gráfica
from tkinter import messagebox  # Importa messagebox para mostrar mensajes de error
from gauss_jordan import GaussJordan  # Importa la clase GaussJordan que contiene la lógica de resolución

class InterfazGaussJordan:
    def __init__(self, ventana):
        # Inicializa la interfaz con la ventana principal
        self.ventana = ventana
        self.ventana.title("Gauss-Jordan 3x3")  # Título de la ventana
        self.ventana.geometry("600x500")  # Tamaño de la ventana

        ctk.set_appearance_mode("dark")  # Establece el modo de apariencia oscuro
        ctk.set_default_color_theme("dark-blue")  # Define el tema de color oscuro

        self.gauss_jordan = GaussJordan()  # Crea una instancia de GaussJordan para resolver matrices

        # Crea un marco (frame) para contener los elementos de la interfaz
        self.frame = ctk.CTkFrame(self.ventana)
        self.frame.pack(padx=20, pady=20, fill="both", expand=True)

        # Inicializa una lista para almacenar las entradas de la matriz
        self.entradas = []
        for i in range(3):  # Crea 3 filas
            fila = []
            for j in range(4):  # Crea 4 columnas
                # Crea una entrada (Entry) para cada elemento de la matriz
                entrada = ctk.CTkEntry(self.frame, width=80, height=40, font=("Helvetica", 16), justify="center")
                entrada.grid(row=i, column=j, padx=10, pady=10)  # Coloca la entrada en la cuadrícula
                fila.append(entrada)  # Añade la entrada a la fila
            self.entradas.append(fila)  # Añade la fila a la lista de entradas

        # Crea un botón para resolver la matriz
        self.boton_resolver = ctk.CTkButton(self.frame, text="Resolver", command=self.resolver)
        self.boton_resolver.grid(row=3, column=0, columnspan=4, pady=20)  # Coloca el botón en la cuadrícula

        # Crea un cuadro de texto para mostrar los resultados
        self.resultado_texto = ctk.CTkTextbox(self.frame, height=200, width=525)
        self.resultado_texto.grid(row=4, column=0, columnspan=4, padx=10, pady=10)  # Coloca el cuadro de texto

    def resolver(self):
        # Método que se llama al presionar el botón "Resolver"
        try:
            # Extrae los valores de las entradas y los convierte a flotantes para formar la matriz
            matriz = [[float(entrada.get()) for entrada in fila] for fila in self.entradas]
            solucion, pasos = self.gauss_jordan.resolver(matriz)  # Resuelve la matriz usando Gauss-Jordan

            # Limpia el cuadro de texto y muestra los pasos de resolución
            self.resultado_texto.delete(1.0, "end")  # Borra el contenido anterior
            self.resultado_texto.insert("end", "Pasos de resolución:\n\n")
            for i, paso in enumerate(pasos):  # Itera sobre los pasos y los muestra
                self.resultado_texto.insert("end", f"Paso {i + 1}:\n{paso}\n\n")

            # Muestra la solución final
            self.resultado_texto.insert("end", "Solución:\n")
            self.resultado_texto.insert("end", f"x = {solucion[0][3]:.3f}\n")
            self.resultado_texto.insert("end", f"y = {solucion[1][3]:.3f}\n")
            self.resultado_texto.insert("end", f"z = {solucion[2][3]:.3f}\n")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese números válidos en todas las celdas.")  # Manejo de error por entradas no numéricas
        except ZeroDivisionError:
            messagebox.showerror("Error", "Error: No se puede dividir por cero.")  # Manejo de error por división entre cero
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {str(e)}")  # Manejo de cualquier otro error
