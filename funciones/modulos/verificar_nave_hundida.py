def verificar_nave_hundida(tablero, fila_inicial, columna_inicial):
    """Esta funcion se encarga de verificar si la nave disparada fue hundida o no.

    Args:
    -tabero:
    -fila_inicial:
    -columna_inicial:

    Return: Retorna un booleano si la nave esta hundida o no, y en caso de estar hundida, una lista con las coordenadas de las partes que componen el barco
    """

    #Estado inicial
    nave_hundida = False            # Partimos de la suposicion de que la nave no esta hundida
    partes_nave  = []               # Lista vacía de piezas detectadas

    #La casilla de partida debe estar impactada
    if tablero[fila_inicial][columna_inicial] == 2:

        #Preparar estructuras auxiliares
        filas_total = len(tablero)       # Cantidad de filas del tablero
        columnas_total = len(tablero[0])    # Cantidad de columnas

        # Matriz booleana que indica si una celda ya fue examinada
        visitada = []
        for indice_fila in range(filas_total):
            fila_visitada = []
            for indice_columna in range(columnas_total):
                fila_visitada.append(False)   # Al inicio, ninguna celda está visitada
            visitada.append(fila_visitada)

        pendientes = [(fila_inicial, columna_inicial)]  # Celdas por buscar

        #Recorrer las casillas vecinas que forman parte de la misma nave
        while pendientes:
            fila_actual, columna_actual = pendientes.pop()   # Tomamos una celda pendiente

            # Si ya la procesamos, saltamos a la siguiente
            if visitada[fila_actual][columna_actual] == True:
                continue

            # Marcamos la celda como visitada y la añadimos a la nave encontrada
            visitada[fila_actual][columna_actual] = True
            partes_nave.append([fila_actual, columna_actual])

            # Desplazamientos ortogonales: ↑ ↓ ← →
            desplazamientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            # Recorremos los cuatro vecinos ortogonales
            for cambio_fila, cambio_columna in desplazamientos:
                fila_vecina     = fila_actual + cambio_fila
                columna_vecina  = columna_actual + cambio_columna

                # Verificamos que la vecina esté dentro de los límites del tablero
                dentro_filas     = (fila_vecina  >= 0) and (fila_vecina  < filas_total)
                dentro_columnas  = (columna_vecina >= 0) and (columna_vecina < columnas_total)

                if dentro_filas and dentro_columnas:
                    valor_vecino = tablero[fila_vecina][columna_vecina]

                    # Es parte de una nave si su valor es 1 (intacta) o 2 (impactada)
                    parte_de_nave = (valor_vecino == 1) or (valor_vecino == 2)

                    # La añadimos solo si todavía no la visitamos
                    pendiente_visita = visitada[fila_vecina][columna_vecina] == False

                    if parte_de_nave and pendiente_visita:
                        pendientes.append((fila_vecina, columna_vecina))

        # Determinar si la nave esta hundida
        tamaño_correcto = len(partes_nave) <= 4      # Regla: naves de hasta 4 celdas

        # Comprobamos que cada pieza este impactada (valor 2)
        todas_impactadas = True
        for fila_parte, columna_parte in partes_nave:
            if tablero[fila_parte][columna_parte] != 2:   # Encontramos una pieza sin impactar
                todas_impactadas = False
                break

        # La nave se considera hundida solo si cumple ambos criterios
        if tamaño_correcto and todas_impactadas:
            nave_hundida = True
        else:
            partes_nave = []      # Si no se hundio, no devolvemos las piezas

    # ---------- Paso 5: unico return ----------
    return nave_hundida, partes_nave
