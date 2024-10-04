from operaciones_matriz import OperacionesMatriz  # Importa la clase OperacionesMatriz desde otro archivo

# Constructor de la clase GaussJordan
class GaussJordan:
    def __init__(self):  
        self.operaciones = OperacionesMatriz()  # Instancia la clase OperacionesMatriz para usar sus métodos
        self.max_value = 4000  # Define un valor máximo para evitar overflow (números extremadamente grandes)

# Método para resolver un sistema de ecuaciones mediante el método de Gauss-Jordan
    def resolver(self, matriz):
        pasos = []  # Lista para almacenar los pasos del proceso
        n = len(matriz)  # Número de filas (o columnas, ya que es una matriz cuadrada)
        
        # Verifica si hay algún valor en la matriz mayor que el límite definido
        for fila in matriz:
            for valor in fila:
                if abs(valor) > self.max_value:  # Si algún valor excede el límite
                    raise OverflowError("Números demasiado grandes.")  # Lanza un error de desbordamiento
        
        # Realiza el proceso de eliminación de Gauss-Jordan
        for i in range(n):
            # Obtiene el pivote de la diagonal de la fila i
            pivote = matriz[i][i]
            pasos.append(f"Dividir la fila {i+1} por {pivote:.3f}")  # Almacena el paso en el historial
            self.operaciones.multiplicar_fila(matriz, i, 1/pivote)  # Divide la fila actual por el valor del pivote
            pasos.append(self.operaciones.formato_matriz(matriz))  # Almacena la matriz resultante en el historial
            
            # Elimina los otros valores en la columna del pivote
            for j in range(n):
                if i != j:  # Evita operar sobre la misma fila
                    factor = matriz[j][i]  # Factor por el que se multiplicará para anular el valor en la columna
                    pasos.append(f"Restar {factor:.3f} veces la fila {i+1} de la fila {j+1}")  # Almacena el paso
                    self.operaciones.sumar_filas(matriz, j, i, -factor)  # Realiza la eliminación en la fila j
                    pasos.append(self.operaciones.formato_matriz(matriz))  # Almacena la matriz resultante
        
        return matriz, pasos  # Devuelve la matriz resultante y la lista de pasos
