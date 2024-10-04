import customtkinter as ctk
from tkinter import messagebox
from gauss_jordan import GaussJordan

class InterfazGaussJordan:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Gauss-Jordan 3x3")
        self.ventana.geometry("600x500")

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        
        self.gauss_jordan = GaussJordan()

        
        self.frame = ctk.CTkFrame(self.ventana)
        self.frame.pack(padx=20, pady=20, fill="both", expand=True)

        
        self.entradas = []
        for i in range(3):
            fila = []
            for j in range(4):
                entrada = ctk.CTkEntry(self.frame, width=80, height=40, font=("Helvetica", 16), justify="center")
                entrada.grid(row=i, column=j, padx=10, pady=10)
                fila.append(entrada)
            self.entradas.append(fila)

        
        self.boton_resolver = ctk.CTkButton(self.frame, text="Resolver", command=self.resolver)
        self.boton_resolver.grid(row=3, column=0, columnspan=4, pady=20)

        
        self.resultado_texto = ctk.CTkTextbox(self.frame, height=200, width=525)
        self.resultado_texto.grid(row=4, column=0, columnspan=4, padx=10, pady=10)

    def resolver(self):
        try:
            
            matriz = [[float(entrada.get()) for entrada in fila] for fila in self.entradas]
            solucion, pasos = self.gauss_jordan.resolver(matriz)

            
            self.resultado_texto.delete(1.0, "end")
            self.resultado_texto.insert("end", "Pasos de resolución:\n\n")
            for i, paso in enumerate(pasos):
                self.resultado_texto.insert("end", f"Paso {i + 1}:\n{paso}\n\n")

            self.resultado_texto.insert("end", "Solución:\n")
            self.resultado_texto.insert("end", f"x = {solucion[0][3]:.3f}\n")
            self.resultado_texto.insert("end", f"y = {solucion[1][3]:.3f}\n")
            self.resultado_texto.insert("end", f"z = {solucion[2][3]:.3f}\n")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese números válidos en todas las celdas.")
        except ZeroDivisionError:
            messagebox.showerror("Error", "Error: No se puede dividir por cero.")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {str(e)}")