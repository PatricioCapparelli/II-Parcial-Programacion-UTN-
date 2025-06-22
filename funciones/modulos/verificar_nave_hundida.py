def verificar_y_sumar_puntaje_extra(matriz, fila_disparo, columna_disparo, puntaje_actual):
    # Verificar si la celda disparada es parte de una nave no hundida
    if matriz[fila_disparo][columna_disparo] != 2:
        return puntaje_actual, []

    # Inicializar conjuntos para el seguimiento
    partes_nave = set()
    celdas_visitadas = set()
    celdas_a_explorar = [(fila_disparo, columna_disparo)]
    
    # BFS para encontrar todas las partes conectadas de la nave
    while celdas_a_explorar:
        fila_actual, columna_actual = celdas_a_explorar.pop(0)
        
        if (fila_actual, columna_actual) in celdas_visitadas:
            continue
            
        celdas_visitadas.add((fila_actual, columna_actual))
        
        # Solo considerar celdas que son parte de una nave (1 o 2)
        if matriz[fila_actual][columna_actual] in (1, 2):
            partes_nave.add((fila_actual, columna_actual))
            
            # Explorar vecinos ortogonales
            for df, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nueva_fila = fila_actual + df
                nueva_col = columna_actual + dc
                
                # Verificar límites de la matriz
                if (0 <= nueva_fila < len(matriz) and 
                    0 <= nueva_col < len(matriz[0])):
                    celdas_a_explorar.append((nueva_fila, nueva_col))
    
    # Verificar si todas las partes de la nave han sido impactadas
    nave_hundida = True
    for fila, col in partes_nave:
        if matriz[fila][col] != 2:
            nave_hundida = False
            break
    
    if nave_hundida:
        # Calcular puntaje extra basado en el tamaño de la nave
        tamaño_nave = len(partes_nave)
        puntaje_extra = 5 * tamaño_nave  # Puntos por impactos
        puntaje_extra += 10 * tamaño_nave  # Puntos extra por hundir
        
        # Marcar la nave como hundida (podrías usar 3 para indicar hundido)
        for fila, col in partes_nave:
            matriz[fila][col] = 3  # Opcional: marcar como hundido
            
        return puntaje_actual + puntaje_extra, list(partes_nave)
    
    return puntaje_actual, []