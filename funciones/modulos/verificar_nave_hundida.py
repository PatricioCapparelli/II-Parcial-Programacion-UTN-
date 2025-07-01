def verificar_nave_hundida(tablero:list, fila_inicial:int, columna_inicial:int) -> tuple[bool, list]:
    """Esta funcion se encarga de verificar si la nave disparada fue hundida o no.

    Args:
    -tabero:Recibe el tablero en forma de matriz
    -fila_inicial:Recibe un numero que representa la coordenada x
    -columna_inicial:Recibe un numero que representa la coordenada y

    Return: Retorna un booleano si la nave esta hundida o no, y en caso de estar hundida, una lista con las coordenadas de las partes que componen el barco
    """

    nave_hundida = False #flag
    partes_nave  = []  #lista vacia de partes de la nave detectadas

    #Encuentra una parte impactada en el tablero
    if tablero[fila_inicial][columna_inicial] == 2:
        
        filas_total = len(tablero)       # Cantidad de filas del tablero
        columnas_total = len(tablero[0])    # Cantidad de columnas

        # Matriz booleana que indica si una celda ya fue visitada
        visitada = []
        for indice_fila in range(filas_total):
            fila_visitada = []
            for indice_columna in range(columnas_total):
                fila_visitada.append(False)   # Al inicio ninguna celda esta visitada
            visitada.append(fila_visitada)

        pendientes = [(fila_inicial, columna_inicial)]  # Celdas por buscar ej: fila = 2, col = 4

        #Recorrer las casillas vecinas que forman parte de la misma nave
        while pendientes:
            fila_actual, columna_actual = pendientes.pop()   # Tomamos una celda pendiente

            # Si ya estaba revisada la salteamos
            if visitada[fila_actual][columna_actual] == True:
                continue

            # Marcamos la celda como visitada y la añadimos a la nave encontrada
            visitada[fila_actual][columna_actual] = True
            partes_nave.append([fila_actual, columna_actual])

            #teniendo en cuenta que ya sabemos que pertenece a la nave
            #ahora buscamos si las celdas vecinas son partes de la misma nave
            # Desplazamientos:   ↑:1 fila menos,    ↓:1 fila mas,    ←:1 columna menos,  →:1 columna mas
            desplazamientos = [(-1, 0), (1, 0), (0, -1), (0, 1)] 

            # le sumamos el desplazamiento a la fila y columna actual para saber la vecina
            for cambio_fila, cambio_columna in desplazamientos:
                fila_vecina = fila_actual + cambio_fila
                columna_vecina = columna_actual + cambio_columna

                # Verificamos que la vecina este dentro de los limites del tablero
                dentro_filas = (fila_vecina  >= 0) and (fila_vecina  < filas_total)
                dentro_columnas = (columna_vecina >= 0) and (columna_vecina < columnas_total)

                if dentro_filas and dentro_columnas: 
                    valor_vecino = tablero[fila_vecina][columna_vecina] #valor numerico de celda vecina

                    # Es parte de una nave si su valor es 1 (intacta) o 2 (impactada)
                    parte_de_nave = (valor_vecino == 1) or (valor_vecino == 2)

                    # La añadimos solo si todavia no la visitamos
                    pendiente_visita = visitada[fila_vecina][columna_vecina] == False

                    #Si esta vecina es una celda de un barco y todavia no la revise, la pongo en la lista para revisarla mas adelante
                    if parte_de_nave and pendiente_visita:
                        pendientes.append((fila_vecina, columna_vecina))

        # Determinar si la nave esta hundida
        tamaño_correcto = len(partes_nave) <= 4      # hasta 4 celdas

        # verifica que cada celda este impactada == 2
        todas_impactadas = True
        for fila_parte, columna_parte in partes_nave:
            if tablero[fila_parte][columna_parte] != 2:   # Encontramos una celda sin impactar en las coordenadas
                todas_impactadas = False
                break

        # La nave se considera hundida solo si cumple los dos criterios
        if tamaño_correcto and todas_impactadas:
            nave_hundida = True
        else:
            partes_nave = []      # Si no se hundio, no devolvemos las piezas

    return nave_hundida, partes_nave
