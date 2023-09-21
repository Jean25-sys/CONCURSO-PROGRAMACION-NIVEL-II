def is_valid_walk(walk):
    if len(walk) != 10:
        return False
    
    x, y = 0, 0
    
    direcciones = {'n': (0, 1), 's': (0, -1), 'e': (1, 0), 'w': (-1, 0)}
    
    for direccion in walk:
        if direccion in direcciones:
            dx, dy = direcciones[direccion]
            x += dx
            y += dy
    
    return x == 0 and y == 0

print(is_valid_walk(['n','s','n','s','n','s','n','s','n','s']))  # True
print(is_valid_walk(['w','e','w','e','w','e','w','e','w','e','w','e']))  # False
print(is_valid_walk(['w']))  # False
print(is_valid_walk(['n','n','n','s','n','s','n','s','n','s']))  # False
