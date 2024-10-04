import customtkinter as ctk
from interfaz import InterfazGaussJordan

if __name__ == "__main__":
    ventana = ctk.CTk()
    app = InterfazGaussJordan(ventana)
    ventana.mainloop()
