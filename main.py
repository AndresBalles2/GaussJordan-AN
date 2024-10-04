import customtkinter as ctk  # Importa la biblioteca customtkinter para crear interfaces gráficas
from interfaz import InterfazGaussJordan  # Importa la clase InterfazGaussJordan desde el módulo interfaz

# Este bloque se ejecuta solo si el script se ejecuta directamente
if __name__ == "__main__":
    ventana = ctk.CTk()  # Crea una nueva ventana principal usando customtkinter
    app = InterfazGaussJordan(ventana)  # Crea una instancia de la interfaz de Gauss-Jordan, pasando la ventana
    ventana.mainloop()  # Inicia el bucle principal de la aplicación, esperando eventos del usuario
