def verificar_nave_hundida(matriz, fila, col):
    """Verifica si el disparo hundió una nave completa con límite de tamaño"""
    if matriz[fila][col] != 2:
        return False, []

    # Buscar todas las partes conectadas de la nave
    partes_nave = []
    por_visitar = [[fila, col]]
    
    while por_visitar and len(partes_nave) < 4:  # Límite de 4 celdas
        actual = por_visitar.pop()
        if actual in partes_nave:
            continue
            
        partes_nave.append(actual)
        f, c = actual
        
        # Explorar vecinos ortogonales
        for df, dc in [[-1,0], [1,0], [0,-1], [0,1]]:
            nueva_fila = f + df
            nueva_col = c + dc
            
            if 0 <= nueva_fila < len(matriz) and (0 <= nueva_col < len(matriz[0])):
                if matriz[nueva_fila][nueva_col] in [1, 2]:
                    if [nueva_fila, nueva_col] not in partes_nave:
                        por_visitar.append([nueva_fila, nueva_col])

    # Verificar si todas las partes están impactadas (solo si no excedió el límite)
    nave_hundida = False
    if len(partes_nave) <= 4:  # Solo considerar naves de hasta 4 celdas
        nave_hundida = all(matriz[p[0]][p[1]] == 2 for p in partes_nave)

    # Ordenar las partes para comparación consistente
    partes_nave.sort()
    
    return nave_hundida, partes_nave