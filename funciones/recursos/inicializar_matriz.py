def inicializar_matriz(cant_filas:int, cant_columnas:int, valor_inicial: any) -> list:
    """la funcion genera una matriz segun la cantidad de filas, columnas y valor que se le indique.
    Args:
        Recibe la cantidad de filas, columnas y el valor que se le dará a todos los numeros de la matriz.
    Returns:
        La matriz generada
    """
    matriz = []
    for i in range(cant_filas):
        fila = [valor_inicial] * cant_columnas
        matriz += [fila]
    return matriz

