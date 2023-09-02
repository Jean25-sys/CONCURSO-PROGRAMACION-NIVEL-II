def is_valid_walk(walk):
    # Verificar si la caminata dura exactamente diez minutos
    if len(walk) != 10:
        return False
    
    # Inicializar las coordenadas en (0, 0)
    x, y = 0, 0
    
    # Definir las direcciones (norte, sur, este, oeste)
    direcciones = {'n': (0, 1), 's': (0, -1), 'e': (1, 0), 'w': (-1, 0)}
    
    # Calcular las coordenadas finales
    for direccion in walk:
        if direccion in direcciones:
            dx, dy = direcciones[direccion]
            x += dx
            y += dy
    
    # Verificar si regresas al punto de partida (0, 0)
    return x == 0 and y == 0

# Pruebas de ejemplo
print(is_valid_walk(['n','s','n','s','n','s','n','s','n','s']))  # True
print(is_valid_walk(['w','e','w','e','w','e','w','e','w','e','w','e']))  # False
print(is_valid_walk(['w']))  # False
print(is_valid_walk(['n','n','n','s','n','s','n','s','n','s']))  # False