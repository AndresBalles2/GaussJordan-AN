from operaciones_matriz import OperacionesMatriz
import math

class GaussJordan:
    def __init__(self):
        self.operaciones = OperacionesMatriz()
        self.max_value = 4000 #1e308

    def resolver(self, matriz):
        pasos = []
        n = len(matriz)
        
        for fila in matriz:
            for valor in fila:
                if abs(valor) > self.max_value:
                    raise OverflowError("Números demasiado grandes.")
        
        for i in range(n):
            
            pivote = matriz[i][i]
            pasos.append(f"Dividir la fila {i+1} por {pivote:.3f}")
            self.operaciones.multiplicar_fila(matriz, i, 1/pivote)
            pasos.append(self.operaciones.formato_matriz(matriz))
            
            
            for j in range(n):
                if i != j:
                    factor = matriz[j][i]
                    pasos.append(f"Restar {factor:.3f} veces la fila {i+1} de la fila {j+1}")
                    self.operaciones.sumar_filas(matriz, j, i, -factor)
                    pasos.append(self.operaciones.formato_matriz(matriz))
        
        return matriz, pasos
