class OperacionesMatriz:
    @staticmethod
    def create_matriz(filas, columnas):
        return [[0 for _ in range(columnas)] for _ in range(filas)]

    @staticmethod
    def copy_matriz(matriz):
        return [fila[:] for fila in matriz]

    @staticmethod
    def multiplicar_fila(matriz, fila, escalar):
        for j in range(len(matriz[fila])):
            matriz[fila][j] *= escalar

    @staticmethod
    def sumar_filas(matriz, fila_destino, fila_origen, escalar):
        for j in range(len(matriz[fila_destino])):
            matriz[fila_destino][j] += escalar * matriz[fila_origen][j]

    @staticmethod
    def formato_matriz(matriz):
        return "\n".join([" ".join([f"{x:8.3f}" for x in fila]) for fila in matriz])
