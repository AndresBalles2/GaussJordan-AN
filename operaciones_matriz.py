class OperacionesMatriz:
    
    # Esta clase contiene métodos estáticos que realizan operaciones básicas sobre matrices
    @staticmethod
    def create_matriz(filas, columnas):
        # Crea y devuelve una matriz (lista de listas) de ceros con el número dado de filas y columnas
        # Se utiliza una lista para generar la matriz
        # filas: número de filas de la matriz
        # columnas: número de columnas de la matriz
        return [[0 for _ in range(columnas)] for _ in range(filas)]

    @staticmethod
    def copy_matriz(matriz):
        # Crea una copia de la matriz dada y la devuelve
        # Se utiliza una lista por comprensión para copiar cada fila de la matriz original
        # matriz: la matriz que se quiere copiar
        return [fila[:] for fila in matriz]  # Copia cada fila para evitar modificar la original

    @staticmethod
    def multiplicar_fila(matriz, fila, escalar):
        # Multiplica todos los elementos de la fila especificada por un escalar dado
        # matriz: la matriz en la que se quiere realizar la operación
        # fila: el índice de la fila que se va a multiplicar
        # escalar: el número por el que se multiplicará cada elemento de la fila
        for j in range(len(matriz[fila])):  # Recorre cada columna de la fila
            matriz[fila][j] *= escalar  # Multiplica el elemento actual por el escalar

    @staticmethod
    def sumar_filas(matriz, fila_destino, fila_origen, escalar):
        # Suma los elementos de la fila de origen multiplicados por el escalar a la fila de destino
        # matriz: la matriz en la que se quiere realizar la operación
        # fila_destino: el índice de la fila a la que se sumarán los elementos
        # fila_origen: el índice de la fila cuyos elementos se usarán para la suma
        # escalar: el número por el que se multiplicarán los elementos de la fila de origen antes de sumarlos
        for j in range(len(matriz[fila_destino])):  # Recorre cada columna de la fila destino
            matriz[fila_destino][j] += escalar * matriz[fila_origen][j]  # Suma el resultado a la fila destino

    @staticmethod
    def formato_matriz(matriz):
        # Formatea la matriz como una cadena de texto para su visualización
        # matriz: la matriz que se quiere convertir a texto
        # Convierte cada fila en una línea de texto, y cada elemento en un formato de 3 decimales
        return "\n".join([" ".join([f"{x:8.3f}" for x in fila]) for fila in matriz])