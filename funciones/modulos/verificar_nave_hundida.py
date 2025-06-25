def verificar_nave_hundida(matriz, fila, col):
    """Devuelve (hundida: bool, partes: list[[f,c],...]) para naves de hasta 4 celdas."""
    if matriz[fila][col] != 2:
        return False, []

    visitados   = set()
    por_visitar = [(fila, col)]

    while por_visitar:
        f, c = por_visitar.pop()
        if (f, c) in visitados:
            continue
        visitados.add((f, c))

        for df, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nf, nc = f + df, c + dc
            if 0 <= nf < len(matriz) and 0 <= nc < len(matriz[0]):
                if matriz[nf][nc] in (1, 2) and (nf, nc) not in visitados:
                    por_visitar.append((nf, nc))

    # ES UNA NAVE HUNDIDA
    hundida = (len(visitados) <= 4  and all(matriz[f][c] == 2 for f, c in visitados))

    #  Solo devolvemos la pieza si realmente esta hundida (para colorear en rojo)
    return hundida, [list(pos) for pos in visitados] if hundida else (False, [])
